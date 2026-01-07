# How Tests Were Performed - Testing Methodology

## 🧪 Testing Framework & Tools

### Primary Tools Used:
1. **pytest** - Python testing framework
2. **FastAPI TestClient** - For testing API endpoints
3. **unittest.mock** - For mocking dependencies
4. **pytest-asyncio** - For async test support

---

## 📋 Testing Approach: Unit Testing with Mocking

### Why Mocking?
- **Isolation**: Tests don't require a real database
- **Speed**: Tests run faster (no database I/O)
- **Reliability**: Tests don't depend on database state
- **Independence**: Tests can run in any order

---

## 🔧 Backend API Tests (`test_api.py`)

### Testing Strategy: **Mock Database Layer**

#### 1. **Test Client Setup**
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)  # Creates a test HTTP client
```

**What it does:**
- Creates an in-memory test client
- Simulates HTTP requests to your API
- No actual server needed

#### 2. **Mocking Database Functions**

**Example: Testing Add Employee**
```python
@patch('db.db_utils.add_employee')  # Mock the database function
def test_add_employee_success(self, mock_add_employee):
    # Define what the mock should return
    mock_add_employee.return_value = {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "salary": 50000.0,
        "department": "Engineering"
    }
    
    # Make actual HTTP request to API
    response = client.post("/employee", json=employee_data)
    
    # Verify response
    assert response.status_code == 201
    assert response.json()["id"] == 1
```

**How it works:**
1. `@patch` decorator replaces `db.db_utils.add_employee` with a mock
2. Mock returns predefined data (simulating database)
3. API endpoint uses the mock (not real database)
4. Test verifies API behavior with mocked data

#### 3. **Test Categories**

**A. Endpoint Tests (No Mocking Needed)**
```python
def test_root_endpoint(self):
    response = client.get("/")  # Direct HTTP call
    assert response.status_code == 200
```
- Tests endpoints that don't use database
- Direct HTTP requests

**B. CRUD Operation Tests (With Mocking)**
```python
@patch('db.db_utils.add_employee')
def test_add_employee_success(self, mock_add_employee):
    mock_add_employee.return_value = {...}
    response = client.post("/employee", json={...})
    # Verify API response
```
- Mocks database functions
- Tests API endpoint logic
- Verifies request/response handling

**C. Validation Tests (No Mocking)**
```python
def test_add_employee_validation_error(self):
    invalid_data = {"name": "", "age": -5}  # Invalid data
    response = client.post("/employee", json=invalid_data)
    assert response.status_code == 422  # Validation error
```
- Tests Pydantic validation
- No database needed

**D. Error Handling Tests (With Mocking)**
```python
@patch('db.db_utils.add_employee')
def test_add_employee_database_error(self, mock_add_employee):
    mock_add_employee.side_effect = Exception("Database error")
    response = client.post("/employee", json={...})
    assert response.status_code == 500  # Server error
```
- Mocks database to throw errors
- Tests error handling in API

---

## 🎨 Frontend UI Tests (`test_ui_logic.py`)

### Testing Strategy: **Mock HTTP Requests**

#### 1. **Data Formatting Tests (No Mocking)**
```python
def test_format_employee_table_single(self):
    employees = [{"id": 1, "name": "John Doe", ...}]
    result = format_employee_table(employees)
    assert "John Doe" in result
```
- Tests pure functions (no external dependencies)
- Direct function calls
- Verifies output format

#### 2. **API Integration Tests (With Mocking)**
```python
@patch('streamlit_app.requests.get')  # Mock HTTP requests
def test_call_api_get_success(self, mock_get):
    # Create mock HTTP response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": "test"}
    mock_get.return_value = mock_response
    
    # Call the function
    data, error, status_code = call_api("/employees", "GET")
    
    # Verify results
    assert data == {"data": "test"}
    assert error is None
    assert status_code == 200
