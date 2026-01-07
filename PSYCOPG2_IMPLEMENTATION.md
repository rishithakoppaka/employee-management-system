# psycopg2 Implementation - Raw SQL (No ORM)

## ✅ Confirmation: Using psycopg2 with Raw SQL

This project uses **psycopg2** for direct PostgreSQL connections with **raw SQL queries** - **NO ORM** (Object-Relational Mapping) is used.

---

## 🔧 Implementation Details

### 1. **Database Connection** (`get_db_connection()`)

**Location:** `db/db_utils.py`

```python
import psycopg2

def get_db_connection():
    """Create and return a database connection."""
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("DB_NAME", "employee_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "")
    )
    return conn
```

**Key Points:**
- ✅ Uses `psycopg2.connect()` directly
- ✅ No ORM layer (no SQLAlchemy, Django ORM, etc.)
- ✅ Direct connection to PostgreSQL
- ✅ Connection parameters from environment variables

---

## 📝 Raw SQL Queries Implementation

### 2. **Add Employee** (`add_employee()`)

**Raw SQL INSERT:**
```python
def add_employee(name: str, age: int, salary: float, department: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # RAW SQL QUERY - No ORM
    insert_query = """
    INSERT INTO employees (name, age, salary, department)
    VALUES (%s, %s, %s, %s)
    RETURNING id, name, age, salary, department;
    """
    
    # Parameterized query (prevents SQL injection)
    cursor.execute(insert_query, (name, age, salary, department))
    result = cursor.fetchone()
    conn.commit()
    
    # Manual data mapping (no ORM object mapping)
    employee_data = {
        "id": result[0],
        "name": result[1],
        "age": result[2],
        "salary": float(result[3]),
        "department": result[4]
    }
    
    cursor.close()
    conn.close()
    return employee_data
```

**Features:**
- ✅ Raw SQL `INSERT` statement
- ✅ Parameterized queries (`%s` placeholders)
- ✅ Manual result mapping to dictionary
- ✅ No ORM model classes

---

### 3. **Get All Employees** (`get_all_employees()`)

**Raw SQL SELECT:**
```python
def get_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # RAW SQL QUERY
    select_query = """
    SELECT id, name, age, salary, department
    FROM employees
    ORDER BY id;
    """
    
    cursor.execute(select_query)
    results = cursor.fetchall()
    
    # Manual conversion to list of dictionaries
    employees = []
    for row in results:
        employees.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "salary": float(row[3]),
            "department": row[4]
        })
    
    cursor.close()
    conn.close()
    return employees
```

**Features:**
- ✅ Raw SQL `SELECT` statement
- ✅ Manual row iteration
- ✅ Manual dictionary creation
- ✅ No ORM query builder

---

### 4. **Delete Employee** (`delete_employee_by_id()`)

**Raw SQL DELETE:**
```python
def delete_employee_by_id(employee_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # RAW SQL QUERY
    delete_query = """
    DELETE FROM employees
    WHERE id = %s;
    """
    
    cursor.execute(delete_query, (employee_id,))
    rows_deleted = cursor.rowcount
    conn.commit()
    
    cursor.close()
    conn.close()
    return rows_deleted > 0
```

**Features:**
- ✅ Raw SQL `DELETE` statement
- ✅ Parameterized query for safety
- ✅ Direct `rowcount` check
- ✅ No ORM delete methods

---

### 5. **Get Median Age** (`get_median_age()`)

**Raw SQL with Aggregate Function:**
```python
def get_median_age():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # RAW SQL with PostgreSQL function
    median_query = """
    SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY age) AS median_age
    FROM employees;
    """
    
    cursor.execute(median_query)
    result = cursor.fetchone()
    
    if result and result[0] is not None:
        return float(result[0])
    return None
```

**Features:**
- ✅ Raw SQL with PostgreSQL-specific function
- ✅ `PERCENTILE_CONT` for median calculation
- ✅ Direct SQL-level calculation (not Python-level)
- ✅ No ORM aggregation methods

---

