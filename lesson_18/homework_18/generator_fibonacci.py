def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

gen = fibonacci_generator(10)
for i in gen:
    print(i)

