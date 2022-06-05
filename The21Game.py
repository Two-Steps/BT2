from random import randint

game = True
play_again = True
while game:
    while play_again:
        current_player = randint(0,1)
        current_number = 0
        while current_number < 21:
            print('Current number:',current_number)
            if current_player == 0:
                player_choice = ''
                while not player_choice in ['1','2','3']:
                    player_choice = input('---> Input your number:')
                current_number += int(player_choice)
                if current_number >= 21:
                    print('Current number:',current_number) 
                    print('You loss!')
                    game = False
                else: 
                    print('Current number:',current_number)
                    current_player = 1
            if current_player == 1:
                computer_choice = randint(1,3)
                print('---> Computer choice',computer_choice)
                current_number += computer_choice
                if current_number >= 21:
                    print('Current number:',current_number)
                    print('You win!')
                    game = False
                else:
                    current_player = 0
        pa = input('Enter "y" to play again, any to quit the game: ')
        if pa == 'y':
            play_again = True
        else:
            print('Goodbye!')
            play_again = False
                