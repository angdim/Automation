import re

def phone_matcher(phone):
    m = r'(\+\d{3}\s|0)(\d{9})'
    if re.fullmatch(m, phone):
        print(f'Valid phone number!: {phone}')
    else:
        print(f'Invalid phone number!: {phone}')

phone_matcher('+359 887605061')
phone_matcher('0887582381')
phone_matcher('+3529 887605061')
phone_matcher('08873582381')
phone_matcher('+35288760061')
phone_matcher('088582381')