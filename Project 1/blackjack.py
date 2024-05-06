# Project 1 - Blackjack

from p1_random import P1Random
rng = P1Random()

# Data tracked over multiple games
game = 0
player_wins = 0
dealer_wins = 0
tie = 0

# Loop for 1 game
while game >= 0:
    game += 1
    print(f'START GAME #{game}\n')
    player = 0
    dealer = 0

    # Player draws random card and display
    card = rng.next_int(13) + 1
    if card == 1:
        print('Your card is a ACE!')
    elif card == 11:
        card = 10
        print('Your card is a JACK!')
    elif card == 12:
        card = 10
        print('Your card is a QUEEN!')
    elif card == 13:
        card = 10
        print('Your card is a KING!')
    else:
        print(f'Your card is a {card}!')
    player += card
    print(f'Your hand is: {player}\n')

    # Loop for 1 turn
    while player < 21 and dealer < 21:
        # Menu Selection
        print('1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n')
        choose = int(input('Choose an option: '))
        print()

        # OPTION 1: Player chooses to draw card again
        if choose == 1:
            card = rng.next_int(13) + 1
            if card == 1:
                print('Your card is a ACE!')
            elif card == 11:
                card = 10
                print('Your card is a JACK!')
            elif card == 12:
                card = 10
                print('Your card is a QUEEN!')
            elif card == 13:
                card = 10
                print('Your card is a KING!')
            else:
                print(f'Your card is a {card}!')
            player += card
            print(f'Your hand is: {player}\n')

            # Determine if player auto wins/loses
            if player == 21:
                print('BLACKJACK! You win!\n')
                player_wins += 1
                break
            elif player > 21:
                print('You exceeded 21! You lose.\n')
                dealer_wins += 1
                break

        # OPTION 2: Player chooses to let Dealer draw
        elif choose == 2:
            card = rng.next_int(11) + 16
            dealer += card
            print(f'Dealer\'s hand: {dealer}')
            print(f'Your hand is: {player}\n')
            if (dealer > 21) or (player > dealer):
                print('You win!\n')
                player_wins += 1
                break
            elif dealer > player:
                print('Dealer wins!\n')
                dealer_wins += 1
                break
            else:
                print('It\'s a tie! No one wins!\n')
                tie = tie + 1
                break

        # OPTION 3: Player chooses to view stats
        elif choose == 3:
            print(f'Number of Player wins: {player_wins}')
            print(f'Number of Dealer wins: {dealer_wins}')
            print(f'Number of tie games: {tie}')
            print(f'Total # of games played is: {game - 1}')
            print(f'Percentage of Player wins: {round((player_wins / (game - 1)) * 100,1)}%\n')
            continue

        # OPTION 4: Player chooses to exit game
        elif choose == 4:
            game = -1
            break

        # OTHER: Invalid input
        else:
            print('Invalid input!\nPlease enter an integer value between 1 and 4.\n')
            continue
