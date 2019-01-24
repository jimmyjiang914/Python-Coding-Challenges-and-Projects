def factorial(num):
    if num <= 0:
        return 1
    fact = num * int(factorial(num - 1))
    return fact

print(factorial(10))