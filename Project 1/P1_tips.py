# P1 - Blackjack (tips from lecture)

from p1_random import P1Random
rng = P1Random()

game_continue = True
game_number = 0

while game_continue:
    #1. Print game number message
    game_number += 1
    player_hand = 0
    print(f'Start Game #{game_number}')

    #2. Deal card to player
    player_card = rng.next_int(13) + 1
    if player_card == 1:
        print('Your card is a Ace')
    elif 2 <= player_card <= 10:
        print(f'Your card is a {player_card}')
    elif player_card == 11:
        # all face cards worth 10!
        pass

    print(player_card)
    player_hand += player_card
    print(player_hand)

    #3. Keep prompting user to choose menu option until win
    no_winner = True
    while no_winner:
        # print menu
        # ask player to enter new option
        # if menu option is 1
            # deal a card to player
            # update player hand
            # if hand value = 21, or > 21, someone win
                # end current game by setting no_winner to false













