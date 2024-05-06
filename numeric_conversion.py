# Lab 04: Numeric Conversion

import math

# Program Methods
def hex_char_decode(digit):
    if digit == 'A' or digit == 'a':
        answer = 10
    elif digit == 'B' or digit == 'b':
        answer = 11
    elif digit == 'C' or digit == 'c':
        answer = 12
    elif digit == 'D' or digit == 'd':
        answer = 13
    elif digit == 'E' or digit == 'e':
        answer = 14
    elif digit == 'F' or digit == 'f':
        answer = 15
    else:
        answer = int(digit)
    return answer


def hex_string_decode(hex):
    result = 0
    loop = 0
    for digit in reversed(hex):
        if digit == 'x':
            break
        else:
            result = hex_char_decode(digit)*(16**loop) + result
        loop += 1
    return str(result)


def binary_string_decode(binary):
    result = 0
    count = 1
    for digit in reversed(binary):
        if digit == '1':
            result += count
            count *= 2
        elif digit == '0':
            count *= 2
        else:
            break
    return result

def binary_to_hex(binary):
    decimal = binary_string_decode(binary)
    remainder = ''
    while decimal > 0:
        if decimal % 16 == 10:
            remainder = 'A' + remainder
        elif decimal % 16 == 11:
            remainder = 'B' + remainder
        elif decimal % 16 == 12:
            remainder = 'C' + remainder
        elif decimal % 16 == 13:
            remainder = 'D' + remainder
        elif decimal % 16 == 14:
            remainder = 'E' + remainder
        elif decimal % 16 == 15:
            remainder = 'F' + remainder
        else:
            remainder = str((decimal % 16)) + remainder
        decimal = math.floor(decimal/16)
    return remainder


# Main Program
def main():
    choose = 1
    while choose != 4:
        print('Decoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit\n')
        choose = int(input('Please enter an option: '))

        if 1 <= choose <= 3:
            string = str(input('Please enter the numeric string to convert: '))

            # 1. Decode hexadecimal
            if choose == 1:
                print('Result:', hex_string_decode(string))
                print()

            # 2. Decode binary
            elif choose == 2:
                print('Result:', binary_string_decode(string))
                print()

            # 3. Convert binary to hexadecimal
            elif choose == 3:
                print('Result:', binary_to_hex(string))
                print()

        # 4. Quit
        else:
            print('Goodbye!')
            break

if __name__ == "__main__":
    main()



