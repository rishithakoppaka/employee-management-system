# How to Run the Application

## 🚀 Quick Start

### Step 1: Start PostgreSQL (Docker)
```bash
docker-compose up -d
```
**Status Check:**
```bash
docker ps
```
Should show `employee_db_postgres` running.

---

### Step 2: Start Backend API

**Terminal 1:**
```bash
cd c:\Users\rishi\Downloads\module1
uvicorn main:app --reload
```

**Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
Database initialized successfully
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Verify:**
- Open: http://localhost:8000
- Should see: `{"message":"Employee Management API","version":"1.0.0","docs":"/docs"}`

---

### Step 3: Start Frontend (Streamlit)

**Terminal 2 (New Terminal):**
```bash
cd c:\Users\rishi\Downloads\module1
streamlit run streamlit_app.py
```

**Expected Output:**
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

**Browser:**
- Automatically opens at http://localhost:8501
- Or manually open the URL

---

## ✅ Verification Checklist

- [ ] PostgreSQL running: `docker ps` shows container
- [ ] Backend running: http://localhost:8000 shows API message
- [ ] Swagger docs: http://localhost:8000/docs accessible
- [ ] Frontend running: http://localhost:8501 opens Streamlit UI
- [ ] Database connected: No connection errors in backend logs

---

## 🎯 Access Points

| Service | URL | Description |
|---------|-----|-------------|
| **Backend API** | http://localhost:8000 | FastAPI server |
| **Swagger Docs** | http://localhost:8000/docs | Interactive API docs |
| **ReDoc** | http://localhost:8000/redoc | Alternative API docs |
| **Frontend UI** | http://localhost:8501 | Streamlit application |

---

## 🛑 Stop Application

### Stop Frontend:
- Press `Ctrl+C` in Streamlit terminal

### Stop Backend:
- Press `Ctrl+C` in uvicorn terminal

### Stop Database:
```bash
docker-compose down
```

---

## 🐛 Troubleshooting

### Backend Won't Start:
- Check if port 8000 is available
- Verify `.env` file exists and has correct credentials
- Check PostgreSQL is running: `docker ps`

### Frontend Can't Connect:
- Ensure backend is running first
- Check `API_BASE_URL` in `.env` matches backend URL
- Look for connection errors in browser console

### Database Connection Error:
- Verify Docker container: `docker ps`
- Check `.env` credentials match `docker-compose.yml`
- Restart container: `docker-compose restart`

---

## 📝 Quick Commands

```bash
# Start everything
docker-compose up -d          # Database
uvicorn main:app --reload     # Backend (Terminal 1)
streamlit run streamlit_app.py # Frontend (Terminal 2)

# Check status
docker ps                      # Database
curl http://localhost:8000/   # Backend
# Open http://localhost:8501  # Frontend

# Stop everything
# Ctrl+C in both terminals
docker-compose down           # Database
```

---

**Your application is ready to run!** 🚀


