# Github Repo Link

https://github.com/RaghavaBusanaboina/raghava_tutedude.git

# Flask & MongoDB Assignment

A simple Flask application that serves a JSON API and includes a frontend form that securely inserts data into MongoDB.

## Prerequisites
- Python 3.x
- Mongodb URI

## Setup Instructions

1. **Clone the repository:**

2. **Set up the virtual environment:**
   python3 -m venv venv
   source venv/bin/activate

3. **Install the requirements:**
   pip install -r requirements.txt


4. **Configure Environment Variables:**
   MONGO_URI

## Running the Application
Start the Flask server by running:
python app.py
The server will start on `http://127.0.0.1:8000/`.

## Routes
- `GET /` - Renders the form to collect user name and email.
- `POST /` - Accepts form submission and saves the data to MongoDB. Redirects to `/success` on success.
- `GET /api` - Returns JSON data loaded from `movies.json`.
