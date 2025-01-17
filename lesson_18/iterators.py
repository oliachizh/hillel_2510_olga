import random
class MyIterator:
    list_of_greetings = ['hi', 'hello', 'nice to meet']
    def __init__(self, *args):
        self._list_of_names = args
        self.current_position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_position == len(self._list_of_names):
            raise StopIteration
        current_greet = random.choice(self.list_of_greetings)
        current_name = self._list_of_names[self.current_position]
        self.current_position +=1

        return f"{current_greet}, {current_name}"



for name in MyIterator("Ola", "kate"):
    print(name)



