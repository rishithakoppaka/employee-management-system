# How to View Your PostgreSQL Database

## Option 1: Command Line (psql) - Quick Access

### Access PostgreSQL CLI directly:
```bash
docker exec -it employee_db_postgres psql -U postgres -d employee_db
```

Once inside, you can run SQL commands:
```sql
-- List all tables
\dt

-- View all employees
SELECT * FROM employees;

-- View table structure
\d employees

-- Exit
\q
```

### Quick one-liner commands:
```bash
# View all employees
docker exec -it employee_db_postgres psql -U postgres -d employee_db -c "SELECT * FROM employees;"

# Count employees
docker exec -it employee_db_postgres psql -U postgres -d employee_db -c "SELECT COUNT(*) FROM employees;"

# List all tables
docker exec -it employee_db_postgres psql -U postgres -d employee_db -c "\dt"
```

---

## Option 2: pgAdmin (GUI Tool) - Recommended for Visual Viewing

### Install pgAdmin:
1. Download from: https://www.pgadmin.org/download/
2. Install pgAdmin 4
3. Open pgAdmin

### Connect to Docker PostgreSQL:
1. Right-click "Servers" → "Create" → "Server"
2. **General Tab:**
   - Name: `Employee DB (Docker)`
3. **Connection Tab:**
   - Host: `localhost`
   - Port: `5432`
   - Database: `employee_db`
   - Username: `postgres`
   - Password: `postgres123`
4. Click "Save"

### View Data:
- Navigate to: Servers → Employee DB (Docker) → Databases → employee_db → Schemas → public → Tables → employees
- Right-click "employees" → "View/Edit Data" → "All Rows"

---

## Option 3: DBeaver (Free Universal Database Tool)

### Install DBeaver:
1. Download from: https://dbeaver.io/download/
2. Install DBeaver Community Edition (free)

### Connect:
1. Click "New Database Connection"
2. Select "PostgreSQL"
3. **Connection Settings:**
   - Host: `localhost`
   - Port: `5432`
   - Database: `employee_db`
   - Username: `postgres`
   - Password: `postgres123`
4. Click "Test Connection" → "Finish"

### View Data:
- Navigate to: employee_db → Schemas → public → Tables → employees
- Double-click "employees" to view data

---

## Option 4: VS Code Extension

### Install PostgreSQL Extension:
1. Open VS Code
2. Install extension: "PostgreSQL" by Chris Kolkman
3. Click the PostgreSQL icon in sidebar
4. Click "+" to add connection:
   - Host: `localhost`
   - Port: `5432`
   - Database: `employee_db`
   - User: `postgres`
   - Password: `postgres123`

---

## Option 5: TablePlus (Modern GUI - Paid/Free Trial)

1. Download from: https://tableplus.com/
2. Click "Create a new connection"
3. Select "PostgreSQL"
4. Enter:
   - Name: `Employee DB`
   - Host: `localhost`
   - Port: `5432`
   - User: `postgres`
   - Password: `postgres123`
   - Database: `employee_db`
5. Click "Test" → "Connect"

---

## Quick Verification Commands

### Check if database exists:
```bash
docker exec -it employee_db_postgres psql -U postgres -l
```

### Check if table exists:
```bash
docker exec -it employee_db_postgres psql -U postgres -d employee_db -c "\dt"
```

### View all data:
```bash
docker exec -it employee_db_postgres psql -U postgres -d employee_db -c "SELECT * FROM employees;"
```

### View table structure:
```bash
docker exec -it employee_db_postgres psql -U postgres -d employee_db -c "\d employees"
```

---

## Connection Details Summary

- **Host:** `localhost`
- **Port:** `5432`
- **Database:** `employee_db`
- **Username:** `postgres`
- **Password:** `postgres123`

These credentials work for any PostgreSQL client tool!

---

## Recommended: Start with Command Line

For quick checks, use the command line. For visual browsing and easier management, use **pgAdmin** or **DBeaver**.