"""
Employee class for the Employee Management System.
"""

from models.person import Person


class Employee(Person):
    """Employee class that extends Person with salary and department."""
    
    def __init__(self, name: str, age: int, salary: float, department: str, employee_id: int = None):
        """
        Initialize an Employee instance.
        
        Args:
            name: Full name of the employee
            age: Age of the employee
            salary: Salary of the employee
            department: Department the employee works in
            employee_id: Optional employee ID (for existing employees)
        """
        super().__init__(name, age)
        self.salary = salary
        self.department = department
        self.employee_id = employee_id
    
    def __str__(self) -> str:
        """String representation of Employee."""
        return f"Employee(id={self.employee_id}, name={self.name}, age={self.age}, salary={self.salary}, department={self.department})"
    
    def __repr__(self) -> str:
        """Official string representation of Employee."""
        return self.__str__()
    
    def get_info(self) -> dict:
        """
        Get employee information as a dictionary.
        
        Returns:
            Dictionary containing all employee attributes
        """
        info = super().get_info()
        info.update({
            "id": self.employee_id,
            "salary": float(self.salary),
            "department": self.department
        })
        return info
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Employee':
        """
        Create an Employee instance from a dictionary.
        
        Args:
            data: Dictionary containing employee data
            
        Returns:
            Employee instance
        """
        return cls(
            name=data.get("name"),
            age=data.get("age"),
            salary=data.get("salary"),
            department=data.get("department"),
            employee_id=data.get("id")
        )



