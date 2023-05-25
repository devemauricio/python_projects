# rock paper scissors

import random
def play():
    user = str(input("Pick one option: 'r' for rock, 'p'for paper, 's for scissors: "))
    computer = random.choice(['r', 'p', 's'])
    options = {
        'r':'rock',
        'p':'paper',
        's':'scissors'
    }
    print(f"You choose {options[user]} and computer choose {options[computer]}")
    if user == computer:
        print('Tie')
    
    # r > s, s > p, p > r
    else:
        if is_win(user, computer):
            print('You Won!')
        else:
            print("You lost!")

def is_win(player, opponent):
    #return true if player wins

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent =='r'):
        return True
    
play()
