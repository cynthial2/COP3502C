# Project 2

from console_gfx import ConsoleGfx


# Method 1: RLE/raw to hexadecimal (w/o delimiters)
def to_hex_string(data):
    string = ''
    for value in data:
        value = int(value)
        if value >= 10:
            if value == 10:
                string += 'a'
            elif value == 11:
                string += 'b'
            elif value == 12:
                string += 'c'
            elif value == 13:
                string += 'd'
            elif value == 14:
                string += 'e'
            elif value == 15:
                string += 'f'
        else:
            string += str(value)
    return string


# Method 2: Returns number of runs
def count_runs(flat_data):
    run = 1
    count = 1
    current = flat_data[0]
    for value in flat_data[1:]:
        if value == current:
            count += 1
            if count == 15:
                run += 1
                count = 0
        else:
            run += 1
            count = 1
        current = value
    return run


# Method 3: Returns encoding of raw data (compresses into RLE)
def encode_rle(flat_data):
    list = []
    count = 1
    current = flat_data[0]
    for value in flat_data[1:]:
        if value == current:
            count += 1
            if count == 15:
                list += [count] + [current]
                count = 0
        else:
            list += [count] + [current] if count != 0 else []
            count = 1
        current = value
    list += [count] + [current] if count != 0 else []
    return list


# Method 4: Returns decompressed size of RLE (number of data values)
def get_decoded_length(rle_data):
    length = 0
    for value in rle_data[::2]:
        length += value
    return length


# Method 5: Returns decoded data from RLE (decompresses RLE)
def decode_rle(rle_data):
    list = []
    temp = 0
    for idx, value in enumerate(rle_data):
        if idx % 2 == 0:
            temp = int(value)
        else:
            for i in range(temp):
                list += [value]
    return list


# Method 6: Translates string in hexadecimal format to byte data (raw or RLE)
def string_to_data(data_string):
    list = []
    for char in data_string:
        if char.isdigit() != True:
            if char == 'a':
                list += [10]
            elif char == 'b':
                list += [11]
            elif char == 'c':
                list += [12]
            elif char == 'd':
                list += [13]
            elif char == 'e':
                list += [14]
            elif char == 'f':
                list += [15]
        else:
            list += [int(char)]
    return list


# Method 7: Translates RLE to human-readable (run in decimal, value in hex)
def to_rle_string(rle_data):
    string = ''
    for idx, value in enumerate(rle_data):
        if idx % 2 == 0:
            string += str(value)
        else:
            value = int(value)
            if value < 10:
                string += str(value) + ':'
            elif value == 10:
                string += 'a:'
            elif value == 11:
                string += 'b:'
            elif value == 12:
                string += 'c:'
            elif value == 13:
                string += 'd:'
            elif value == 14:
                string += 'e:'
            elif value == 15:
                string += 'f:'
    return string[:-1]


# Method 8: Translates human-readable string to RLE (w/ delimiters)
def string_to_rle(rle_string):
    list = []
    rle_string.lower()
    tokens = rle_string.split(':')
    for token in tokens:
            list += [token[:-1]] + [token[-1]]
    new_list = []
    for value in list:
        if value.islower():
            if value == 'a':
                new_list += [10]
            elif value == 'b':
                new_list += [11]
            elif value == 'c':
                new_list += [12]
            elif value == 'd':
                new_list += [13]
            elif value == 'e':
                new_list += [14]
            elif value == 'f':
                new_list += [15]
        else:
            new_list += [value]
    return new_list


# Main Program
if __name__ == '__main__':
    image_data = None
    print('Welcome to the RLE image encoder!\n')
    print('Displaying Spectrum Image:')
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print('\n')

    choose = 1
    while choose != 0:
        # Menu Selection
        print(
            'RLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data\n')
        choose = int(input('Select a Menu Option: '))

        # Option #1: Load File
        if choose == 1:
            filename = str(input('Enter name of file to load: '))
            image_data = ConsoleGfx.load_file(filename)
            print()

        # Option #2: Load Test Image (Gator)
        elif choose == 2:
            image_data = ConsoleGfx.test_image
            print('Test image data loaded.\n')

        # Option #3: Read RLE String input
        elif choose == 3:
            data = input('Enter an RLE string to be decoded: ')
            image_data = decode_rle(string_to_rle(data))
            print()

        # Option #4: Read RLE Hex String input
        elif choose == 4:
            data = input('Enter the hex string holding RLE data: ')
            image_data = decode_rle(string_to_data(data))
            print()

        # Option #5: Read Data Hex String input
        elif choose == 5:
            data = input('Enter the hex string holding flat data: ')
            image_data = string_to_data(data)
            print()

        # Option #6: Display Image
        elif choose == 6:
            print('Displaying image...')
            if image_data == None:
                print('(no data)\n')
            else:
                ConsoleGfx.display_image(image_data)
                print()

        # Option #7: Display RLE String
        elif choose == 7:
            if image_data == None:
                print('RLE representation: (no data)\n')
            else:
                print('RLE representation:', to_rle_string(encode_rle(image_data)))
                print()

        # Option #8: Display Hex RLE Data
        elif choose == 8:
            if image_data == None:
                print('RLE hex values: (no data)\n')
            else:
                print('RLE hex values:', to_hex_string(encode_rle(image_data)))
                print()

        # Option #9: Display Hex Flat Data
        elif choose == 9:
            if image_data == None:
                print('Flat hex values: (no data)\n')
            else:
                print('Flat hex values:', to_hex_string(image_data))
                print()

'''
        # Other
        else:
            print('Error! Invalid Input.\n')
'''