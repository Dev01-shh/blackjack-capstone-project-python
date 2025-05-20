# Blackjack Capstone project 
import random 

numbers = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Ace conversion logic
def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

ask = input("Do you want to play a game of blackjack? type 'y' or 'n' : ").lower().strip()
if ask == 'y':
    print(''' 
          
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
        |  \/ K|                            _/ |                
        '------'                           |__/  
          ''')
    # Creating card lists
    user_card = []
    computer_card = []
    # Creating cards and calculating scores
    user_card.append(random.choice(numbers))
    user_card.append(random.choice(numbers))
    user_score = calculate_score(user_card)
    computer_card.append(random.choice(numbers))
    computer_card.append(random.choice(numbers))
    computer_score = calculate_score(computer_card)
# Checking win or lose
    def check_user():
            if user_score > 21: 
                print(f'      Your final hand : {user_card}, final score : {user_score}')
                print(f"      Computer's final hand : {computer_card}, final score : {computer_score}") 
                print('You went over. You lose')
            elif user_score == 21:
                print('You won !')

    def check_computer():
        if computer_score > 21:
            print(f'      Your final hand : {user_card}, final score : {user_score}')
            print(f"      Computer's final hand : {computer_card}, final score : {computer_score}") 
            print('Opponent went over. You win')
        elif computer_score == 21:
            print('Computer win. You lose')


# Main game logic
    while True:
        print(f'      Your cards : {user_card},  current score : {user_score}')
        print(f"      Computer's first card : {computer_card[0]}")
        check_user() 
        if user_score > 21 or  user_score == 21:
            break
        should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
        if should_continue == 'y':
            user_card.append(random.choice(numbers))
            user_score = calculate_score(user_card)
            continue
        elif should_continue == 'n':
                computer_card.append(random.choice(numbers))
                computer_score = calculate_score(computer_card)
                if computer_score > 21 or computer_score == 21:
                     check_computer()
                     break
                else:
                    print(f'      Your final hand : {user_card}, final score : {user_score}')
                    print(f"      Computer's final hand : {computer_card}, final score : {computer_score}")
                    if user_score > computer_score:
                        print('You won !')
                        next_game = input("Do you want to play a game of blackjack? type 'y' or 'n' : ").lower().strip()
                        if next_game == 'y':
                            continue
                        else:
                            break
                    elif computer_score > user_score:
                        print('You lose.')
                        next_game = ("Do you want to play a game of blackjack? type 'y' or 'n' : ").lower().strip()
                        if next_game == 'y':
                            continue
                        else:
                            break
        else:
            print('Please enter a valid input')
else:
    print('Please enter valid input ')
    

