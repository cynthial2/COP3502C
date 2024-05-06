# Lab 07: The Cow Says... (1)

from heifer_generator import HeiferGenerator
import sys


def list_cows(cows):
    print('Cows available:', end=' ')
    for cow in cows:
        print(cow.get_name(), end=' ')
    print('\n')

def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow.get_image()
    return None


if __name__ == '__main__':
    cows = HeiferGenerator.get_cows()

    # Lists all available cows
    if sys.argv[1] == '-l':
        list_cows(cows)

    # Print message with specified cow
    elif sys.argv[1] == '-n':
        image = find_cow(sys.argv[2], cows)
        if image == None:
            print(f'Could not find {sys.argv[2]} cow!\n')
        else:
            print(' '.join(sys.argv[3:]))
            print(image)

    # Print message with default cow
    else:
        print(' '.join(sys.argv[1:]))
        print(cows[0].get_image())


