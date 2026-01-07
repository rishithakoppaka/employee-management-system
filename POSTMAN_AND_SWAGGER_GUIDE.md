# Postman & Swagger Documentation Guide

## ✅ Swagger Auto-Generated Docs

### Access Swagger UI

**URL:** http://localhost:8000/docs

**Features:**
- ✅ Interactive API documentation
- ✅ Test endpoints directly in browser
- ✅ See request/response schemas
- ✅ View all 5 endpoints
- ✅ Try it out functionality

### How to Use Swagger UI:

1. **Open in Browser:**
   - Navigate to: http://localhost:8000/docs
   - You'll see all API endpoints listed

2. **Test an Endpoint:**
   - Click on any endpoint (e.g., `POST /employee`)
   - Click "Try it out" button
   - Fill in the request body
   - Click "Execute"
   - See the response below

3. **Available Endpoints in Swagger:**
   - `GET /` - Root endpoint
   - `POST /employee` - Add employee
   - `GET /employees` - Get all employees
   - `DELETE /employee/{employee_id}` - Delete employee
   - `GET /stats/median-age` - Get median age
   - `GET /stats/median-salary` - Get median salary

---

## 📬 Postman Collection

### Import Postman Collection

**File:** `postman_collection.json`

**Steps to Import:**

1. **Open Postman**
2. **Click "Import"** (top left)
3. **Select "File"** tab
4. **Click "Upload Files"**
5. **Select:** `postman_collection.json` from project root
6. **Click "Import"**

### Postman Collection Contents

The collection includes all 5 endpoints:

1. **Root** - `GET http://localhost:8000/`
2. **Add Employee** - `POST http://localhost:8000/employee`
3. **Get All Employees** - `GET http://localhost:8000/employees`
4. **Delete Employee** - `DELETE http://localhost:8000/employee/1`
5. **Get Median Age** - `GET http://localhost:8000/stats/median-age`
6. **Get Median Salary** - `GET http://localhost:8000/stats/median-salary`

---

## 🧪 Testing in Postman

### 1. Test POST /employee (Add Employee)

**Request:**
- **Method:** POST
- **URL:** `http://localhost:8000/employee`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "name": "John Doe",
    "age": 30,
    "salary": 50000.0,
    "department": "Engineering"
  }
  ```

**Expected Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "salary": 50000.0,
  "department": "Engineering"
}
```
**Status:** 201 Created

---

### 2. Test GET /employees (Get All Employees)

**Request:**
- **Method:** GET
- **URL:** `http://localhost:8000/employees`
- **Headers:** None needed

**Expected Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "salary": 50000.0,
    "department": "Engineering"
  }
]
```
**Status:** 200 OK

---

### 3. Test DELETE /employee/{id} (Delete Employee)

**Request:**
- **Method:** DELETE
- **URL:** `http://localhost:8000/employee/1`
- **Headers:** None needed

**Expected Response:**
```json
{
  "message": "Employee with ID 1 deleted successfully",
  "deleted": true
}
```
**Status:** 200 OK

**If Not Found:**
```json
{
  "detail": "Employee with ID 999 not found"
}
```
**Status:** 404 Not Found

---

### 4. Test GET /stats/median-age (Get Median Age)

**Request:**
- **Method:** GET
- **URL:** `http://localhost:8000/stats/median-age`
- **Headers:** None needed

**Expected Response:**
```json
{
  "median_value": 32.5,
  "message": "Median age: 32.50"
}
```
**Status:** 200 OK

**If No Employees:**
```json
{
  "median_value": null,
  "message": "No employees found to calculate median age"
}
```

---

### 5. Test GET /stats/median-salary (Get Median Salary)

**Request:**
- **Method:** GET
- **URL:** `http://localhost:8000/stats/median-salary`
- **Headers:** None needed

**Expected Response:**
```json
{
  "median_value": 55000.0,
  "message": "Median salary: $55,000.00"
}
```
**Status:** 200 OK

---

## 📋 Postman Collection Structure

