# PE1 - Q4

number = 1

while number != 0:
    total = 0
    number = int(input('Enter number: '))
    if number == 0:
        break
    for digit in range(number):
        new = int(input('Enter number: '))
        total += new
    print(total)
    print()







