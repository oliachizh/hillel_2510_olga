lst = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3', '', '1.2, 1.3']

def sum_of_list_elements(lst):
    for i in lst:
        try:
            print(sum([int(j) for j in i.split(",")]))
        except ValueError:
            print(f"Не можу це зробити")
        except Exception as e:
            print(f"Інша помилка: {e}")


sum_of_list_elements(lst)