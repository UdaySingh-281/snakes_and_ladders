# Commencement of Game

from move import playing_chance

def playing_game(player1, player2, current_pos, flag = 1):
  dice_roll_1, dice_roll_2, turn = 0, 0, 0
  while flag:
    if flag == 1:
      dice_roll_1 += 1
      current_pos, flag = playing_chance(player1, current_pos, dice_roll_1), 2
      if current_pos == 100:
        flag = False
    elif flag == 2:
      dice_roll_2 += 1
      current_pos, flag = playing_chance(player2, current_pos, dice_roll_2), 1
      if current_pos == 100:
        flag = False

#Playing with two players
x = int(input("Set ID for Player 1: "))
y = int(input("Set ID for Player 2: "))
playing_game(x, y, 0)