# Github Repo Link

https://github.com/RaghavaBusanaboina/raghava_tutedude.git

# Branches
- main
- master_1
- master_2
- tutedude_new
- raghava_tutedude

# Flask & MongoDB Assignment

A simple Flask application that serves a JSON API and includes a frontend form that securely inserts data into MongoDB.

## Prerequisites
- Python 3.x
- MongoDB URI

## Setup Instructions

1. **Clone the repository using SSH:**
   ```bash
   git clone git@github.com:RaghavaBusanaboina/raghava_tutedude.git
   ```

2. **Set up the virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   - Create a `.env` file in the root directory.
   - Add your MongoDB connection string securely:
     ```
     MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
     ```

## Running the Application
Start the Flask server by running:
```bash
python app.py
```
The server will start on `http://127.0.0.1:8000/`.

## Routes
- `GET /` - Renders the form to collect user name and email.
- `POST /` - Accepts form submission and saves the data to MongoDB. Redirects to `/success` on success.
- `GET /api` - Returns JSON data loaded from `movies.json`.
- `GET /submittodoitem` - Renders the To-Do item form.
- `POST /submittodoitem` - Saves a new To-Do item to the database.

---

## Assignment Evidence: Git Workflow Documentation

Throughout this assignment, various Git workflows were utilized to manage features, resolve conflicts, and maintain a clean commit history. Here is the evidence of the required steps:

### 1. SSH Repository Cloning
The repository is cloned securely using SSH instead of HTTPS to ensure secure, password-less authentication. (See Setup Instructions above).

### 2. Branching & Updating the JSON API
The `movies.json` file (which powers the `/api` route) was updated in a completely separate feature branch (`tutedude_new`).
```bash
git branch -M tutedude_new
# Modifications made to movies.json (added Telugu movies & IDs)
git add movies.json
git commit -m "update movies json in tutedude_new branch"
git push origin tutedude_new
```

### 3. Resolving Merge Conflicts
During the merge of the `tutedude_new` branch back into `main`, and during the rebase operations with `master_1`, merge conflicts were encountered. 
- Git paused the operation and highlighted conflicting lines (e.g., changes to `app.py` and `todo.html`).
- The conflicts were resolved by manually editing the files to **accept the changes from the feature branch** (incorporating both the base features and the new fields like `item_id`, `item_UUID`, and `item_hash`).
- After resolving, the merge/rebase was finalized with `git add .` and `git rebase --continue`.

### 4. Rollback using `git reset --soft`
To isolate specific changes (like committing only the `item_id` field), a soft reset was performed. This rolled back the commit history while keeping the file changes staged, allowing for a precise, isolated commit.
```bash
git reset --soft 68119cd166972349a0a2536980ef3dd2c55b06dd
git add . && git commit -m "rollback to id commit"
git push -f origin main
```

### 5. Advanced Rebasing
To integrate updates from `main` into the `master_1` branch cleanly without creating a messy web of merge commits, a rebase was performed:
```bash
git checkout main
git rebase main master_1
git add . 
git rebase --continue
git push -f origin master_1
```
- **Preserving Individual Commits:** By default, standard `git rebase` replays commits individually without squashing them, maintaining a granular commit history where each change remains its own distinct commit.

### 6. Resolving Merge Conflicts & Finalizing Features
Features built across different branches (`master_1` and `master_2`) were merged back into `main`. Merge conflicts were manually resolved and committed.
```bash
git checkout main
git merge master_1
git merge master_2
git add . && git commit -m "todo template and route merged from master 1 and 2"
git push origin main
```
