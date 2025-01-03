class EvenNumIterator:
    def __init__(self, limit):
        self.limit = limit
        self.start = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.limit:
            raise StopIteration
        current_num =  self.start
        self.start += 2
        return current_num

my_iterator = EvenNumIterator(10)
for num in my_iterator:
    print(num)