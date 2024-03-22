def calculate_area(shape, *args):
    if shape == 'circle':
        return print(f'The calculated area of the {shape} is {args[0]*args[0]*3.14:.2f}')
    else:
        return print(f'The calculated area of the {shape} is {args[0]*args[1]:.2f}')

calculate_area("rectangle", 5, 4)
calculate_area("rectangle", 7.5, 11.1234)
calculate_area("circle", 10)
calculate_area("circle", 11.3092581)