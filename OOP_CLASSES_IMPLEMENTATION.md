# OOP Classes Implementation - Person, Employee, HRManager

## ✅ Confirmation: All Three Classes Defined Using Python OOP

This project implements **Person**, **Employee**, and **HRManager** classes using proper **Object-Oriented Programming** principles.

---

## 📋 Class Hierarchy

```
Person (Base Class)
    │
    └── Employee (Inherits from Person)
         │
         └── Used by HRManager (Composition)
```

---

## 1. Person Class (Base Class)

**Location:** `models/person.py`

### Class Definition:
```python
class Person:
    """Base class representing a person with basic attributes."""
    
    def __init__(self, name: str, age: int):
        """Initialize a Person instance."""
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        """String representation of Person."""
        return f"Person(name={self.name}, age={self.age})"
    
    def __repr__(self) -> str:
        """Official string representation of Person."""
        return self.__str__()
    
    def get_info(self) -> dict:
        """Get person information as a dictionary."""
        return {
            "name": self.name,
            "age": self.age
        }
```

### OOP Features:
- ✅ **Encapsulation**: Attributes (`name`, `age`) are instance variables
- ✅ **Methods**: `get_info()` method for data retrieval
- ✅ **Magic Methods**: `__str__()` and `__repr__()` for string representation
- ✅ **Type Hints**: Proper type annotations

### Attributes:
- `name` (str): Person's full name
- `age` (int): Person's age

### Methods:
- `__init__(name, age)`: Constructor
- `__str__()`: String representation
- `__repr__()`: Official representation
- `get_info()`: Returns person data as dictionary

---

## 2. Employee Class (Inherits from Person)

**Location:** `models/employee.py`

### Class Definition:
```python
from models.person import Person

class Employee(Person):
    """Employee class that extends Person with salary and department."""
    
    def __init__(self, name: str, age: int, salary: float, department: str, employee_id: int = None):
        """Initialize an Employee instance."""
        super().__init__(name, age)  # Call parent constructor
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
        """Get employee information as a dictionary."""
        info = super().get_info()  # Call parent method
        info.update({
            "id": self.employee_id,
            "salary": float(self.salary),
            "department": self.department
        })
        return info
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Employee':
        """Create an Employee instance from a dictionary."""
        return cls(
            name=data.get("name"),
            age=data.get("age"),
            salary=data.get("salary"),
            department=data.get("department"),
            employee_id=data.get("id")
        )
```

### OOP Features:
- ✅ **Inheritance**: Inherits from `Person` class
- ✅ **Method Overriding**: Overrides `get_info()` and `__str__()` methods
- ✅ **Super()**: Uses `super().__init__()` to call parent constructor
- ✅ **Class Method**: `from_dict()` is a class method (alternative constructor)
- ✅ **Polymorphism**: Can be used wherever Person is expected

### Attributes:
- Inherited from Person:
  - `name` (str)
  - `age` (int)
- Additional:
  - `salary` (float): Employee's salary
  - `department` (str): Employee's department
  - `employee_id` (int, optional): Employee's ID

