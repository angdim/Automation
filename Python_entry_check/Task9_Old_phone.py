# mapper = list(map(chr, range(65, 91)))
# mapper.append('#')

def old_phone(num):
    if len(set(num)) != 1 or 0 <= len(num) > 3:
        return print('Incorrect string!')
    digit = int(num[0])
    idx = (digit - 1) * 3 + len(num) - 1
    return print(chr(65+idx))

old_phone('34')
old_phone('2')
old_phone('555')
old_phone('')
old_phone('9')
old_phone('99')
old_phone('999')