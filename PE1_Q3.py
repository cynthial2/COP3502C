# PE1 - Q3

'''
def is_prime(n):
    if n % 2 or 3 or 5 or 7 != 0:
        result = 'prime'
    elif n == 1 or 2 or 3 or 5 or 7:
        result = 'prime'
    else:
        result = 'is not'
    return result

n = int(input('Enter a number: '))
print(is_prime(n))
'''

def is_prime(n):
    if n <= 1:
        result = 'False'
    for i in range(2, n):
        if n % i == 0:
            result = 'False'
            break
    else:
        result = 'True'
    return result

number = int(input('Enter number: '))
print(is_prime(number))






