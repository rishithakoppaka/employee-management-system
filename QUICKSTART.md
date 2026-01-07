# Quick Start Guide

Get up and running in 5 minutes!

## Prerequisites Check

- [ ] Python 3.8+ installed (`python --version`)
- [ ] PostgreSQL installed and running
- [ ] Database `employee_db` created

## 5-Minute Setup

### Step 1: Install Dependencies (1 min)
```bash
pip install -r requirements.txt
```

### Step 2: Configure Environment (1 min)
Create `.env` file:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=your_password
API_BASE_URL=http://localhost:8000
```

### Step 3: Start Backend (1 min)
```bash
uvicorn main:app --reload
```
✅ API running at http://localhost:8000
✅ Docs at http://localhost:8000/docs

### Step 4: Start Frontend (1 min)
New terminal:
```bash
streamlit run streamlit_app.py
```
✅ UI opens at http://localhost:8501

### Step 5: Test It! (1 min)
1. Add an employee in Streamlit
2. View employees
3. Check statistics
4. Delete an employee

## Common Commands

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_api.py -v

# Check API health
curl http://localhost:8000/

# View API docs
# Open http://localhost:8000/docs in browser
```

## Troubleshooting

**Database connection error?**
- Check PostgreSQL is running
- Verify `.env` credentials
- Ensure database exists: `CREATE DATABASE employee_db;`

**Port already in use?**
- Change port in `.env`: `API_PORT=8001`
- Update `API_BASE_URL` accordingly

**Module not found?**
- Ensure you're in project root
- Run: `pip install -r requirements.txt`

## Next Steps

- Import `postman_collection.json` into Postman
- Run `snyk test` for security scan
- Record demo video showing full CRUD flow

Happy coding! 🚀


