"""
FastAPI backend for Employee Management System.
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import db.db_utils as db_utils

# Initialize FastAPI app
app = FastAPI(
    title="Employee Management API",
    description="RESTful API for managing employees",
    version="1.0.0"
)

# Enable CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for request/response validation
class EmployeeCreate(BaseModel):
    """Model for creating a new employee."""
    name: str = Field(..., min_length=1, max_length=255, description="Employee name")
    age: int = Field(..., gt=0, le=150, description="Employee age")
    salary: float = Field(..., gt=0, description="Employee salary")
    department: str = Field(..., min_length=1, max_length=100, description="Employee department")


class EmployeeResponse(BaseModel):
    """Model for employee response."""
    id: int
    name: str
    age: int
    salary: float
    department: str


class StatsResponse(BaseModel):
    """Model for statistics response."""
    median_value: Optional[float] = None
    message: str


# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    """Initialize database on application startup."""
    try:
        db_utils.init_database()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Error initializing database: {e}")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Employee Management API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.post("/employee", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
async def add_employee(employee: EmployeeCreate):
    """
    Add a new employee to the database.
    
    Args:
        employee: Employee data to create
        
    Returns:
        Created employee with generated ID
    """
    try:
        employee_data = db_utils.add_employee(
            name=employee.name,
            age=employee.age,
            salary=employee.salary,
            department=employee.department
        )
        return EmployeeResponse(**employee_data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error adding employee: {str(e)}"
        )


@app.get("/employees", response_model=List[EmployeeResponse])
async def get_all_employees():
    """
    Get all employees from the database.
    
    Returns:
        List of all employees
    """
    try:
        employees = db_utils.get_all_employees()
        return [EmployeeResponse(**emp) for emp in employees]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving employees: {str(e)}"
        )


@app.delete("/employee/{employee_id}", status_code=status.HTTP_200_OK)
async def delete_employee(employee_id: int):
    """
    Delete an employee by ID.
    
    Args:
        employee_id: ID of the employee to delete
        
    Returns:
        Success message
    """
    try:
        deleted = db_utils.delete_employee_by_id(employee_id)
        if deleted:
            return {
                "message": f"Employee with ID {employee_id} deleted successfully",
                "deleted": True
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with ID {employee_id} not found"
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting employee: {str(e)}"
        )


@app.get("/stats/median-age", response_model=StatsResponse)
async def get_median_age():
    """
    Get the median age of all employees.
    
    Returns:
        Median age value
    """
    try:
        median_age = db_utils.get_median_age()
        if median_age is not None:
            return StatsResponse(
                median_value=median_age,
                message=f"Median age: {median_age:.2f}"
            )
        else:
            return StatsResponse(
                median_value=None,
                message="No employees found to calculate median age"
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error calculating median age: {str(e)}"
        )


@app.get("/stats/median-salary", response_model=StatsResponse)
async def get_median_salary():
    """
    Get the median salary of all employees.
    
    Returns:
        Median salary value
    """
    try:
        median_salary = db_utils.get_median_salary()
        if median_salary is not None:
            return StatsResponse(
                median_value=median_salary,
                message=f"Median salary: ${median_salary:,.2f}"
            )
        else:
            return StatsResponse(
                median_value=None,
                message="No employees found to calculate median salary"
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error calculating median salary: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



