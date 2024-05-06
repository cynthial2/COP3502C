# Lab 03: Scientific Calculator

import math

current = 0.0
total = 0.0
calculations = 0
choose = 1
print('Current Result:', current)
print()

# Using calculator
while choose != 0:
    # Display menu
    if 1 <= choose <= 6:
        print('Calculator Menu')
        print('---------------')
        print('0. Exit Program')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Exponentiation')
        print('6. Logarithm')
        print('7. Display Average')
        print()
    choose = int(input('Enter Menu Selection: '))

    # Average
    if choose == 7:
        if total == 0:
            print()
            print('Error: No calculations yet to average!')
            print()
        else:
            print()
            print('Sum of calculations:', total)
            print('Number of calculations:', calculations)
            print('Average of calculations:', '%.2f' % (total/calculations))
            print()

    # Exit Calculator
    elif choose == 0:
        print()
        print('Thanks for using this calculator. Goodbye!')

    # Calculator Functions
    elif 1 <= choose <= 6:
        # Enter numbers
        num1 = str(input('Enter first operand: '))
        num2 = str(input('Enter second operand: '))
        # Extra credit: use prev result as input
        if num1 == 'RESULT':
            num1 = current
        if num2 == 'RESULT':
            num2 = current
        num1 = float(num1)
        num2 = float(num2)
        print()

        if choose == 1:
            current = num1 + num2
        elif choose == 2:
            current = num1 - num2
        elif choose == 3:
            current = num1 * num2
        elif choose == 4:
            current = num1 / num2
        elif choose == 5:
            current = num1 ** num2
        elif choose == 6:
            current = math.log(num2, num1)

        # Current Results
        print('Current Result:', current)
        print()
        total = total + current
        calculations = calculations + 1

    # Invalid Menu Selection
    else:
        print()
        print('Error: Invalid selection!')
        print()





