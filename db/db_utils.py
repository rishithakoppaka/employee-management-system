"""
Database utilities for Employee Management System using raw SQL with psycopg2.
"""

import psycopg2
import os
from typing import List, Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_db_connection():
    """
    Create and return a database connection.
    
    Returns:
        psycopg2 connection object
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME", "employee_db"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "")
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise


def init_database():
    """
    Initialize the database by creating the employees table if it doesn't exist.
    """
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Create employees table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INTEGER NOT NULL,
            salary DECIMAL(10, 2) NOT NULL,
            department VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        print("Database initialized successfully")
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        print(f"Error initializing database: {e}")
        raise
    finally:
        if conn:
            conn.close()


def add_employee(name: str, age: int, salary: float, department: str) -> Dict[str, Any]:
    """
    Add a new employee to the database.
    
    Args:
        name: Employee name
        age: Employee age
        salary: Employee salary
        department: Employee department
        
    Returns:
        Dictionary with employee data including the generated ID
    """
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        insert_query = """
        INSERT INTO employees (name, age, salary, department)
        VALUES (%s, %s, %s, %s)
        RETURNING id, name, age, salary, department;
        """
        
        cursor.execute(insert_query, (name, age, salary, department))
        result = cursor.fetchone()
        conn.commit()
        
        employee_data = {
            "id": result[0],
            "name": result[1],
            "age": result[2],
            "salary": float(result[3]),
            "department": result[4]
        }
        
        cursor.close()
        return employee_data
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        print(f"Error adding employee: {e}")
        raise
    finally:
        if conn:
            conn.close()


def get_all_employees() -> List[Dict[str, Any]]:
    """
    Retrieve all employees from the database.
    
    Returns:
        List of dictionaries containing employee data
    """
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        select_query = """
        SELECT id, name, age, salary, department
        FROM employees
        ORDER BY id;
        """
        
        cursor.execute(select_query)
        results = cursor.fetchall()
        
        employees = []
        for row in results:
            employees.append({
                "id": row[0],
                "name": row[1],
                "age": row[2],
                "salary": float(row[3]),
                "department": row[4]
            })
        
        cursor.close()
        return employees
    except psycopg2.Error as e:
        print(f"Error retrieving employees: {e}")
        raise
    finally:
        if conn:
            conn.close()


def delete_employee_by_id(employee_id: int) -> bool:
    """
    Delete an employee by ID.
    
    Args:
        employee_id: ID of the employee to delete
        
    Returns:
        True if employee was deleted, False if not found
    """
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        delete_query = """
        DELETE FROM employees
        WHERE id = %s;
        """
        
        cursor.execute(delete_query, (employee_id,))
        rows_deleted = cursor.rowcount
        conn.commit()
        
        cursor.close()
        return rows_deleted > 0
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        print(f"Error deleting employee: {e}")
        raise
    finally:
        if conn:
            conn.close()


def get_median_age() -> Optional[float]:
    """
    Calculate the median age of all employees using SQL.
    
    Returns:
        Median age as float, or None if no employees exist
    """
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Use PostgreSQL's percentile_cont function for median
        median_query = """
        SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY age) AS median_age
        FROM employees;
        """
        
        cursor.execute(median_query)
        result = cursor.fetchone()
        
        cursor.close()
        
        if result and result[0] is not None:
            return float(result[0])
        return None
    except psycopg2.Error as e:
        print(f"Error calculating median age: {e}")
        raise
    finally:
        if conn:
            conn.close()


def get_median_salary() -> Optional[float]:
    """
    Calculate the median salary of all employees using SQL.
    
    Returns:
        Median salary as float, or None if no employees exist
    """
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Use PostgreSQL's percentile_cont function for median
        median_query = """
        SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary
        FROM employees;
        """
        
        cursor.execute(median_query)
        result = cursor.fetchone()
        
        cursor.close()
        
        if result and result[0] is not None:
            return float(result[0])
        return None
    except psycopg2.Error as e:
        print(f"Error calculating median salary: {e}")
        raise
    finally:
        if conn:
            conn.close()