```json
{
  "info": {
    "name": "Employee Management API",
    "description": "Postman collection for Employee Management System API"
  },
  "item": [
    {
      "name": "Root",
      "request": {
        "method": "GET",
        "url": "http://localhost:8000/"
      }
    },
    {
      "name": "Add Employee",
      "request": {
        "method": "POST",
        "url": "http://localhost:8000/employee",
        "body": {
          "raw": "{\n    \"name\": \"John Doe\",\n    \"age\": 30,\n    \"salary\": 50000.0,\n    \"department\": \"Engineering\"\n}"
        }
      }
    },
    // ... other endpoints
  ]
}
```

---

## 🔍 Swagger UI Features

### What You Can Do in Swagger:

1. **View All Endpoints:**
   - See all available API endpoints
   - View HTTP methods (GET, POST, DELETE)
   - See request/response schemas

2. **Test Endpoints:**
   - Click "Try it out" on any endpoint
   - Fill in parameters/body
   - Click "Execute"
   - See live response

3. **View Schemas:**
   - See Pydantic models
   - View required/optional fields
   - See data types and constraints

4. **Copy cURL Commands:**
   - Click "Try it out"
   - Fill in request
   - Scroll down to see cURL command
   - Copy and use in terminal

---

## 🎯 Quick Test Workflow

### Step 1: Open Swagger UI
1. Open browser: http://localhost:8000/docs
2. Verify all endpoints are visible

### Step 2: Test in Swagger
1. Click `POST /employee`
2. Click "Try it out"
3. Fill in JSON body:
   ```json
   {
     "name": "Jane Smith",
     "age": 25,
     "salary": 60000.0,
     "department": "Marketing"
   }
   ```
4. Click "Execute"
5. See response (201 Created with employee data)

### Step 3: Import Postman Collection
1. Open Postman
2. Import `postman_collection.json`
3. Run "Get All Employees" request
4. Verify you see the employee you just added

### Step 4: Test All Endpoints
1. Add employee (POST)
2. Get all employees (GET)
3. Get median age (GET)
4. Get median salary (GET)
5. Delete employee (DELETE)

---

## 📊 Endpoint Summary

| Endpoint | Method | Path | Description |
|----------|--------|------|-------------|
| Root | GET | `/` | API information |
| Add Employee | POST | `/employee` | Create new employee |
| Get Employees | GET | `/employees` | Get all employees |
| Delete Employee | DELETE | `/employee/{id}` | Delete by ID |
| Median Age | GET | `/stats/median-age` | Calculate median age |
| Median Salary | GET | `/stats/median-salary` | Calculate median salary |

---

## 🔗 Quick Links

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc (Alternative):** http://localhost:8000/redoc
- **OpenAPI JSON:** http://localhost:8000/openapi.json
- **API Root:** http://localhost:8000/

---

## ✅ Verification Checklist

- [ ] Swagger UI accessible at `/docs`
- [ ] All 5 endpoints visible in Swagger
- [ ] Postman collection imported
- [ ] All endpoints testable in Postman
- [ ] Request/response schemas visible
- [ ] "Try it out" works in Swagger
- [ ] All endpoints return correct responses

---

## 🎓 Tips

### Swagger UI:
- Use "Try it out" to test without leaving browser
- Copy cURL commands for terminal use
- View schemas to understand data structure

### Postman:
- Save requests to collection
- Create environment variables for base URL
- Use collection runner to test all endpoints
- Export test results

---

## 📝 Example Test Sequence

1. **Add Employee:**
   ```json
   POST /employee
   {
     "name": "Alice Johnson",
     "age": 28,
     "salary": 55000.0,
     "department": "HR"
   }
   ```

2. **Get All Employees:**
   ```
   GET /employees
   ```
   Should return Alice in the list

3. **Get Median Age:**
   ```
   GET /stats/median-age
   ```
   Should calculate median of all ages

4. **Get Median Salary:**
   ```
   GET /stats/median-salary
   ```
   Should calculate median of all salaries

5. **Delete Employee:**
   ```
   DELETE /employee/{id}
   ```
   Replace {id} with Alice's ID

---

**Both Swagger and Postman are ready to use!** 🚀

