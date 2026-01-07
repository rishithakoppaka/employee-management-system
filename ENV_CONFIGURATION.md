# Environment Configuration Guide

## 📋 Current Configuration

Your `.env` file is located at: `c:\Users\rishi\Downloads\module1\.env`

### Current Settings:
```env
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=postgres123

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_BASE_URL=http://localhost:8000
```

---

## 🔧 Environment Variables Explained

### Database Configuration

| Variable | Value | Description | Used By |
|----------|-------|-------------|---------|
| `DB_HOST` | `localhost` | PostgreSQL server address | `db/db_utils.py` |
| `DB_PORT` | `5432` | PostgreSQL server port | `db/db_utils.py` |
| `DB_NAME` | `employee_db` | Database name | `db/db_utils.py` |
| `DB_USER` | `postgres` | PostgreSQL username | `db/db_utils.py` |
| `DB_PASSWORD` | `postgres123` | PostgreSQL password | `db/db_utils.py` |

**How it's used:**
- Loaded by `python-dotenv` in `db/db_utils.py`
- Used to create database connections via `psycopg2`
- Default values provided if not set

### API Configuration

| Variable | Value | Description | Used By |
|----------|-------|-------------|---------|
| `API_HOST` | `0.0.0.0` | FastAPI server host (0.0.0.0 = all interfaces) | `main.py` (via uvicorn) |
| `API_PORT` | `8000` | FastAPI server port | `main.py` (via uvicorn) |
| `API_BASE_URL` | `http://localhost:8000` | Base URL for API calls | `streamlit_app.py` |

**How it's used:**
- `API_BASE_URL` is used by Streamlit frontend to make HTTP requests
- `API_HOST` and `API_PORT` can be used when starting uvicorn programmatically

---

## 📍 Where Environment Variables Are Loaded

### 1. Backend (FastAPI)
**File:** `db/db_utils.py`
```python
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

# Used in get_db_connection()
host=os.getenv("DB_HOST", "localhost")
port=os.getenv("DB_PORT", "5432")
database=os.getenv("DB_NAME", "employee_db")
user=os.getenv("DB_USER", "postgres")
password=os.getenv("DB_PASSWORD", "")
```

### 2. Frontend (Streamlit)
**File:** `streamlit_app.py`
```python
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

# Used for API calls
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
```

---

## 🔄 How to Update Configuration

### Option 1: Edit `.env` File Directly
1. Open `.env` file in your editor
2. Modify the values
3. Restart the application (backend/frontend)

### Option 2: Use Command Line (PowerShell)
```powershell
# Update password
(Get-Content .env) -replace 'DB_PASSWORD=.*', 'DB_PASSWORD=new_password' | Set-Content .env

# Update API URL
(Get-Content .env) -replace 'API_BASE_URL=.*', 'API_BASE_URL=http://localhost:8001' | Set-Content .env
```

---

## 🎯 Common Configuration Scenarios

### Scenario 1: Change Database Port
If PostgreSQL runs on a different port (e.g., 5433):
```env
DB_PORT=5433
```

### Scenario 2: Change API Port
If port 8000 is already in use:
```env
API_PORT=8001
API_BASE_URL=http://localhost:8001
```

### Scenario 3: Remote Database
If connecting to a remote PostgreSQL server:
```env
DB_HOST=192.168.1.100  # Remote IP address
DB_PORT=5432
DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=your_remote_password
```

### Scenario 4: Different Database Name
```env
DB_NAME=my_employee_db
```

---

## ✅ Verification

### Check Current Configuration
```powershell
# View .env file
Get-Content .env

# Test database connection
docker exec employee_db_postgres psql -U postgres -d employee_db -c "SELECT version();"

# Test API connection
curl http://localhost:8000/
```

### Verify Environment Variables Are Loaded
```python
# In Python
import os
from dotenv import load_dotenv

load_dotenv()
print(f"DB_HOST: {os.getenv('DB_HOST')}")
print(f"DB_NAME: {os.getenv('DB_NAME')}")
print(f"API_BASE_URL: {os.getenv('API_BASE_URL')}")
```

---

## 🔒 Security Best Practices

1. **Never commit `.env` to Git**
   - Already in `.gitignore`
   - Use `.env.example` as template

2. **Use Strong Passwords**
   - Change default `postgres123` in production
   - Use environment-specific passwords

3. **Restrict Access**
   - Limit who can read `.env` file
   - Use environment variables in production (not files)

4. **Separate Configurations**
   - Development: `.env`
   - Production: Environment variables or secure vault

---

## 🐛 Troubleshooting

### Issue: Database Connection Failed
**Check:**
- Is PostgreSQL running? `docker ps`
- Are credentials correct in `.env`?
- Is port 5432 accessible?

**Solution:**
```powershell
# Verify Docker container
docker ps | Select-String "postgres"

# Test connection
docker exec employee_db_postgres psql -U postgres -d employee_db -c "SELECT 1;"
```

### Issue: Frontend Can't Connect to API
**Check:**
- Is `API_BASE_URL` correct in `.env`?
- Is backend running? `curl http://localhost:8000/`

**Solution:**
```powershell
# Verify API_BASE_URL
Get-Content .env | Select-String "API_BASE_URL"

# Test API
curl http://localhost:8000/
```

### Issue: Environment Variables Not Loading
**Check:**
- Is `.env` file in project root?
- Is `python-dotenv` installed? `pip list | Select-String "dotenv"`

**Solution:**
```powershell
# Verify .env exists
Test-Path .env

# Reinstall dotenv
pip install python-dotenv
```

---

## 📝 Environment Variable Defaults

If environment variables are not set, the application uses these defaults:

| Variable | Default Value | Location |
|----------|---------------|----------|
| `DB_HOST` | `localhost` | `db/db_utils.py` |
| `DB_PORT` | `5432` | `db/db_utils.py` |
| `DB_NAME` | `employee_db` | `db/db_utils.py` |
| `DB_USER` | `postgres` | `db/db_utils.py` |
| `DB_PASSWORD` | `""` (empty) | `db/db_utils.py` |
| `API_BASE_URL` | `http://localhost:8000` | `streamlit_app.py` |

---

## 🎓 Summary

- **Location:** `.env` file in project root
- **Loaded by:** `python-dotenv` library
- **Used in:** `db/db_utils.py` and `streamlit_app.py`
- **Current Status:** ✅ Properly configured
- **Security:** ✅ In `.gitignore`, not committed

Your environment is correctly configured! The application will use these values automatically when you start the backend and frontend.

