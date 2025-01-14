class ReverseOrderIterator:
    def __init__(self, lst):
        self._list_of_nums = lst
        self.num = len(self._list_of_nums)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 0:
            raise StopIteration
        current_num =  self._list_of_nums[self.num]
        self.num -= 1
        return current_num

my_iterator = ReverseOrderIterator([1,2,3, 4, 5, 6])
for num in my_iterator:
    print(num)


