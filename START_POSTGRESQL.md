# How to Start PostgreSQL on Windows

## Quick Fix for Connection Timeout

If you're seeing "connection timeout expired" in pgAdmin, PostgreSQL is not running. Here's how to start it:

## Method 1: Using Windows Services (Recommended)

1. **Open Services Manager:**
   - Press `Win + R`
   - Type `services.msc` and press Enter
   - OR search for "Services" in the Start menu

2. **Find PostgreSQL Service:**
   - Look for services named:
     - `postgresql-x64-XX` (where XX is version number, e.g., 15, 16)
     - `PostgreSQL`
     - `postgresql-x64-XX - PostgreSQL Server`

3. **Start the Service:**
   - Right-click on the PostgreSQL service
   - Click "Start"
   - If it's already running, try "Restart"

4. **Set to Auto-Start (Optional):**
   - Right-click the service → Properties
   - Set "Startup type" to "Automatic"
   - Click OK

## Method 2: Using Command Line (PowerShell as Administrator)

```powershell
# Find PostgreSQL service
Get-Service | Where-Object {$_.DisplayName -like "*PostgreSQL*"}

# Start PostgreSQL (replace with actual service name)
Start-Service postgresql-x64-16

# Or if you know the service name:
Start-Service -Name "postgresql-x64-16"
```

## Method 3: Using pgAdmin

1. Open pgAdmin 4
2. Right-click on your server (e.g., "Employee DB")
3. Select "Connect Server"
4. If it still times out, the service isn't running - use Method 1

## Method 4: Check if PostgreSQL is Installed

If you can't find the PostgreSQL service, it might not be installed:

1. Check installation location (common paths):
   - `C:\Program Files\PostgreSQL\`
   - `C:\Program Files (x86)\PostgreSQL\`

2. If not installed, download from:
   - https://www.postgresql.org/download/windows/

## Verify PostgreSQL is Running

After starting, verify it's running:

```powershell
# Check if port 5432 is listening
netstat -ano | findstr :5432

# Check PostgreSQL service status
Get-Service | Where-Object {$_.DisplayName -like "*PostgreSQL*"}
```

You should see port 5432 in LISTENING state.

## Common Issues

### Issue: Service won't start
- Check Windows Event Viewer for errors
- Verify PostgreSQL data directory exists and has correct permissions
- Try running PostgreSQL installer's "Service Configuration" tool

### Issue: Port 5432 already in use
- Another application might be using the port
- Check: `netstat -ano | findstr :5432`
- Change PostgreSQL port in `postgresql.conf` if needed

### Issue: Authentication failed
- Verify password in `.env` file matches PostgreSQL password
- Reset password if needed using pgAdmin or psql

## After Starting PostgreSQL

1. **Test connection in pgAdmin:**
   - Right-click server → Connect Server
   - Enter password
   - Should connect successfully

2. **Verify database exists:**
   - Expand server → Databases
   - Look for `employee_db`
   - If missing, create it (see below)

3. **Create database if needed:**
   ```sql
   CREATE DATABASE employee_db;
   ```

4. **Update `.env` file:**
   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=employee_db
   DB_USER=postgres
   DB_PASSWORD=your_actual_password
   ```

5. **Restart your FastAPI server:**
   - The API will automatically create the `employees` table on startup

## Quick Test

Once PostgreSQL is running, test the connection:

```powershell
# Test with psql (if installed)
psql -U postgres -h localhost -p 5432

# Or test from Python
python -c "import psycopg2; conn = psycopg2.connect(host='localhost', port=5432, database='postgres', user='postgres', password='your_password'); print('Connected!'); conn.close()"
```

