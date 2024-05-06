# PE1 - Q4

integers = 1

while integers != 0:
    total = 0
    integers = int(input('Enter number: '))
    if integers == 0:
        break
    for digit in range(integers):
        new = int(input('Enter number: '))
        total += new
    print(total)
    print()







