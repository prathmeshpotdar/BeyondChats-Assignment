# BeyondChats Article Upgrader

A full-stack automated content enhancement system. This application scrapes/seeds blog articles, serves them via a Laravel API, and uses an AI agent (OpenAI/Groq) to rewrite and enhance the content in the background, displaying real-time updates on a React frontend.

## 🏗️ Architecture & Data Flow

The system operates as a pipeline of four distinct micro-services.


```
graph TD
    A[Python Seeder] -- 1. Seeds Initial Data --> B(Laravel Backend / SQLite DB)
    C[React Frontend] -- 2. Polls for Updates --> B
    D[Node.js Processor] -- 3. Fetches Pending Articles --> B
    D -- 4. Retrieves Context --> E[Static Context / Search]
    D -- 5. Generates Content --> F[OpenAI / Groq API]
    F -- 6. Returns Enhanced Text --> D
    D -- 7. Updates Database --> B
🚀 Features
Multi-Service Architecture: Decoupled Backend, Frontend, and AI Processor.

Real-time Updates: Frontend reflects AI changes immediately without page reloads.

Robust Error Handling: Failsafe modes for API keys and search context.

Automated Pipeline: Seamless flow from "Pending" to "AI Enhanced" status.

🛠️ Tech Stack
Backend: PHP 8.2, Laravel 10, SQLite

Frontend: React.js, CSS3

AI Engine: Node.js, OpenAI API (or Groq SDK)

Data Ops: Python 3 (Requests)

⚙️ Local Setup Instructions
Follow these steps to run the entire suite locally.

Prerequisites
Ensure you have the following installed:

Node.js & npm

PHP & Composer

Python 3

Git

1. Backend Setup (Laravel)
The backend serves the API and manages the SQLite database.

Bash

cd backend-laravel

# Install PHP dependencies
composer install

# Setup Environment
cp .env.example .env
# Open .env and ensure: DB_CONNECTION=sqlite

# Create Database File (Linux/Mac)
touch database/database.sqlite
# OR for Windows (PowerShell):
# New-Item -ItemType File database/database.sqlite

# Run Migrations
php artisan migrate:fresh

# Start Server
php artisan serve
Server will start at http://127.0.0.1:8000

2. Frontend Setup (React)
The user interface for viewing original vs. enhanced articles.

Bash

cd frontend-react

# Install JS dependencies
npm install

# Start Application
npm start
App will run at http://localhost:3000

3. Seed Data (Python)
Populates the database with initial "Pending" articles.

Bash

cd scraper-python

# Install requests if needed
pip install requests

# Run the seeder
python force_seed.py
You should see a success message indicating the article was inserted.

4. AI Processor Setup (Node.js)
The worker script that connects to OpenAI/Groq to rewrite content.

Bash

cd processor-node

# Install dependencies
npm install

# Configure API Key
cp .env.example .env
# Open .env and add your key:
# OPENAI_API_KEY=sk-your-key-here
# LARAVEL_API_URL=[http://127.0.0.1:8000/api/articles](http://127.0.0.1:8000/api/articles)

# Run the Processor
node index.js
📸 Usage Guide
Initial State: Open the React App (localhost:3000). You will see the article card in a Red/Pending state.

Process: Run the node index.js script in your terminal.

Result: Watch the terminal for "SUCCESS: Database updated."

Final State: The React App card will automatically turn Green, displaying the AI-rewritten content.

📂 Project Structure
/backend-laravel: REST API (Controllers, Migrations, Models).

/frontend-react: UI Components (App.js, CSS).

/processor-node: AI logic and Context generation.

/scraper-python: Data seeding scripts.

🔗 Live Demo


Frontend: http://localhost:3000

Backend API: http://127.0.0.1:8000
