# PE1 - Q2

base = int(input('base = '))

def print_triangle(base):
    i = 1
    while i <= base:
        print('*' * i)
        i += 1

def print_inverse_triangle(base):
    j = base
    while j >= 1:
        print('*' * j)
        j -= 1

print_triangle(base)
print_inverse_triangle(base)








