numbers = [1,23,4,5,6,7,9]

for i in iter(numbers):
    print(i)

listd = iter(numbers)
for i in range(len(numbers)):
    x = next(listd)
    print(x)


def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

fib1 = fibonacci(20)
fib_nums = [num for num in fib1]
double_fib_nums = [num * 2 for num in fibonacci(30)] 

print(fib1)
print(fib_nums)
print(double_fib_nums)