import dealer
import user

final_result_user = user.play_human_turn()
final_result_dealer = dealer.play_dealer_turn()

# function for determining winner and printing result
def determine_winner(user, dealer):
    if dealer > 21 and user > 21:
        print('draw')
    elif dealer == user:
        print('draw')
    elif dealer > 21 and user < 21:
        print('you win')
    elif dealer < 21 and user > 21:
        print('you lose')
    elif user > dealer:
        print('you win')
    else:
        print('you lose')

determine_winner(final_result_user, final_result_dealer)

