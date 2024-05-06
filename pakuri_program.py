# Project 3: Pakudex Project (main)

from pakudex import Pakudex

if __name__ == '__main__':

    # Welcome + Menu
    print('Welcome to Pakudex: Tracker Extraordinaire!')
    while True:
        capacity = input('Enter max capacity of the Pakudex: ')
        if not capacity.isdigit():
            print('Please enter a valid size.')
            continue
        print(f'The Pakudex can hold {capacity} species of Pakuri.\n')
        instance = Pakudex(capacity)


        choose = 0
        while choose != '6':
            print('Pakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n'
                  '4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit\n')
            choose = input('What would you like to do? ')


            # 1. List Pakuri
            if choose == '1':
                if instance.get_species_array() is None:
                    print('No Pakuri in Pakudex yet!\n')
                else:
                    print('Pakuri In Pakudex:')
                    for idx, entry in enumerate(instance.get_species_array()):
                        print(f'{idx+1}. {entry}')
                    print()


            # 2. Show Pakuri
            elif choose == '2':
                name = input('Enter the name of the species to display: ')
                if instance.get_stats(name) is None:
                    print('Error: No such Pakuri!\n')
                else:
                    result = instance.get_stats(name)
                    print('\nSpecies:', name)
                    print('Attack:', result[0])
                    print('Defense:', result[1])
                    print('Speed:', result[2], '\n')


            # 3. Add Pakuri
            elif choose == '3':
                if instance.get_size() == instance.get_capacity():
                    print('Error: Pakudex is full!\n')
                else:
                    name = input('Enter the name of the species to add: ')
                    if instance.add_pakuri(name) is False:
                        print('Error: Pakudex already contains this species!\n')
                    else:
                        print(f'Pakuri species {name} successfully added!\n')


            # 4. Evolve Pakuri
            elif choose == '4':
                name = input('Enter the name of the species to evolve: ')
                if instance.evolve_species(name) is False:
                    print('Error: No such Pakuri!\n')
                else:
                    print(f'{name} has evolved!\n')


            # 5. Sort Pakuri
            elif choose == '5':
                instance.sort_pakuri()
                print('Pakuri have been sorted!\n')


            # Unknown Menu Selection
            elif choose != '6':
                print('Unrecognized menu selection!\n')


        # 6. Exit
        print('Thanks for using Pakudex! Bye!')
        break
