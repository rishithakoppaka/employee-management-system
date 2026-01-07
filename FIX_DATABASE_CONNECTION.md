# Fix Database Connection Error

## Problem
You're seeing a `500 Internal Server Error` with the message:
```
connection to server at "localhost" (::1), port 5432 failed: Connection refused
```

This means the FastAPI backend cannot connect to PostgreSQL.

## Solution Steps

### Step 1: Start Docker Desktop
1. Open Docker Desktop application
2. Wait for it to fully start (you'll see "Docker Desktop is running" in the system tray)
3. This may take 30-60 seconds

### Step 2: Start PostgreSQL Container
Once Docker Desktop is running, execute:
```bash
docker-compose up -d
```

### Step 3: Verify Container is Running
```bash
docker ps
```

You should see `employee_db_postgres` in the list.

### Step 4: Test the Connection
Wait 5-10 seconds for PostgreSQL to fully initialize, then try the API again in Swagger UI.

---

## Quick Commands

```bash
# Check if Docker is running
docker ps

# Start database container
docker-compose up -d

# Check container status
docker ps | Select-String "postgres"

# View container logs (if issues)
docker logs employee_db_postgres

# Stop container (if needed)
docker-compose down
```

---

## Alternative: If Docker Desktop Won't Start

If Docker Desktop has issues, you can:

1. **Restart Docker Desktop:**
   - Right-click Docker Desktop icon in system tray
   - Select "Restart"

2. **Check Docker Desktop Status:**
   - Look for Docker icon in system tray
   - Should show "Docker Desktop is running"

3. **Manual Start:**
   - Open Docker Desktop from Start Menu
   - Wait for it to initialize

---

## Verify Database is Ready

After starting the container, you can verify PostgreSQL is ready:

```bash
# Check if port 5432 is listening
Test-NetConnection -ComputerName localhost -Port 5432
```

---

## Once Fixed

After the database is running:
1. The FastAPI backend should automatically reconnect
2. Try the `POST /employee` endpoint again in Swagger UI
3. It should work now! ✅

