# FastAPI CRUD Application with MongoDB

This project is a FastAPI-based application that performs CRUD (Create, Read, Update, Delete) operations for managing **Items** and **User Clock-In Records**. It integrates with MongoDB as the database and is designed to handle filtering and aggregation. The project includes unit tests for all the CRUD operations.

## Features

- **Items CRUD operations**: Create, Read, Update, Delete items.
- **Clock-In Records**: Manage user clock-in records with time and location data.
- **MongoDB Integration**: Uses MongoDB to store data.
- **Data Filtering**: Filter items based on specific fields like email.
- **Aggregation**: Get item counts by email.
- **Asynchronous API calls**: Fully async API with asynchronous MongoDB operations.
- **Unit Tests**: Unit tests using `pytest` and `httpx` to ensure the correctness of the endpoints.

## Table of Contents
- [Project Setup](#project-setup)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [Items API](#items-api)
  - [Clock-In API](#clock-in-api)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Setup

### Prerequisites

- Python 3.10 or higher
- MongoDB (local or cloud, e.g., MongoDB Atlas)
- Git
- A MongoDB URI

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rahul-charaki/fastapi-crud-app.git
    cd fastapi-crud-app
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables**:
    Create a `.env` file in the root of the project directory:
    ```bash
    touch .env
    ```
    Add the following environment variables to the `.env` file:
    ```bash
    MONGO_URI="your_mongodb_uri"
    ```

5. **Run MongoDB**: Ensure your MongoDB service is running locally or on a cloud service like MongoDB Atlas.

## Running the Application

1. **Start the FastAPI server**:
    ```bash
    uvicorn app.main:app --reload
    ```

2. **Access the API documentation**:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints

### Items API
- **POST /items**: Create a new item.
- **GET /items**: Get all items with optional filtering.
- **GET /items/{item_id}**: Retrieve a single item by its ID.
- **PUT /items/{item_id}**: Update an existing item.
- **DELETE /items/{item_id}**: Delete an item by its ID.
- **GET /items/aggregation**: Get item counts by email.

### Clock-In API
- **POST /clock_in**: Record a user clock-in with time and location.
- **GET /clock_in/{id}**: Retrieve a clock-in record by ID.
- **PUT /clock_in/{id}**: Update a clock-in record by ID.
- **DELETE /clock_in/{id}**: Delete a clock-in record by ID.
- **GET /clock_in**: Get all clock-in records (with optional filtering).

## Running Tests

This project uses `pytest` for unit testing. The tests cover the main functionalities of the Items and Clock-In APIs, including creating, reading, updating, and deleting records.

1. **Install the test dependencies**:
    ```bash
    pip install -r requirements-dev.txt
    ```

2. **Run the test suite**:
    ```bash
    pytest
    ```

This will execute all the tests, and you'll see the results in the terminal.

## Project Structure

```bash
.
├── app
│   ├── main.py                 # Entry point for FastAPI app
│   ├── models.py               # MongoDB models for Items and Clock-In Records
│   ├── routes                  # API route definitions
│       └── clock_in.py         # colck in api functions
│       └── items.py            # items api functions
│   ├── database.py             # MongoDB database connection setup
│   ├── schemas.py              # MongoDB schemas for Items and Clock-In Records
├── test_main.py                # Unit tests for Items and Clock-In APIs
├── .env                        # Environment variables
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development and test dependencies
└── README.md                   # Project documentation
