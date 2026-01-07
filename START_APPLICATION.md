# How to Start Your Application

## 🔄 Restart Backend (Required - Password Updated)

The backend needs to be restarted to pick up the new password. Here's how:

### Step 1: Stop Current Backend
1. Find the terminal where `uvicorn main:app --reload` is running
2. Press `Ctrl+C` to stop it

### Step 2: Restart Backend
In the project directory (`c:\Users\rishi\Downloads\module1`), run:
```bash
uvicorn main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
Database initialized successfully
```

### Step 3: Verify It Works
Open in browser: http://localhost:8000

You should see:
```json
{"message":"Employee Management API","version":"1.0.0","docs":"/docs"}
```

---

## 🚀 Complete Startup Sequence

### Terminal 1: Backend
```bash
cd c:\Users\rishi\Downloads\module1
uvicorn main:app --reload
```

### Terminal 2: Frontend
```bash
cd c:\Users\rishi\Downloads\module1
streamlit run streamlit_app.py
```

### Terminal 3: Database (Already Running)
```bash
# Check status
docker ps

# View logs if needed
docker-compose logs postgres
```

---

## ✅ Quick Verification Checklist

- [ ] PostgreSQL container running: `docker ps` shows `employee_db_postgres`
- [ ] Backend running: http://localhost:8000 shows API message
- [ ] Database table created: Check with `docker exec employee_db_postgres psql -U postgres -d employee_db -c "\dt"`
- [ ] Frontend running: http://localhost:8501 opens Streamlit UI

---

## 🎯 After Restarting Backend

1. The `employees` table will be created automatically
2. You can verify with:
   ```bash
   docker exec employee_db_postgres psql -U postgres -d employee_db -c "\dt"
   ```
3. Then start the frontend and start using the app!


