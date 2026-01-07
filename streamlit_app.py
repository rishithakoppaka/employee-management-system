"""
Streamlit frontend for Employee Management System.
"""

import streamlit as st
import requests
from typing import Dict, Any, Optional, Tuple
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")


def call_api(endpoint: str, method: str = "GET", data: Optional[Dict] = None) -> Tuple[Optional[Dict], Optional[str], int]:
    """
    Make an API call and return response.
    
    Args:
        endpoint: API endpoint (e.g., "/employees")
        method: HTTP method (GET, POST, DELETE)
        data: Optional data for POST requests
        
    Returns:
        Tuple of (response_data, error_message, status_code)
    """
    url = f"{API_BASE_URL}{endpoint}"
    
    try:
        if method == "GET":
            response = requests.get(url, timeout=5)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=5)
        elif method == "DELETE":
            response = requests.delete(url, timeout=5)
        else:
            return None, f"Unsupported method: {method}", 400
        
        if response.status_code in [200, 201]:
            return response.json(), None, response.status_code
        else:
            return None, f"Error: {response.status_code} - {response.text}", response.status_code
            
    except requests.exceptions.ConnectionError:
        return None, "Connection error: Could not connect to API. Make sure the backend is running.", 0
    except requests.exceptions.Timeout:
        return None, "Request timeout: API took too long to respond.", 0
    except Exception as e:
        return None, f"Unexpected error: {str(e)}", 0


def format_employee_table(employees: list) -> str:
    """
    Format employee list for display in Streamlit table.
    
    Args:
        employees: List of employee dictionaries
        
    Returns:
        Formatted string representation
    """
    if not employees:
        return "No employees found."
    
    formatted = "ID | Name | Age | Salary | Department\n"
    formatted += "---|------|-----|--------|-----------\n"
    
    for emp in employees:
        formatted += f"{emp['id']} | {emp['name']} | {emp['age']} | ${emp['salary']:,.2f} | {emp['department']}\n"
    
    return formatted


# Streamlit UI
st.set_page_config(
    page_title="Employee Management System",
    page_icon="👥",
    layout="wide"
)

st.title("👥 Employee Management System")
st.markdown("---")

# Sidebar for API status
with st.sidebar:
    st.header("API Status")
    status_data, status_error, status_code = call_api("/")
    if status_error:
        st.error(f"❌ API Offline: {status_error}")
    else:
        st.success("✅ API Online")
        if status_data:
            st.info(f"Version: {status_data.get('version', 'N/A')}")

# Main content tabs
tab1, tab2, tab3, tab4 = st.tabs(["Add Employee", "View Employees", "Delete Employee", "Statistics"])

# Tab 1: Add Employee
with tab1:
    st.header("➕ Add New Employee")
    
    with st.form("add_employee_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name *", placeholder="Enter employee name")
            age = st.number_input("Age *", min_value=1, max_value=150, value=25)
        
        with col2:
            salary = st.number_input("Salary *", min_value=0.0, value=50000.0, step=1000.0)
            department = st.text_input("Department *", placeholder="Enter department")
        
        submitted = st.form_submit_button("Add Employee", type="primary")
        
        if submitted:
            if not name or not department:
                st.error("Please fill in all required fields (marked with *)")
            else:
                with st.spinner("Adding employee..."):
                    employee_data = {
                        "name": name,
                        "age": int(age),
                        "salary": float(salary),
                        "department": department
                    }
                    
                    response_data, error, status_code = call_api("/employee", "POST", employee_data)
                    
                    if error:
                        st.error(f"❌ {error}")
                    else:
                        st.success(f"✅ Employee added successfully!")
                        st.json(response_data)

# Tab 2: View Employees
with tab2:
    st.header("📋 View All Employees")
    
    if st.button("🔄 Refresh Employee List", type="primary"):
        st.rerun()
    
    st.markdown("---")
    
    with st.spinner("Loading employees..."):
        employees_data, error, status_code = call_api("/employees")
        
        if error:
            st.error(f"❌ {error}")
        elif employees_data:
            if len(employees_data) == 0:
                st.info("No employees found. Add some employees using the 'Add Employee' tab.")
            else:
                st.success(f"Found {len(employees_data)} employee(s)")
                st.markdown("### Employee List")
                
                # Display as table
                st.dataframe(
                    employees_data,
                    use_container_width=True,
                    hide_index=True
                )
                
                # Display formatted text
                with st.expander("View as formatted text"):
                    st.text(format_employee_table(employees_data))
        else:
            st.warning("No data received from API")

# Tab 3: Delete Employee
with tab3:
    st.header("🗑️ Delete Employee")
    
    # First, get list of employees for the dropdown
    employees_data, error, status_code = call_api("/employees")
    
    if error:
        st.error(f"❌ {error}")
        st.info("Cannot load employee list. Make sure the API is running.")
    else:
        if employees_data and len(employees_data) > 0:
            # Create dropdown with employee options
            employee_options = {
                f"{emp['id']} - {emp['name']} ({emp['department']})": emp['id']
                for emp in employees_data
            }
            
            selected_employee = st.selectbox(
                "Select Employee to Delete",
                options=list(employee_options.keys()),
                help="Choose an employee from the list"
            )
            
            if selected_employee:
                employee_id = employee_options[selected_employee]
                
                st.warning(f"⚠️ You are about to delete employee ID: {employee_id}")
                
                if st.button("🗑️ Delete Employee", type="primary"):
                    with st.spinner("Deleting employee..."):
                        response_data, error, status_code = call_api(f"/employee/{employee_id}", "DELETE")
                        
                        if error:
                            st.error(f"❌ {error}")
                        else:
                            st.success(f"✅ {response_data.get('message', 'Employee deleted successfully')}")
                            st.rerun()
        else:
            st.info("No employees available to delete.")

# Tab 4: Statistics
with tab4:
    st.header("📊 Employee Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Median Age")
        if st.button("🔄 Get Median Age", type="primary"):
            with st.spinner("Calculating median age..."):
                response_data, error, status_code = call_api("/stats/median-age")
                
                if error:
                    st.error(f"❌ {error}")
                elif response_data:
                    median_age = response_data.get("median_value")
                    if median_age is not None:
                        st.metric("Median Age", f"{median_age:.2f} years")
                        st.info(response_data.get("message", ""))
                    else:
                        st.warning("No employees found to calculate median age")
    
    with col2:
        st.subheader("Median Salary")
        if st.button("🔄 Get Median Salary", type="primary"):
            with st.spinner("Calculating median salary..."):
                response_data, error, status_code = call_api("/stats/median-salary")
                
                if error:
                    st.error(f"❌ {error}")
                elif response_data:
                    median_salary = response_data.get("median_value")
                    if median_salary is not None:
                        st.metric("Median Salary", f"${median_salary:,.2f}")
                        st.info(response_data.get("message", ""))
                    else:
                        st.warning("No employees found to calculate median salary")
    
    # Auto-refresh statistics
    if st.checkbox("🔄 Auto-refresh statistics", value=False):
        st.rerun()

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        Employee Management System | Built with FastAPI, PostgreSQL, and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

