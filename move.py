# Playing a move
from player_setup import chance
def playing_chance(player, currentpos, dice_roll):
  dice_roll += 1
  currentpos = chance(player, currentpos)
  if currentpos == 100:
    print(f"Player {player} took {dice_roll} turns to win")
    return currentpos
  return currentpos