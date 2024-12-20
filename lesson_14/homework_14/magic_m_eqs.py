res_from_api = {'name': 'Apple', 'empl': 3000}
res_from_db = {'c_name': 'Apple', 'c_employee': 3000}

class UserAPI:
    def __init__(self, name, empl):
        self.name = name
        self.empl = empl

    def __eq__(self, other):
        if self.name ==other.c_name:
            return True
        if self.empl ==other.c_employee:
            return True
        return False


class UserDB:
    def __init__(self, c_name, c_employee):
        self.c_name = c_name
        self.c_employee = c_employee

def compare(user_api, user_db):
    print(user_api == user_db)


user_api = UserAPI(**res_from_api)
user_db = UserDB(**res_from_db)

compare(user_api, user_db)

"""__eq__"""

#The __eq__ method in Python is a special (or "magic") method
# used to define how two objects are compared for equality
# using the == operator. By default, the == operator compares
# object references, meaning two objects are only considered
# equal if they are the same instance in memory.

#The __eq__ method allows you to override this behavior and define
# a custom logic for equality based on the attributes of the objects.

"""
__gte__>=
__gt__ >
__lte__ <=
__lt__ <
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

# Create instances
person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
person3 = Person("Bob", 25)

# Compare objects
print(person1 == person2)  # Output: True
print(person1 == person3)  # Output: False

# Compare instances
print(person1 != person2)  # Output: False (because they are equal)
print(person1 != person3)  # Output: True (because they are not equal)

