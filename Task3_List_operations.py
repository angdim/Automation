evens = [x for x in range(1, 21) if x%2 == 0]
no_5s = [y for y in evens if not y%5 == 0]
print('Original list: ', end='')
print(*evens, sep=', ')
print('Modified list: ', end='')
print(*no_5s, sep=', ')