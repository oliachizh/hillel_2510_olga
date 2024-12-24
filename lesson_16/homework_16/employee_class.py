class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Developer, Manager):
    def __init__(self, name, salary, department, programming_language, team_size):
        Developer.__init__(self, name, salary, programming_language)
        Manager.__init__(self, name, salary, department)
        self.team_size = team_size



test_lead = TeamLead("hh", '66', 'department', 'py',9)
print(type(test_lead).mro())