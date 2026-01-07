# Application Flow - Employee Management System

## 🏗️ Architecture Overview

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│   Streamlit     │         │   FastAPI       │         │   PostgreSQL    │
│   Frontend      │◄───────►│   Backend       │◄───────►│   Database      │
│   (UI Layer)    │  HTTP   │   (API Layer)   │  SQL    │   (Data Layer)  │
└─────────────────┘         └─────────────────┘         └─────────────────┘
```

## 📊 Complete Application Flow

### **Layer 1: Frontend (Streamlit)**
- **File**: `streamlit_app.py`
- **Purpose**: User interface for interacting with the system
- **Technology**: Streamlit, Requests library

### **Layer 2: Backend (FastAPI)**
- **File**: `main.py`
- **Purpose**: RESTful API endpoints, request validation, business logic
- **Technology**: FastAPI, Pydantic models

### **Layer 3: Database Layer**
- **File**: `db/db_utils.py`
- **Purpose**: Raw SQL queries, database connections
- **Technology**: psycopg2, PostgreSQL

### **Layer 4: Data Models**
- **Files**: `models/person.py`, `models/employee.py`, `models/hr_manager.py`
- **Purpose**: Object-oriented data structures
- **Technology**: Python OOP

---

## 🔄 Detailed Flow for Each Operation

### **1. ADD EMPLOYEE Flow**

```
User Action (Streamlit)
    ↓
[User fills form: name, age, salary, department]
    ↓
[User clicks "Add Employee" button]
    ↓
streamlit_app.py → call_api("/employee", "POST", employee_data)
    ↓
HTTP POST Request → http://localhost:8000/employee
    ↓
FastAPI Backend (main.py)
    ↓
@app.post("/employee") receives request
    ↓
Pydantic validates data (EmployeeCreate model)
    ├─ Valid? → Continue
    └─ Invalid? → Return 422 error
    ↓
db_utils.add_employee(name, age, salary, department)
    ↓
Database Layer (db_utils.py)
    ↓
1. get_db_connection() → Connect to PostgreSQL
2. Execute SQL: INSERT INTO employees ...
3. RETURNING id, name, age, salary, department
4. Commit transaction
5. Close connection
    ↓
Return employee_data with generated ID
    ↓
FastAPI formats response (EmployeeResponse model)
    ↓
HTTP 201 Created Response
    ↓
Streamlit receives response
    ↓
Display success message + employee data
```

**Key Points:**
- ✅ Input validation at API level (Pydantic)
- ✅ SQL injection prevention (parameterized queries)
- ✅ Transaction management (commit/rollback)
- ✅ Error handling at each layer

---

### **2. VIEW ALL EMPLOYEES Flow**

```
User Action (Streamlit)
    ↓
[User opens "View Employees" tab OR clicks "Refresh"]
    ↓
streamlit_app.py → call_api("/employees", "GET")
    ↓
HTTP GET Request → http://localhost:8000/employees
    ↓
FastAPI Backend (main.py)
    ↓
@app.get("/employees") receives request
    ↓
db_utils.get_all_employees()
    ↓
Database Layer (db_utils.py)
    ↓
1. get_db_connection() → Connect to PostgreSQL
2. Execute SQL: SELECT id, name, age, salary, department FROM employees
3. Fetch all results
4. Convert to list of dictionaries
5. Close connection
    ↓
Return list of employee dictionaries
    ↓
FastAPI formats response (List[EmployeeResponse])
    ↓
HTTP 200 OK Response with JSON array
    ↓
Streamlit receives response
    ↓
format_employee_table() formats data
    ↓
Display in Streamlit dataframe/table
```

**Key Points:**
- ✅ No input needed (read-only operation)
- ✅ Returns all employees in one request
- ✅ Data formatted for display

---

### **3. DELETE EMPLOYEE Flow**

```
User Action (Streamlit)
    ↓
[User selects employee from dropdown]
    ↓
[User clicks "Delete Employee" button]
    ↓
streamlit_app.py → call_api(f"/employee/{id}", "DELETE")
    ↓
HTTP DELETE Request → http://localhost:8000/employee/1
    ↓
FastAPI Backend (main.py)
    ↓
@app.delete("/employee/{employee_id}") receives request
    ↓
Extract employee_id from URL path
    ↓
db_utils.delete_employee_by_id(employee_id)
    ↓
Database Layer (db_utils.py)
    ↓
1. get_db_connection() → Connect to PostgreSQL
2. Execute SQL: DELETE FROM employees WHERE id = %s
3. Check rows_deleted (cursor.rowcount)
4. Commit transaction
5. Close connection
    ↓
Return True (deleted) or False (not found)
    ↓
FastAPI checks result
    ├─ Found & Deleted? → Return 200 OK
    └─ Not Found? → Return 404 Not Found
    ↓
HTTP Response (200 or 404)
    ↓
