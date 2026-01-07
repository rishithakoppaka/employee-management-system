# Next Steps - Your Application is Running! 🚀

## ✅ What's Already Done

1. ✅ PostgreSQL database running in Docker
2. ✅ `.env` file configured with correct password
3. ✅ FastAPI backend running at http://localhost:8000
4. ✅ Database table `employees` created automatically

## 🎯 Next: Start the Frontend

### Open a NEW terminal window and run:

```bash
cd c:\Users\rishi\Downloads\module1
streamlit run streamlit_app.py
```

This will:
- Open your browser automatically
- Show the Employee Management System UI
- Allow you to add, view, and delete employees

---

## 🌐 Access Points

### 1. **Streamlit Frontend** (Main UI)
- **URL:** http://localhost:8501
- **What it does:** User interface for managing employees
- **Start with:** `streamlit run streamlit_app.py`

### 2. **FastAPI Backend** (API)
- **URL:** http://localhost:8000
- **Status:** ✅ Already running!
- **Test it:** Open http://localhost:8000 in browser

### 3. **API Documentation** (Swagger)
- **URL:** http://localhost:8000/docs
- **What it does:** Interactive API documentation
- **Try it:** Test API endpoints directly in browser

### 4. **Alternative API Docs** (ReDoc)
- **URL:** http://localhost:8000/redoc
- **What it does:** Alternative API documentation view

---

## 🧪 Test the Application

### Step 1: Start Frontend
```bash
streamlit run streamlit_app.py
```

### Step 2: Use the UI
1. **Add Employee Tab:**
   - Fill in name, age, salary, department
   - Click "Add Employee"
   - See success message

2. **View Employees Tab:**
   - See all employees in a table
   - Click "Refresh" to update

3. **Statistics Tab:**
   - Click "Get Median Age"
   - Click "Get Median Salary"
   - See calculated statistics

4. **Delete Employee Tab:**
   - Select employee from dropdown
   - Click "Delete Employee"

### Step 3: Test API Directly
- Open http://localhost:8000/docs
- Try the endpoints:
  - `POST /employee` - Add employee
  - `GET /employees` - Get all employees
  - `DELETE /employee/{id}` - Delete employee
  - `GET /stats/median-age` - Get median age
  - `GET /stats/median-salary` - Get median salary

---

## 📊 View Database

### Command Line:
```bash
# View all employees
docker exec employee_db_postgres psql -U postgres -d employee_db -c "SELECT * FROM employees;"

# Count employees
docker exec employee_db_postgres psql -U postgres -d employee_db -c "SELECT COUNT(*) FROM employees;"
```

### GUI Tools:
- **pgAdmin:** See `VIEW_DATABASE.md` for setup
- **DBeaver:** See `VIEW_DATABASE.md` for setup

---

## 🧪 Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run only API tests
pytest tests/test_api.py -v

# Run only UI tests
pytest tests/test_ui_logic.py -v
```

---

## 📝 Postman Collection

1. Open Postman
2. Import `postman_collection.json`
3. Test all endpoints

---

## 🎥 Demo Video Checklist

Record a 2-3 minute video showing:
- [ ] Adding employees via Streamlit UI
- [ ] Viewing all employees
- [ ] Viewing median age and salary
- [ ] Deleting an employee
- [ ] Testing API endpoints in Swagger/Postman

---

## 🛑 Stop Services

### Stop Frontend:
- Press `Ctrl+C` in the Streamlit terminal

### Stop Backend:
- Press `Ctrl+C` in the uvicorn terminal
- Or find the process and kill it

### Stop Database:
```bash
docker-compose down
```

### Stop Everything:
```bash
# Stop backend (Ctrl+C)
# Stop frontend (Ctrl+C)
docker-compose down
```

---

## 🐛 Troubleshooting

### Backend not responding?
- Check if it's running: `curl http://localhost:8000/`
- Check logs for errors
- Verify `.env` has correct password

### Frontend can't connect to API?
- Ensure backend is running first
- Check `API_BASE_URL` in `.env` matches backend URL
- Check browser console for errors

### Database connection error?
- Verify Docker container is running: `docker ps`
- Check `.env` credentials match `docker-compose.yml`
- Restart container: `docker-compose restart`

---

## 🎉 You're All Set!

Your fullstack CRUD application is ready to use! Start the frontend and begin managing employees.


