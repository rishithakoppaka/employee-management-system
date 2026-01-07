"""
Person base class for the Employee Management System.
"""


class Person:
    """Base class representing a person with basic attributes."""
    
    def __init__(self, name: str, age: int):
        """
        Initialize a Person instance.
        
        Args:
            name: Full name of the person
            age: Age of the person
        """
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        """String representation of Person."""
        return f"Person(name={self.name}, age={self.age})"
    
    def __repr__(self) -> str:
        """Official string representation of Person."""
        return self.__str__()
    
    def get_info(self) -> dict:
        """
        Get person information as a dictionary.
        
        Returns:
            Dictionary containing person's name and age
        """
        return {
            "name": self.name,
            "age": self.age
        }



