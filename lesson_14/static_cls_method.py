# Use static methods for logically related helper functions.
# Use class methods when you need to work with class-level data or want to implement factory patterns.

class User:
    min_age= 1
    all_users = []
    def __init__(self, name, age):
        self.name = name
        if age < self.min_age:
            raise AttributeError
        self.age = age

        self.all_users.append({'name': name})

    @staticmethod
    def print_hello():
        print("hello")

    @classmethod
    def print_min(cls):
        print(f"min age is {cls.min_age}")

    # def __del__(self):
    #     print(f"Deleting {self.name}")


den = User("den", 66)
oll = User("kk", 66)
print(den.min_age)
print(den.all_users)
del den
