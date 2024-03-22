mapper = list(map(chr, range(65, 91)))

def old_phone(num):
    if len(set(num)) != 1 or 0 <= len(num) > 3:
        return print('Incorrect string!')
    digit = int(num[0])
    idx = (digit - 1) * 3 + digit%len(num)
    return print(mapper[idx])

old_phone('34')
old_phone('2')
old_phone('555')
old_phone('')
old_phone('8')
old_phone('999')
old_phone('0')