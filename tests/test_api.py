"""
Unit tests for FastAPI backend endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from main import app
import db.db_utils as db_utils
from unittest.mock import patch, MagicMock

# Create test client
client = TestClient(app)


class TestEmployeeEndpoints:
    """Test cases for employee CRUD endpoints."""
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup before each test method."""
        # Mock database functions
        pass
    
    def test_root_endpoint(self):
        """Test root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
    
    @patch('db.db_utils.add_employee')
    def test_add_employee_success(self, mock_add_employee):
        """Test adding an employee successfully."""
        mock_add_employee.return_value = {
            "id": 1,
            "name": "John Doe",
            "age": 30,
            "salary": 50000.0,
            "department": "Engineering"
        }
        
        employee_data = {
            "name": "John Doe",
            "age": 30,
            "salary": 50000.0,
            "department": "Engineering"
        }
        
        response = client.post("/employee", json=employee_data)
        assert response.status_code == 201
        data = response.json()
        assert data["id"] == 1
        assert data["name"] == "John Doe"
        assert data["age"] == 30
        assert data["salary"] == 50000.0
        assert data["department"] == "Engineering"
    
    def test_add_employee_validation_error(self):
        """Test adding employee with invalid data."""
        invalid_data = {
            "name": "",  # Empty name should fail
            "age": -5,  # Negative age should fail
            "salary": -1000,  # Negative salary should fail
            "department": ""
        }
        
        response = client.post("/employee", json=invalid_data)
        assert response.status_code == 422  # Validation error
    
    @patch('db.db_utils.get_all_employees')
    def test_get_all_employees_success(self, mock_get_all):
        """Test retrieving all employees."""
        mock_get_all.return_value = [
            {
                "id": 1,
                "name": "John Doe",
                "age": 30,
                "salary": 50000.0,
                "department": "Engineering"
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "age": 25,
                "salary": 60000.0,
                "department": "Marketing"
            }
        ]
        
        response = client.get("/employees")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        assert data[0]["name"] == "John Doe"
        assert data[1]["name"] == "Jane Smith"
    
    @patch('db.db_utils.get_all_employees')
    def test_get_all_employees_empty(self, mock_get_all):
        """Test retrieving employees when none exist."""
        mock_get_all.return_value = []
        
        response = client.get("/employees")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 0
        assert isinstance(data, list)
    
    @patch('db.db_utils.delete_employee_by_id')
    def test_delete_employee_success(self, mock_delete):
        """Test deleting an employee successfully."""
        mock_delete.return_value = True
        
        response = client.delete("/employee/1")
        assert response.status_code == 200
        data = response.json()
        assert data["deleted"] is True
        assert "successfully" in data["message"].lower()
    
    @patch('db.db_utils.delete_employee_by_id')
    def test_delete_employee_not_found(self, mock_delete):
        """Test deleting a non-existent employee."""
        mock_delete.return_value = False
        
        response = client.delete("/employee/999")
        assert response.status_code == 404
        data = response.json()
        assert "not found" in data["detail"].lower()


class TestStatisticsEndpoints:
    """Test cases for statistics endpoints."""
    
    @patch('db.db_utils.get_median_age')
    def test_get_median_age_success(self, mock_median_age):
        """Test getting median age successfully."""
        mock_median_age.return_value = 32.5
        
        response = client.get("/stats/median-age")
        assert response.status_code == 200
        data = response.json()
        assert data["median_value"] == 32.5
        assert "median age" in data["message"].lower()
    
    @patch('db.db_utils.get_median_age')
    def test_get_median_age_no_employees(self, mock_median_age):
        """Test getting median age when no employees exist."""
        mock_median_age.return_value = None
        
        response = client.get("/stats/median-age")
        assert response.status_code == 200
        data = response.json()
        assert data["median_value"] is None
        assert "no employees" in data["message"].lower()
    
    @patch('db.db_utils.get_median_salary')
    def test_get_median_salary_success(self, mock_median_salary):
        """Test getting median salary successfully."""
        mock_median_salary.return_value = 55000.0
        
        response = client.get("/stats/median-salary")
        assert response.status_code == 200
        data = response.json()
        assert data["median_value"] == 55000.0
        assert "median salary" in data["message"].lower()
    
    @patch('db.db_utils.get_median_salary')
    def test_get_median_salary_no_employees(self, mock_median_salary):
        """Test getting median salary when no employees exist."""
        mock_median_salary.return_value = None
        
        response = client.get("/stats/median-salary")
        assert response.status_code == 200
        data = response.json()
        assert data["median_value"] is None
        assert "no employees" in data["message"].lower()


class TestErrorHandling:
    """Test cases for error handling."""
    
    @patch('db.db_utils.add_employee')
    def test_add_employee_database_error(self, mock_add_employee):
        """Test handling database errors when adding employee."""
        mock_add_employee.side_effect = Exception("Database connection failed")
        
        employee_data = {
            "name": "John Doe",
            "age": 30,
            "salary": 50000.0,
            "department": "Engineering"
        }
        
        response = client.post("/employee", json=employee_data)
        assert response.status_code == 500
        data = response.json()
        assert "error" in data["detail"].lower()
    
    @patch('db.db_utils.get_all_employees')
    def test_get_employees_database_error(self, mock_get_all):
        """Test handling database errors when retrieving employees."""
        mock_get_all.side_effect = Exception("Database query failed")
        
        response = client.get("/employees")
        assert response.status_code == 500
        data = response.json()
        assert "error" in data["detail"].lower()



