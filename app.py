from flask import Flask, jsonify, request, render_template, redirect, url_for
from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
MONGO_URI = os.getenv("MONGO_URI")
# add comment in new branch
if not MONGO_URI:
    print("MONGO_URI is not set in ENV.")

try:
    client = MongoClient(MONGO_URI)
    db = client['tutedude_db']
    collection = db['users']
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        if not name or not email:
            error = "Name and Email are required!"
        else:
            try:
                collection.insert_one({"name": name, "email": email})
                return redirect(url_for('success'))
            except Exception as e:
                error = f"Database error: {str(e)}"
    return render_template('index.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')
    
@app.route('/todo', methods=['GET', 'POST'])
def todo():
    message = None
    if request.method == 'POST':
        item_name = request.form.get('item_name')
        item_description = request.form.get('item_description')
        item_id = request.form.get('item_id')
        item_UUID = request.form.get('item_UUID')
        item_hash = request.form.get('item_hash')
        if item_name and item_description:
            try:
                # Save the to-do item to MongoDB
                db['todos'].insert_one({"item_name": item_name, "item_description": item_description,"item_id":item_id,"item_UUID":item_UUID,"item_hash":item_hash})
                message = "To-Do item added successfully!"
            except Exception as e:
                message = f"Error adding item: {str(e)}"
        else:
            message = "Both fields are required."
            
    return render_template('todo.html', message=message)

@app.route('/api', methods=['GET'])
def get_api_data():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, 'movies.json')
        
        with open(json_path, 'r') as file:
            data = json.load(file)
            
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
