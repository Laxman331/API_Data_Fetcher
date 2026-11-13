# API Data Fetcher

A beginner Python project that retrieves posts from a REST API, collects records using pagination, and stores the results in a JSON file.

## Features

- Fetches data from a REST API using the Requests library.
- Retrieves records page by page using pagination.
- Handles HTTP and request errors.
- Collects API records into a Python list.
- Saves collected data into a JSON file.
- Reads saved JSON data back into Python.
- Uses reusable Python functions.

## Technologies Used

- Python 3.13
- Requests
- JSON
- REST API
- Git

## API Used

JSONPlaceholder: https://jsonplaceholder.typicode.com/posts

## Project Structure

```text
API_Data_Fetcher/
├── .gitignore
├── main.py
├── posts.json
├── requirements.txt
└── README.md
```

## Installation and Setup

1. Clone the repository.
2. Create a virtual environment:

   `python -m venv .venv`

3. Activate it on Windows PowerShell:

   `.\.venv\Scripts\Activate.ps1`

4. Install dependencies:

   `python -m pip install -r requirements.txt`

5. Run the application:

   `python main.py`

## Output

The application retrieves 100 posts from the API and saves them into `posts.json`.

## Learning Outcomes

- Python functions and loops
- HTTP GET requests
- REST API integration
- Query parameters and pagination
- Exception handling
- JSON serialization and deserialization
- File handling