class Student:
    def __init__(self, name, math_score=None, lit_score=None):
        self.name = name
        self.math_score = math_score
        self.lit_score = lit_score

    def __str__(self):
        return f"my name is {self.name}"

    def __repr__(self):
        return f"Person {self.name}"

alex = Student("Alex", 33, 55)
ola = Student("Ola", 33, 55)

[print(user) for user in [alex, ola]]
print(str(ola))
print(repr(ola))

"""__str__"""
#The primary purpose of the __str__ method
# is to provide a meaningful, easy-to-read
# description of the object that would make
# sense to end users.

"""__repr__"""
#Purpose of __repr__
# Used for debugging and logging.
# Meant for developers rather than end users.
# Should provide an unambiguous representation of the object.

class Courses:
    def __init__(self, name, duration = None):
        self.name = name
        self.students = []
        self.duration = duration if duration else 6
        self.current_dur = 0

    def skip_1_month(self):
        if self.current_dur+1 <=self.duration:
            self.current_dur +=1

    def __len__(self):
        return self.duration - self.current_dur
m = Courses("m", 3)
m.skip_1_month()
m.skip_1_month()
m.skip_1_month()
m.skip_1_month()
print(m.current_dur)
print(len(m))