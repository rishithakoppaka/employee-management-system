# Start Application - Quick Guide

## ✅ Current Status

- ✅ **PostgreSQL Database**: Running in Docker
- ⏳ **Backend API**: Starting...
- ⏳ **Frontend UI**: Not started yet

---

## 🚀 Start the Application

### Step 1: Start Backend (Terminal 1)

Open a **new terminal** and run:

```bash
cd c:\Users\rishi\Downloads\module1
uvicorn main:app --reload
```

**Wait for:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
Database initialized successfully
```

**Verify it's working:**
- Open browser: http://localhost:8000
- Should see: `{"message":"Employee Management API"...}`

---

### Step 2: Start Frontend (Terminal 2)

Open **another new terminal** and run:

```bash
cd c:\Users\rishi\Downloads\module1
streamlit run streamlit_app.py
```

**Wait for:**
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

**Browser will open automatically** at http://localhost:8501

---

## 🎯 What You'll See

### Backend (http://localhost:8000)
- API root endpoint
- Swagger docs at `/docs`
- All 5 API endpoints ready

### Frontend (http://localhost:8501)
- Employee Management System UI
- 4 tabs: Add, View, Delete, Statistics
- Ready to add/view/manage employees

---

## ✅ Quick Verification

After starting both:

1. **Backend:** http://localhost:8000/docs (Swagger UI)
2. **Frontend:** http://localhost:8501 (Streamlit UI)
3. **Test:** Add an employee in Streamlit, view in Swagger

---

## 🛑 To Stop

- **Backend:** Press `Ctrl+C` in Terminal 1
- **Frontend:** Press `Ctrl+C` in Terminal 2
- **Database:** `docker-compose down` (optional)

---

**Ready to start! Open two terminals and run the commands above.** 🚀


