# Lab 02: Four Function Calculator

num1 = float(input('Enter first operand: '))
num2 = float(input('Enter second operand: '))
print()

print('Calculator Menu')
print('---------------')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print()

choose = int(input('Which operation do you want to perform? '))
print()

if choose == 1:
    print('The result of the operation is ' + str(num1 + num2) + '. Goodbye!')
elif choose == 2:
    print('The result of the operation is ' + str(num1 - num2) + '. Goodbye!')
elif choose == 3:
    print('The result of the operation is ' + str(num1 * num2) + '. Goodbye!')
elif choose == 4:
    print('The result of the operation is ' + str(num1 / num2) + '. Goodbye!')
else:
    print('Error: Invalid selection! Terminating program.')
