import random

#the program is build to facilitate the extension of the possible options
choices = ['rock','paper','scissor']

#winning is a tuple of combinaisons (player_choice, computer_choice) for which the player wins
winning = (('rock','scissor'),('scissor','paper'),('paper','rock'))

#play_again is a variable to indicate if the player want to continue to play
play_again = True

while play_again:
    computer = random.choice(choices)
    player = None
    #The following loop aims to force the player to choose one of the option in choice list
    while player not in choices:
        player = input('rock paper or scissor?: ').lower()
# here we display the random computer selection and the choice of the player
    print('computer', computer)
    print('player', player)
    
    if player==computer:
        print('Tie')
    elif (player,computer) in winning:
        print('You Win')
    else:
        print('You Lose')
    new_turn = input("Do You Want To Play Again? (yes/no): ").lower()
    play_again = new_turn=='yes'

print("Bye")