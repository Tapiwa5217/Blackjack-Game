# randint used to generate random cards.
from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw

# function for dealer's turn
def play_dealer_turn():
  total_hand = 0
  give_card = 1
  card = ''

  while (give_card <= 2):
    card = randint(1,13)
    print(draw(card))
    value = card_value(card)
    total_hand += value  
    give_card += 1

  while total_hand < 17:
      print(f"Dealer has {total_hand}.")
      card = randint(1,13)
      value = card_value(card)
      current_draw = draw(card)
      print(current_draw)
      total_hand += value

  print(f"Final hand: {total_hand}.")
  final_result = blackjack_or_bust(total_hand)
  if(total_hand >= 21):
    print(final_result)

  return total_hand





