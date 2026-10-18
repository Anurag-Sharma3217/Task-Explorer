# Task Explorer

A Python command-line application that retrieves and explores tasks using the JSONPlaceholder REST API.

## Features

- View tasks by user ID
- View completed tasks for a user
- Search for tasks by exact title
- Retrieve task details by ID
- Search task titles using partial, case-insensitive matching
- Validate numeric input and permitted ID ranges
- Handle HTTP request errors and timeouts
- Use reusable functions and separate utility modules

## Technologies Used

- Python
- Requests
- REST APIs and HTTP
- JSON
- Git and GitHub

## Project Structure

```text
Task-Explorer/
├── Main.py
├── Function.py
├── Utils.py
├── README.md
└── LICENSE
```

## Requirements

- Python 3.10 or later
- The `requests` library
- An internet connection

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Anurag-Sharma3217/Task-Explorer
   ```

2. Enter the project directory:

   ```bash
   cd Task-Explorer
   ```

3. Install the dependency:

   ```bash
   python -m pip install requests
   ```

## Run the Application

```bash
python Main.py
```

Follow the numbered menu options to explore tasks.

## API

This project uses the JSONPlaceholder API:

https://jsonplaceholder.typicode.com/todos

JSONPlaceholder is a free testing API. Requests demonstrate API integration, but creating or modifying test data does not provide permanent storage.

## Learning Objectives

This project demonstrates:

- Making HTTP GET requests with Python
- Passing query parameters
- Parsing JSON responses
- Handling HTTP and network errors
- Searching and filtering dictionaries in lists
- Organizing Python code across multiple modules
- Building a menu-driven command-line application

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.