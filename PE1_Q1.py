# PE1 - Q1

num = int(input('num = '))

def indentica_digits(num):
    print(num, end=' ')
    while num % 11 != 0:
        num += 1
        print(num, end=' ')

indentica_digits(num)






