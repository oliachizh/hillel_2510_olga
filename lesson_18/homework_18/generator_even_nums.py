def generate_even_nums(limit):
    for n in range(limit):
        if n %2 == 0:
            yield n

gen = generate_even_nums(5)
for num in gen:
    print(num)