### 6. **Get Median Salary** (`get_median_salary()`)

**Same approach as median age:**
```python
def get_median_salary():
    # Uses PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary)
    # Raw SQL, no ORM
```

---

## 🔒 Security: SQL Injection Prevention

### Parameterized Queries

**✅ Safe (Used in this project):**
```python
cursor.execute(
    "INSERT INTO employees (name, age) VALUES (%s, %s)",
    (name, age)  # Parameters passed separately
)
```

**❌ Unsafe (NOT used):**
```python
cursor.execute(f"INSERT INTO employees (name) VALUES ('{name}')")  # DON'T DO THIS
```

**Why it's safe:**
- psycopg2 automatically escapes parameters
- Prevents SQL injection attacks
- Type-safe parameter binding

---

## 📊 Comparison: ORM vs Raw SQL (This Project)

### ❌ What We DON'T Use (ORM):
```python
# SQLAlchemy ORM (NOT USED)
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

# ORM Query (NOT USED)
session.query(Employee).filter(Employee.id == 1).first()
```

### ✅ What We DO Use (Raw SQL):
```python
# Raw SQL (USED IN THIS PROJECT)
cursor.execute("SELECT * FROM employees WHERE id = %s", (1,))
result = cursor.fetchone()
```

---

## 🎯 Key Characteristics

### ✅ Raw SQL Approach:
1. **Direct SQL Queries** - Write SQL statements directly
2. **Manual Mapping** - Convert rows to dictionaries manually
3. **Cursor-based** - Use `cursor.execute()` and `cursor.fetchall()`
4. **Connection Management** - Manual `conn.close()` in finally blocks
5. **Transaction Control** - Manual `conn.commit()` and `conn.rollback()`

### ❌ No ORM Features:
- No model classes
- No query builders
- No automatic mapping
- No relationship management
- No migrations (manual SQL)

---

## 📁 File Structure

```
db/
└── db_utils.py  # All raw SQL queries here
    ├── get_db_connection()      # psycopg2.connect()
    ├── init_database()          # CREATE TABLE (raw SQL)
    ├── add_employee()           # INSERT (raw SQL)
    ├── get_all_employees()      # SELECT (raw SQL)
    ├── delete_employee_by_id()  # DELETE (raw SQL)
    ├── get_median_age()         # SELECT with PERCENTILE_CONT
    └── get_median_salary()      # SELECT with PERCENTILE_CONT
```

---

## 🔍 Verification

### Check for ORM Usage:
```bash
# Search for common ORM imports (should find nothing)
grep -r "sqlalchemy\|django.db\|peewee\|tortoise" .
```

### Verify psycopg2 Usage:
```bash
# Should find psycopg2 imports
grep -r "import psycopg2" .
```

### Verify Raw SQL:
```bash
# Should find raw SQL statements
grep -r "INSERT INTO\|SELECT.*FROM\|DELETE FROM" db/
```

---

## ✅ Requirements Met

| Requirement | Status | Implementation |
|------------|--------|----------------|
| Use psycopg2 | ✅ | `import psycopg2` in `db/db_utils.py` |
| Connect to PostgreSQL | ✅ | `psycopg2.connect()` with env vars |
| Raw SQL queries | ✅ | All queries use raw SQL strings |
| No ORM | ✅ | No ORM libraries imported or used |
| Parameterized queries | ✅ | All queries use `%s` placeholders |
| SQL injection prevention | ✅ | Parameters passed separately |

---

## 🎓 Summary

**This project uses:**
- ✅ **psycopg2** for database connections
- ✅ **Raw SQL queries** for all database operations
- ✅ **Parameterized queries** for security
- ✅ **Manual data mapping** (no ORM)
- ✅ **Direct cursor operations** (execute, fetchall, etc.)

**This project does NOT use:**
- ❌ SQLAlchemy ORM
- ❌ Django ORM
- ❌ Any other ORM framework
- ❌ Query builders
- ❌ Model classes

**Result:** Pure psycopg2 with raw SQL - exactly as required! 🎯

