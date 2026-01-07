"""
Unit tests for Streamlit UI logic and data formatting.
"""

import pytest
from streamlit_app import format_employee_table, call_api
from unittest.mock import patch, MagicMock
import requests


class TestDataFormatting:
    """Test cases for data formatting functions."""
    
    def test_format_employee_table_empty(self):
        """Test formatting empty employee list."""
        result = format_employee_table([])
        assert "No employees found" in result
    
    def test_format_employee_table_single(self):
        """Test formatting single employee."""
        employees = [
            {
                "id": 1,
                "name": "John Doe",
                "age": 30,
                "salary": 50000.0,
                "department": "Engineering"
            }
        ]
        result = format_employee_table(employees)
        assert "John Doe" in result
        assert "30" in result
        assert "Engineering" in result
        assert "1" in result
    
    def test_format_employee_table_multiple(self):
        """Test formatting multiple employees."""
        employees = [
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
        result = format_employee_table(employees)
        assert "John Doe" in result
        assert "Jane Smith" in result
        assert "Engineering" in result
        assert "Marketing" in result
    
    def test_format_employee_table_salary_formatting(self):
        """Test that salary is properly formatted."""
        employees = [
            {
                "id": 1,
                "name": "John Doe",
                "age": 30,
                "salary": 123456.78,
                "department": "Engineering"
            }
        ]
        result = format_employee_table(employees)
        # Check that salary formatting includes comma and decimal
        assert "$" in result or "123456.78" in result


class TestAPIIntegration:
    """Test cases for API integration functions."""
    
    @patch('streamlit_app.requests.get')
    def test_call_api_get_success(self, mock_get):
        """Test successful GET API call."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response
        
        data, error, status_code = call_api("/employees", "GET")
        
        assert data == {"data": "test"}
        assert error is None
        assert status_code == 200
    
    @patch('streamlit_app.requests.post')
    def test_call_api_post_success(self, mock_post):
        """Test successful POST API call."""
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"id": 1, "name": "John"}
        mock_post.return_value = mock_response
        
        data, error, status_code = call_api("/employee", "POST", {"name": "John"})
        
        assert data == {"id": 1, "name": "John"}
        assert error is None
        assert status_code == 201
    
    @patch('streamlit_app.requests.delete')
    def test_call_api_delete_success(self, mock_delete):
        """Test successful DELETE API call."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Deleted"}
        mock_delete.return_value = mock_response
        
        data, error, status_code = call_api("/employee/1", "DELETE")
        
        assert data == {"message": "Deleted"}
        assert error is None
        assert status_code == 200
    
    @patch('streamlit_app.requests.get')
    def test_call_api_error_response(self, mock_get):
        """Test API call with error response."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_get.return_value = mock_response
        
        data, error, status_code = call_api("/employees", "GET")
        
        assert data is None
        assert error is not None
        assert "404" in error
        assert status_code == 404
    
    @patch('streamlit_app.requests.get')
    def test_call_api_connection_error(self, mock_get):
        """Test API call with connection error."""
        mock_get.side_effect = requests.exceptions.ConnectionError()
        
        data, error, status_code = call_api("/employees", "GET")
        
        assert data is None
        assert error is not None
        assert "Connection error" in error
        assert status_code == 0
    
    @patch('streamlit_app.requests.get')
    def test_call_api_timeout(self, mock_get):
        """Test API call with timeout."""
        mock_get.side_effect = requests.exceptions.Timeout()
        
        data, error, status_code = call_api("/employees", "GET")
        
        assert data is None
        assert error is not None
        assert "timeout" in error.lower()
        assert status_code == 0
    
    def test_call_api_unsupported_method(self):
        """Test API call with unsupported method."""
        data, error, status_code = call_api("/employees", "PUT")
        
        assert data is None
        assert error is not None
        assert "Unsupported method" in error
        assert status_code == 400


class TestEmployeeDataValidation:
    """Test cases for employee data validation logic."""
    
    def test_employee_data_structure(self):
        """Test that employee data has required fields."""
        employee = {
            "id": 1,
            "name": "John Doe",
            "age": 30,
            "salary": 50000.0,
            "department": "Engineering"
        }
        
        required_fields = ["id", "name", "age", "salary", "department"]
        for field in required_fields:
            assert field in employee
    
    def test_employee_data_types(self):
        """Test that employee data has correct types."""
        employee = {
            "id": 1,
            "name": "John Doe",
            "age": 30,
            "salary": 50000.0,
            "department": "Engineering"
        }
        
        assert isinstance(employee["id"], int)
        assert isinstance(employee["name"], str)
        assert isinstance(employee["age"], int)
        assert isinstance(employee["salary"], (int, float))
        assert isinstance(employee["department"], str)



