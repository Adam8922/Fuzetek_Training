# Import necessary classes
from Department import department
from Employee import employee
from Hr_system import hr_system
from Project import project

# Initialize the HR System
hr = hr_system()

# Create employees
emp1 = employee(1, "Ali", "Software Engineer", 15000)
emp2 = employee(2, "Mona", "Data Scientist", 18000)
emp3 = employee(3, "Kareem", "Project Manager", 25000)

# Add employees to HR system
hr.add_employee(emp1)
hr.add_employee(emp2)
hr.add_employee(emp3)

# Create departments
dept1 = department(101, "Engineering")
dept2 = department(102, "Data Science")

# Add departments to HR system
hr.add_department(dept1)
hr.add_department(dept2)

# Assign managers to departments
dept1.assign_manager(emp1.emp_id)
dept2.assign_manager(emp2.emp_id)

# Add employees to departments
dept1.add_employee(emp1.emp_id)
dept1.add_employee(emp3.emp_id)
dept2.add_employee(emp2.emp_id)

# Create projects
proj1 = project(201, "AI Chatbot", 50000, "30-Apr-2025")
proj2 = project(202, "E-commerce Platform", 75000, "15-May-2025")

# Add projects to HR system
hr.add_project(proj1)
hr.add_project(proj2)

# Assign employees to projects
proj1.assign_employee(emp1.emp_id)
proj1.assign_employee(emp2.emp_id)
proj2.assign_employee(emp3.emp_id)

# Employees join projects
emp1.assign_project(proj1.project_id)
emp2.assign_project(proj1.project_id)
emp3.assign_project(proj2.project_id)

# Display details
print("\n--- Employees ---")
for employee in hr.employees:
    print(employee.get_details())
print("\n--- Departments ---")
for department in hr.departments:
    print(department.get_department_details())
print("\n--- Projects ---")
for project in hr.projects:
    print(project.get_project_details())