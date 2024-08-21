import streamlit as st
import pandas as pd

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []
        self.selected_employee = None

    def display_selected_employee(self):
        if self.selected_employee:
            st.write("### Selected Employee Details")
            st.write(f"**Name:** {self.selected_employee.get('name', '')}")
            st.write(f"**Position:** {self.selected_employee.get('position', '')}")
            st.write(f"**ID:** {self.selected_employee.get('id', '')}")
            st.write(f"**Address:** {self.selected_employee.get('address', '')}")
            st.write(f"**Department:** {self.selected_employee.get('department', '')}")

    def add_employee(self, name, position, employee_id, address, department):
        if name and position and employee_id and address and department:
            employee = {'name': name, 'position': position, 'id': employee_id, 'address': address, 'department': department}
            self.employees.append(employee)
            st.success("Employee added successfully!")
        else:
            st.warning("Please enter all details.")

    def update_employee(self, name, position, employee_id, address, department):
        if self.selected_employee:
            if name and position and employee_id and address and department:
                self.selected_employee['name'] = name
                self.selected_employee['position'] = position
                self.selected_employee['id'] = employee_id
                self.selected_employee['address'] = address
                self.selected_employee['department'] = department
                st.success("Employee updated successfully!")
            else:
                st.warning("Please enter all details.")
        else:
            st.warning("Select an employee to update.")

    def delete_employee(self):
        if self.selected_employee:
            self.employees.remove(self.selected_employee)
            self.selected_employee = None
            st.success("Employee deleted successfully!")
        else:
            st.warning("Select an employee to delete.")

    def search_employee(self, query):
        if query:
            matching_employees = [employee for employee in self.employees if query.lower() in str(employee).lower()]
            self.display_search_results(matching_employees)
        else:
            self.display_all_employees()

    def display_search_results(self, results):
        st.write("### Search Results")
        for employee in results:
            st.write(f"{employee.get('name', '')} | {employee.get('position', '')} | {employee.get('id', '')} | "
                     f"{employee.get('address', '')} | {employee.get('department', '')}")

    def display_all_employees(self):
        st.write("### All Employees")
        for employee in self.employees:
            st.write(f"{employee.get('name', '')} | {employee.get('position', '')} | {employee.get('id', '')} | "
                     f"{employee.get('address', '')} | {employee.get('department', '')}")

if __name__ == "__main__":
    st.title("Employee Management System")

    app = EmployeeManagementSystem()

    # Sidebar
    st.sidebar.header("Actions")
    action = st.sidebar.radio("Select Action", ["Add Employee", "Update Employee", "Delete Employee", "Search Employees"])

    if action == "Add Employee":
        st.sidebar.header("Add Employee")
        name = st.text_input("Name:")
        position = st.text_input("Position:")
        employee_id = st.text_input("ID:")
        address = st.text_input("Address:")
        department = st.text_input("Department:")

        if st.button("Add"):
            app.add_employee(name, position, employee_id, address, department)

    elif action == "Update Employee":
        st.sidebar.header("Update Employee")
        app.display_all_employees()
        selected_index = st.number_input("Select the index of the employee to update:", min_value=0, max_value=len(app.employees)-1, value=0, step=1)

        if st.button("Update"):
            app.selected_employee = app.employees[int(selected_index)]
            name = st.text_input("Name:", app.selected_employee.get('name', ''))
            position = st.text_input("Position:", app.selected_employee.get('position', ''))
            employee_id = st.text_input("ID:", app.selected_employee.get('id', ''))
            address = st.text_input("Address:", app.selected_employee.get('address', ''))
            department = st.text_input("Department:", app.selected_employee.get('department', ''))

            app.update_employee(name, position, employee_id, address, department)

    elif action == "Delete Employee":
        st.sidebar.header("Delete Employee")
        app.display_all_employees()
        if st.button("Delete"):
            app.delete_employee()

    elif action == "Search Employees":
        st.sidebar.header("Search Employees")
        query = st.text_input("Enter search query:")
        if st.button("Search"):
            app.search_employee(query)
    
    app.display_selected_employee()
