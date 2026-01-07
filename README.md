# Employee Management System - Fullstack CRUD App

A complete fullstack application built with FastAPI, PostgreSQL, and Streamlit for managing employees.

## Tech Stack

- **Backend**: FastAPI, PostgreSQL, psycopg2
- **Frontend**: Streamlit
- **Testing**: Pytest
- **Security**: Snyk
- **Tools**: Postman, Requests, dotenv

## Project Structure

```
module1/
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── employee.py
│   └── hr_manager.py
├── db/
│   ├── __init__.py
│   └── db_utils.py
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_ui_logic.py
├── main.py
├── streamlit_app.py
├── requirements.txt
├── .env.example
├── postman_collection.json
└── README.md
```

## Setup Instructions

### 1. Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE employee_db;
```

### 2. Environment Configuration

Copy `.env.example` to `.env` and update with your database credentials:

```bash
cp .env.example .env
```

Edit `.env` with your PostgreSQL connection details.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Schema

The application will automatically create the `employees` table on first run. The schema includes:
- `id` (SERIAL PRIMARY KEY)
- `name` (VARCHAR)
- `age` (INTEGER)
- `salary` (DECIMAL)
- `department` (VARCHAR)

### 5. Run the Backend API

```bash
uvicorn main:app --reload
```

The API will be available at:
- API: http://localhost:8000
- Swagger Docs: http://localhost:8001/docs
- ReDoc: http://localhost:8000/redoc

### 6. Run the Frontend

In a separate terminal:

```bash
streamlit run streamlit_app.py
```

The Streamlit app will open in your browser at http://localhost:8501

## API Endpoints

- `POST /employee` - Add a new employee
- `GET /employees` - Get all employees
- `DELETE /employee/{id}` - Delete an employee by ID
- `GET /stats/median-age` - Get median age of all employees
- `GET /stats/median-salary` - Get median salary of all employees

## Testing

Run backend tests:
```bash
pytest tests/test_api.py -v
```

Run frontend tests:
```bash
pytest tests/test_ui_logic.py -v
```

## Security Scan

To perform a Snyk vulnerability scan:

```bash
snyk test
```

Or use the Snyk CLI to generate a report:
```bash
snyk test --json > snyk_report.md
```

## Postman Collection

Import `postman_collection.json` into Postman to test all API endpoints.

## Demo Video

Record a 2-3 minute walkthrough demonstrating:
1. Adding employees via Streamlit UI
2. Viewing all employees
3. Viewing median age and salary
4. Deleting an employee
5. Testing API endpoints in Postman/Swagger


