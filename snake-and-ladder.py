import random
import sys

player_1 = input("Enter the player-1 name: ").title()
player_2 = input("Enter the player-2 name: ").title()


player1_score,player2_score = 0,0
winning_point=100

snakes = {16:8, 32:20, 43:4, 50:27, 73:32, 87:49, 98:6,92:77}
ladders = {7:24, 14:40, 25:89, 37:42, 57:76, 79:83}

def dice():
    return random.randint(1,6)

def player1_turn():
    global player1_score
    player1_status = input(f"{player_1}, You want to [c]ontinue or [q]uit: ").lower()
    if player1_status=='c':
        cur_dic = dice()
        print(f'Dice: {cur_dic}')
        player1_score+=cur_dic

        if player1_score>=winning_point:
            print(f'Congrats {player_1}, You Won The Game!!!')
            sys.exit()
     
        if player1_score in snakes:
            player1_score = snakes[player1_score]
            print(f'Board position after snake bit: {player1_score}----------')
        elif player1_score in ladders:
            player1_score = ladders[player1_score]
            print(f'Board position after ladder: {player1_score}+++++++++')
        else:
           print(f'Board position: {player1_score}')
        
    else:
        print(f'Congrats {player_2}, You Won The Game!!!')


def player2_turn():
    global player2_score
    
    player2_status = input(f"{player_2}, You want to [c]ontinue or [q]uit: ").lower()
    if player2_status=='c':
        cur_dic = dice()
        print(f'Dice: {cur_dic}')

        if player2_score+cur_dic<=winning_point:
            player2_score+=cur_dic
            if player2_score in snakes:
                player2_score = snakes[player2_score]
                print(f'Board position after snake bit: {player2_score}----------')
            elif player2_score in ladders:
                player2_score = ladders[player2_score]
                print(f'Board position after ladder: {player2_score}+++++++++')
            else:
               print(f'Board position: {player2_score}')
        else:
               print(f'Board position no change: {player2_score}')
            
        
    else:
        print(f'Congrats {player_1}, You Won The Game!!!')


while player1_score<winning_point and player2_score<winning_point:
    player1_turn()
    player2_turn()

if player1_score > player2_score:
    print(f'Congrats {player_1}, You Won The Game!!!')
else:
    print(f'Congrats {player_2}, You Won The Game!!!')
    
    