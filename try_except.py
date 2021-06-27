def div42by(divideBy):
    try:
        try:
            return 42 / divideBy
        except ZeroDivisionError:
            print('Error: You tried to divide by zero.')
    except TypeError:
        print('Please input only numbers for this operations.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
print(div42by('A'))
