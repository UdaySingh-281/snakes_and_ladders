# Setting the player's behaviour
from board_design import snakes, ladders
from dice_setup import roll_a_die
def chance(player, current_pos):
  move = roll_a_die()
  print(f"Player {player} moved with {move}")


  if current_pos + move > 100:
    print("Invalid move")
    return current_pos

  else:
    current_pos += move

  if current_pos in snakes:
    current_pos -= move
    print(f"Player {player} got bitten by a snake and moved to {current_pos}")

  elif current_pos in ladders:
    current_pos += move
    print(f"Player {player} climbed a ladder and moved to {current_pos}")

  return current_pos