### Methods:
- `__init__(name, age, salary, department, employee_id)`: Constructor
- `__str__()`: Overridden string representation
- `__repr__()`: Overridden official representation
- `get_info()`: Overridden method (extends parent's method)
- `from_dict(data)`: Class method to create Employee from dictionary

---

## 3. HRManager Class (Composition with Employee)

**Location:** `models/hr_manager.py`

### Class Definition:
```python
from models.employee import Employee
from typing import List, Optional

class HRManager:
    """HR Manager class for handling employee operations."""
    
    def __init__(self):
        """Initialize an HRManager instance."""
        self.employees: List[Employee] = []  # Composition: contains Employee objects
    
    def add_employee(self, employee: Employee) -> bool:
        """Add an employee to the manager's list."""
        if employee not in self.employees:
            self.employees.append(employee)
            return True
        return False
    
    def get_all_employees(self) -> List[Employee]:
        """Get all employees managed by this HR manager."""
        return self.employees.copy()
    
    def remove_employee(self, employee_id: int) -> bool:
        """Remove an employee by ID."""
        for i, emp in enumerate(self.employees):
            if emp.employee_id == employee_id:
                del self.employees[i]
                return True
        return False
    
    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """Get an employee by ID."""
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        return None
    
    def calculate_median_age(self) -> Optional[float]:
        """Calculate the median age of all employees."""
        if not self.employees:
            return None
        
        ages = sorted([emp.age for emp in self.employees])
        n = len(ages)
        
        if n % 2 == 0:
            return (ages[n // 2 - 1] + ages[n // 2]) / 2.0
        else:
            return float(ages[n // 2])
    
    def calculate_median_salary(self) -> Optional[float]:
        """Calculate the median salary of all employees."""
        if not self.employees:
            return None
        
        salaries = sorted([float(emp.salary) for emp in self.employees])
        n = len(salaries)
        
        if n % 2 == 0:
            return (salaries[n // 2 - 1] + salaries[n // 2]) / 2.0
        else:
            return float(salaries[n // 2])
```

### OOP Features:
- ✅ **Composition**: Contains a list of `Employee` objects
- ✅ **Encapsulation**: Manages employee list internally
- ✅ **Type Hints**: Uses `List[Employee]` and `Optional[Employee]`
- ✅ **Business Logic**: Contains methods for employee management
- ✅ **Data Processing**: Calculates statistics (median age/salary)

### Attributes:
- `employees` (List[Employee]): List of Employee instances

### Methods:
- `__init__()`: Constructor (initializes empty list)
- `add_employee(employee)`: Add employee to list
- `get_all_employees()`: Get all employees
- `remove_employee(employee_id)`: Remove employee by ID
- `get_employee_by_id(employee_id)`: Get employee by ID
- `calculate_median_age()`: Calculate median age
- `calculate_median_salary()`: Calculate median salary

---

## 🎯 OOP Principles Demonstrated

### 1. **Inheritance**
```python
class Employee(Person):  # Employee inherits from Person
    def __init__(self, ...):
        super().__init__(name, age)  # Call parent constructor
```

### 2. **Encapsulation**
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Encapsulated attributes
        self.age = age
```

### 3. **Polymorphism**
```python
# Employee can be used as Person
person: Person = Employee("John", 30, 50000, "Engineering")
person.get_info()  # Calls Employee's overridden method
```

### 4. **Composition**
```python
class HRManager:
    def __init__(self):
        self.employees: List[Employee] = []  # Contains Employee objects
```

### 5. **Method Overriding**
```python
class Employee(Person):
    def get_info(self) -> dict:
        info = super().get_info()  # Call parent method
        info.update({...})  # Extend with employee-specific data
        return info
```

### 6. **Class Methods**
```python
@classmethod
def from_dict(cls, data: dict) -> 'Employee':
    """Alternative constructor."""
    return cls(...)
```

---

## 📊 Class Relationships

```
┌─────────────┐
│   Person    │  (Base Class)
│  - name     │
│  - age      │
│  + get_info()│
└──────┬──────┘
       │
       │ inherits
       │
┌──────▼──────┐
│  Employee   │  (Derived Class)
│  - salary   │
│  - dept     │
│  - id       │
│  + get_info()│ (overridden)
└──────┬──────┘
       │
       │ used by (composition)
       │
┌──────▼──────┐
│ HRManager   │
│ - employees │ (List[Employee])
│ + add()     │
│ + remove()  │
│ + calc()    │
└─────────────┘
```

---

## 💡 Usage Examples

### Creating Person:
```python
person = Person("John Doe", 30)
print(person.get_info())  # {'name': 'John Doe', 'age': 30}
```

### Creating Employee (Inherits from Person):
```python
employee = Employee("Jane Smith", 25, 60000.0, "Marketing", employee_id=1)
print(employee.get_info())  # Includes all Person + Employee attributes

# Using class method
employee2 = Employee.from_dict({
    "id": 2,
    "name": "Bob Johnson",
    "age": 35,
    "salary": 70000.0,
    "department": "Sales"
})
```

### Using HRManager (Composition):
```python
hr_manager = HRManager()

# Add employees
hr_manager.add_employee(employee)
hr_manager.add_employee(employee2)

# Get all employees
all_employees = hr_manager.get_all_employees()

# Calculate statistics
median_age = hr_manager.calculate_median_age()
median_salary = hr_manager.calculate_median_salary()
```

---

## ✅ Requirements Checklist

| Requirement | Status | Implementation |
|------------|--------|----------------|
| Define Person class | ✅ | `models/person.py` |
| Define Employee class | ✅ | `models/employee.py` |
| Define HRManager class | ✅ | `models/hr_manager.py` |
| Use Python OOP | ✅ | Classes with inheritance, encapsulation |
| Inheritance | ✅ | Employee inherits from Person |
| Encapsulation | ✅ | Attributes and methods in classes |
| Method Overriding | ✅ | Employee overrides Person methods |
| Type Hints | ✅ | All methods have type annotations |

---

## 📁 File Structure

```
models/
├── __init__.py
├── person.py       # Person class (base class)
├── employee.py     # Employee class (inherits Person)
└── hr_manager.py   # HRManager class (uses Employee)
```

---

## 🎓 Summary

**All three classes are properly defined using Python OOP:**

1. ✅ **Person** - Base class with name and age
2. ✅ **Employee** - Inherits from Person, adds salary and department
3. ✅ **HRManager** - Manages Employee objects using composition

**OOP Principles Used:**
- ✅ Inheritance (Employee → Person)
- ✅ Encapsulation (attributes and methods)
- ✅ Polymorphism (method overriding)
- ✅ Composition (HRManager contains Employees)
- ✅ Type hints (proper annotations)

The implementation follows Python OOP best practices! 🎯