Streamlit receives response
    ↓
Display success/error message
    ↓
Refresh employee list (st.rerun())
```

**Key Points:**
- ✅ ID extracted from URL path parameter
- ✅ Checks if employee exists before deletion
- ✅ Returns appropriate HTTP status codes
- ✅ UI refreshes after deletion

---

### **4. GET MEDIAN AGE Flow**

```
User Action (Streamlit)
    ↓
[User clicks "Get Median Age" button]
    ↓
streamlit_app.py → call_api("/stats/median-age", "GET")
    ↓
HTTP GET Request → http://localhost:8000/stats/median-age
    ↓
FastAPI Backend (main.py)
    ↓
@app.get("/stats/median-age") receives request
    ↓
db_utils.get_median_age()
    ↓
Database Layer (db_utils.py)
    ↓
1. get_db_connection() → Connect to PostgreSQL
2. Execute SQL: SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY age)
3. Fetch result (single value)
4. Close connection
    ↓
Return median_age (float) or None
    ↓
FastAPI formats response (StatsResponse model)
    ├─ Has value? → Return median_value + message
    └─ None? → Return null + "No employees found" message
    ↓
HTTP 200 OK Response
    ↓
Streamlit receives response
    ↓
Display median age metric
```

**Key Points:**
- ✅ Uses PostgreSQL's PERCENTILE_CONT function (SQL-level calculation)
- ✅ Handles empty database case
- ✅ Returns formatted message

---

### **5. GET MEDIAN SALARY Flow**

```
[Same as Median Age, but for salary field]
    ↓
SQL: SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary)
    ↓
Returns median salary value
```

---

## 🚀 Application Startup Flow

```
1. User runs: uvicorn main:app --reload
    ↓
2. FastAPI app initializes
    ↓
3. @app.on_event("startup") triggers
    ↓
4. db_utils.init_database() called
    ↓
5. Database Layer:
   - Connect to PostgreSQL
   - Execute: CREATE TABLE IF NOT EXISTS employees (...)
   - Commit transaction
   - Close connection
    ↓
6. Server starts on http://localhost:8000
    ↓
7. Auto-generated Swagger docs available at /docs
```

---

## 🔐 Security & Validation Flow

### **Input Validation Chain:**

```
User Input (Streamlit Form)
    ↓
Streamlit validates (basic checks)
    ↓
HTTP Request sent
    ↓
FastAPI receives request
    ↓
Pydantic Model Validation (EmployeeCreate)
    ├─ name: min_length=1, max_length=255
    ├─ age: gt=0, le=150
    ├─ salary: gt=0
    └─ department: min_length=1, max_length=100
    ↓
If invalid → HTTP 422 Unprocessable Entity
    ↓
If valid → Continue to database
    ↓
SQL Parameterized Query (prevents SQL injection)
    ↓
Database validates constraints
    ↓
Success or Database Error
```

---

## 📡 Request/Response Flow Example

### **Example: Adding Employee "John Doe"**

**Request (from Streamlit):**
```http
POST http://localhost:8000/employee
Content-Type: application/json

{
  "name": "John Doe",
  "age": 30,
  "salary": 50000.0,
  "department": "Engineering"
}
```

**Response (from FastAPI):**
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "salary": 50000.0,
  "department": "Engineering"
}
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,              -- Auto-incrementing ID
    name VARCHAR(255) NOT NULL,         -- Employee name
    age INTEGER NOT NULL,               -- Employee age
    salary DECIMAL(10, 2) NOT NULL,     -- Employee salary
    department VARCHAR(100) NOT NULL,    -- Department name
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Auto timestamp
);
```

---

## 🔄 Error Handling Flow

```
Any Layer
    ↓
Error occurs (Database, Network, Validation, etc.)
    ↓
Exception caught
    ↓
Error logged/printed
    ↓
Appropriate HTTP status code returned
    ├─ 400: Bad Request
    ├─ 404: Not Found
    ├─ 422: Validation Error
    └─ 500: Internal Server Error
    ↓
Streamlit receives error
    ↓
User-friendly error message displayed
```

---

## 🎯 Key Design Patterns

1. **Separation of Concerns**: UI, API, Database layers are separate
2. **RESTful API**: Standard HTTP methods (GET, POST, DELETE)
3. **Data Validation**: Pydantic models ensure data integrity
4. **Raw SQL**: Direct database queries (no ORM) as per requirements
5. **Error Handling**: Try-catch blocks at each layer
6. **Connection Management**: Proper database connection open/close
7. **Transaction Management**: Commit on success, rollback on error

---

## 📝 Summary

**Frontend (Streamlit)** → Makes HTTP requests → **Backend (FastAPI)** → Executes SQL → **Database (PostgreSQL)** → Returns data → **Backend** → Formats response → **Frontend** → Displays to user

Each layer has a specific responsibility and communicates with the next layer through well-defined interfaces!

