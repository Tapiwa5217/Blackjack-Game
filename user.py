# Use randint to generate random cards. 
from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw
# function for human's turn
def play_human_turn():
  total_hand = 0
  give_card = 1
  card = ''
  while (give_card <= 2):
    card = randint(1,13)
    print(draw(card))
    value = card_value(card)
    total_hand += value  
    give_card += 1 

  while (total_hand < 21):
    move = input(f"You have {total_hand}. Hit (y/n)? ")
    while (move != 'y' and move != 'n'):
        print("Sorry I didn't get that.")
        move = input(f"You have {total_hand}. Hit (y/n)? ")

    if (move == 'y'):
        card = randint(1,13)
        print(draw(card))
        value = card_value(card)
        total_hand += value 
    elif(move == 'n'):
        break 

  print(f"Final hand: {total_hand}.")
  final_result = blackjack_or_bust(total_hand)

  if(total_hand >= 21):
    print(final_result)

  return total_hand
            

    