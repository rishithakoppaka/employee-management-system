# Docker Setup Guide for Employee Management System

## 🐳 Using Docker for PostgreSQL

Instead of installing PostgreSQL directly on Windows, you can use Docker Desktop to run PostgreSQL in a container!

## Quick Start with Docker

### Step 1: Start PostgreSQL Container

```bash
docker-compose up -d
```

This will:
- Download PostgreSQL 15 image (if not already downloaded)
- Create a container named `employee_db_postgres`
- Create the database `employee_db` automatically
- Expose PostgreSQL on port 5432
- Persist data in a Docker volume

### Step 2: Update Your `.env` File

Update your `.env` file with these values:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=postgres123
API_BASE_URL=http://localhost:8000
```

**Note**: The password matches what's in `docker-compose.yml`. You can change it in both files if you want.

### Step 3: Verify Container is Running

```bash
docker ps
```

You should see `employee_db_postgres` running.

### Step 4: Test Database Connection

```bash
docker exec -it employee_db_postgres psql -U postgres -d employee_db
```

Or test from your Python app by starting the backend:
```bash
uvicorn main:app --reload
```

The table will be created automatically on first run!

## Docker Commands Reference

### Start PostgreSQL
```bash
docker-compose up -d
```

### Stop PostgreSQL
```bash
docker-compose down
```

### View Logs
```bash
docker-compose logs postgres
```

### Access PostgreSQL CLI
```bash
docker exec -it employee_db_postgres psql -U postgres -d employee_db
```

### Remove Container and Data
```bash
docker-compose down -v
```
⚠️ **Warning**: This deletes all data!

### Check Container Status
```bash
docker ps
```

## Alternative: Manual Docker Run

If you prefer not to use docker-compose:

```bash
docker run --name employee_db_postgres \
  -e POSTGRES_DB=employee_db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres123 \
  -p 5432:5432 \
  -d postgres:15-alpine
```

## Benefits of Using Docker

✅ **No Installation**: No need to install PostgreSQL on Windows
✅ **Isolated**: Database runs in a container, separate from your system
✅ **Easy Cleanup**: Remove container when done
✅ **Consistent**: Same PostgreSQL version across different machines
✅ **Portable**: Works the same on Windows, Mac, Linux

## Troubleshooting

### Port Already in Use
If port 5432 is already taken:
1. Change port in `docker-compose.yml`: `"5433:5432"`
2. Update `.env`: `DB_PORT=5433`

### Container Won't Start
```bash
docker-compose logs postgres
```
Check the logs for errors.

### Reset Database
```bash
docker-compose down -v
docker-compose up -d
```

### Check if Container is Running
```bash
docker ps -a
```

## Next Steps

1. Start PostgreSQL: `docker-compose up -d`
2. Update `.env` with correct password
3. Start backend: `uvicorn main:app --reload`
4. Start frontend: `streamlit run streamlit_app.py`

That's it! Your database is ready to use! 🚀


