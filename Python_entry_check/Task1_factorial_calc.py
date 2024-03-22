def factorial_calc(num):
    if num < 2:
        return 1
    else:
        return num * factorial_calc(num-1)

n = int(input('Enter an integer number: '))
print(f'factorial({n}) is: ',factorial_calc(n))
    