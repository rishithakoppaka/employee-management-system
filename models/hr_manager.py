"""
HRManager class for managing employees in the Employee Management System.
"""

from models.employee import Employee
from typing import List, Optional


class HRManager:
    """HR Manager class for handling employee operations."""
    
    def __init__(self):
        """Initialize an HRManager instance."""
        self.employees: List[Employee] = []
    
    def add_employee(self, employee: Employee) -> bool:
        """
        Add an employee to the manager's list.
        
        Args:
            employee: Employee instance to add
            
        Returns:
            True if employee was added successfully
        """
        if employee not in self.employees:
            self.employees.append(employee)
            return True
        return False
    
    def get_all_employees(self) -> List[Employee]:
        """
        Get all employees managed by this HR manager.
        
        Returns:
            List of Employee instances
        """
        return self.employees.copy()
    
    def remove_employee(self, employee_id: int) -> bool:
        """
        Remove an employee by ID.
        
        Args:
            employee_id: ID of the employee to remove
            
        Returns:
            True if employee was found and removed, False otherwise
        """
        for i, emp in enumerate(self.employees):
            if emp.employee_id == employee_id:
                del self.employees[i]
                return True
        return False
    
    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """
        Get an employee by ID.
        
        Args:
            employee_id: ID of the employee to retrieve
            
        Returns:
            Employee instance if found, None otherwise
        """
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        return None
    
    def calculate_median_age(self) -> Optional[float]:
        """
        Calculate the median age of all employees.
        
        Returns:
            Median age as float, or None if no employees
        """
        if not self.employees:
            return None
        
        ages = sorted([emp.age for emp in self.employees])
        n = len(ages)
        
        if n % 2 == 0:
            return (ages[n // 2 - 1] + ages[n // 2]) / 2.0
        else:
            return float(ages[n // 2])
    
    def calculate_median_salary(self) -> Optional[float]:
        """
        Calculate the median salary of all employees.
        
        Returns:
            Median salary as float, or None if no employees
        """
        if not self.employees:
            return None
        
        salaries = sorted([float(emp.salary) for emp in self.employees])
        n = len(salaries)
        
        if n % 2 == 0:
            return (salaries[n // 2 - 1] + salaries[n // 2]) / 2.0
        else:
            return float(salaries[n // 2])



