class Student:
    def __init__(self, name, surname, age, average_mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_mark = average_mark

    def get_info(self):
        return f"Student: {self.name} {self.surname} is {self.age} with average mark - {self.average_mark}"

    def change_average_mark(self, mark):
        self.average_mark = mark

student_1 = Student("Olga", "Test", 33, 55)
print(student_1.get_info())
student_1.change_average_mark(66)
print(student_1.average_mark)