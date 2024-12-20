class User:
    def __init__(self, name, math_score):
        self.name = name #min 3, max 20
        self.math_score = math_score #min 1, max 100

    def __setattr__(self, key, value):
        if key == 'name':
            if len(value) < 3 or len(value) >20:
                raise AttributeError('Name shuldb be...')
        elif key == 'math_score':
            if value < 1 or value > 100:
                raise AttributeError('math scoe shouldnt be ..')

        super().__setattr__(key, value)

    def __getattribute__(self, item):
        return f"You get the {item} with value {super().__getattribute__(item)}"


alex = User('ook', 11)

# alex.math_score = 700
print(alex.math_score)
print(alex.name)