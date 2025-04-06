class employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.projects = []
    def update_info(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def assign_project(self, project_id):
        self.projects.append(project_id)
    def remove_project(self, project_id):
        self.projects.pop(project_id)
    def get_details(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Projects: {self.projects}"