```

**How it works:**
1. `@patch` replaces `requests.get` with a mock
2. Mock returns predefined HTTP response
3. Function uses mock (not real API)
4. Test verifies function handles response correctly

#### 3. **Error Scenario Tests**
```python
@patch('streamlit_app.requests.get')
def test_call_api_connection_error(self, mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError()
    data, error, status_code = call_api("/employees", "GET")
    assert "Connection error" in error
```
- Mocks HTTP errors
- Tests error handling in UI functions

---

## 🚀 Test Execution Process

### Step 1: Test Discovery
```bash
pytest tests/ -v
```
- Pytest finds all `test_*.py` files
- Discovers all `test_*` functions
- Organizes tests by class

### Step 2: Test Execution Flow

**For Each Test:**
1. **Setup Phase:**
   - Create test client (for API tests)
   - Apply mocks (if needed)
   - Prepare test data

2. **Execution Phase:**
   - Run the test function
   - Execute API calls or function calls
   - Mocks intercept and return predefined data

3. **Assertion Phase:**
   - Verify response status codes
   - Check response data
   - Validate error messages

4. **Teardown Phase:**
   - Clean up mocks
   - Reset state (automatic with pytest)

### Step 3: Results Collection
- Collect pass/fail status
- Count assertions
- Report warnings

---

## 📊 Example: Complete Test Flow

### Backend Test Example

```python
@patch('db.db_utils.get_all_employees')
def test_get_all_employees_success(self, mock_get_all):
    # 1. SETUP: Define mock behavior
    mock_get_all.return_value = [
        {"id": 1, "name": "John", "age": 30, ...},
        {"id": 2, "name": "Jane", "age": 25, ...}
    ]
    
    # 2. EXECUTION: Make HTTP request
    response = client.get("/employees")
    
    # 3. ASSERTION: Verify results
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "John"
```

**What happens:**
1. Mock replaces `db.db_utils.get_all_employees`
2. API endpoint calls the mock (not real database)
3. Mock returns predefined employee list
4. API formats and returns response
5. Test verifies response is correct

### Frontend Test Example

```python
@patch('streamlit_app.requests.post')
def test_call_api_post_success(self, mock_post):
    # 1. SETUP: Create mock HTTP response
    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_response.json.return_value = {"id": 1, "name": "John"}
    mock_post.return_value = mock_response
    
    # 2. EXECUTION: Call function
    data, error, status_code = call_api("/employee", "POST", {"name": "John"})
    
    # 3. ASSERTION: Verify results
    assert data == {"id": 1, "name": "John"}
    assert error is None
    assert status_code == 201
```

**What happens:**
1. Mock replaces `requests.post`
2. Function makes HTTP call (intercepted by mock)
3. Mock returns predefined response
4. Function processes response
5. Test verifies function returns correct data

---

## 🔍 Key Testing Concepts

### 1. **Mocking (`@patch`)**
- Replaces real functions/objects with fake ones
- Allows controlling return values
- Enables testing without external dependencies

### 2. **TestClient (FastAPI)**
- Simulates HTTP requests
- No actual server needed
- Fast and isolated

### 3. **Assertions**
- Verify expected behavior
- Check response codes, data, errors
- Fail test if assertion fails

### 4. **Fixtures (`@pytest.fixture`)**
- Setup/teardown code
- Shared test data
- Automatic cleanup

---

## 📈 Test Coverage

### What's Tested:
✅ **Backend:**
- All API endpoints (GET, POST, DELETE)
- Request validation
- Response formatting
- Error handling
- Edge cases (empty data, not found)

✅ **Frontend:**
- Data formatting functions
- API integration (all HTTP methods)
- Error handling (connection, timeout, errors)
- Data validation

### What's NOT Tested (Intentionally):
- ❌ Actual database operations (mocked)
- ❌ Real HTTP requests (mocked)
- ❌ Streamlit UI rendering (requires browser)
- ❌ End-to-end user flows

---

## 🎯 Why This Approach?

### Advantages:
1. **Fast**: No database I/O, no network calls
2. **Isolated**: Tests don't affect each other
3. **Reliable**: No external dependencies
4. **Comprehensive**: Tests all code paths
5. **Maintainable**: Easy to update when code changes

### Trade-offs:
- Doesn't test actual database integration
- Doesn't test real HTTP communication
- Requires separate integration tests for full coverage

---

## 🔄 Running Tests

### Command Used:
```bash
pytest tests/ -v
```

### What Happens:
1. Pytest discovers all tests
2. Runs each test in isolation
3. Applies mocks automatically
4. Collects results
5. Reports pass/fail status

### Output:
```
tests/test_api.py::TestEmployeeEndpoints::test_add_employee_success PASSED
tests/test_ui_logic.py::TestDataFormatting::test_format_employee_table_single PASSED
...
======================= 26 passed, 5 warnings in 11.24s =======================
```

---

## 📝 Summary

**Testing Methodology:**
1. **Unit Tests** - Test individual functions/endpoints
2. **Mocking** - Replace external dependencies (database, HTTP)
3. **Isolation** - Each test runs independently
4. **Assertions** - Verify expected behavior

**Tools:**
- pytest (test framework)
- FastAPI TestClient (API testing)
- unittest.mock (mocking)
- MagicMock (mock objects)

**Result:**
- 26 tests covering all major functionality
- Fast execution (< 12 seconds)
- No external dependencies required
- Comprehensive coverage of business logic

This approach ensures your code works correctly without needing a running database or API server!

