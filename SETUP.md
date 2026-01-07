# Quick Setup Guide

## Prerequisites

1. **Python 3.8+** installed
2. **PostgreSQL** installed and running
3. **PostgreSQL database** created

## Step-by-Step Setup

### 1. Create PostgreSQL Database

```sql
CREATE DATABASE employee_db;
```

### 2. Create Environment File

Create a `.env` file in the project root with the following content:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=your_password_here

API_HOST=0.0.0.0
API_PORT=8000
API_BASE_URL=http://localhost:8000
```

Replace `your_password_here` with your actual PostgreSQL password.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Backend

```bash
uvicorn main:app --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 5. Run the Frontend (in a new terminal)

```bash
streamlit run streamlit_app.py
```

The Streamlit app will open at http://localhost:8501

### 6. Test the Application

1. Open the Streamlit app in your browser
2. Add some employees using the "Add Employee" tab
3. View employees in the "View Employees" tab
4. Check statistics in the "Statistics" tab
5. Delete employees using the "Delete Employee" tab

### 7. Run Tests

```bash
# Backend tests
pytest tests/test_api.py -v

# Frontend tests
pytest tests/test_ui_logic.py -v

# All tests
pytest tests/ -v
```

### 8. Test with Postman

1. Import `postman_collection.json` into Postman
2. Test all endpoints

### 9. Security Scan

```bash
# Install Snyk CLI (requires Node.js)
npm install -g snyk

# Authenticate
snyk auth

# Run scan
snyk test
```

## Troubleshooting

### Database Connection Issues

- Ensure PostgreSQL is running
- Verify database credentials in `.env`
- Check that the database `employee_db` exists

### Port Already in Use

- Change `API_PORT` in `.env` if port 8000 is taken
- Update `API_BASE_URL` in `.env` accordingly
- Change Streamlit port: `streamlit run streamlit_app.py --server.port 8502`

### Module Not Found Errors

- Ensure you're in the project root directory
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check Python path includes the project directory



