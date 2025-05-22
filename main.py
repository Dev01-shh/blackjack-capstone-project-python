import random 

numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return score

def deal_card():
    return random.choice(numbers)

def display_logo():
    print(''' .------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
    |  \/ K|                            _/ |                
    '------'                           |__/   ''')
def play_game():
    display_logo()
    user_hand = [deal_card() , deal_card()]
    computer_hand = [deal_card() , deal_card()]

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Your cards: {user_hand}, current score: {user_score}")
    print(f"Computer's first card: {computer_hand[0]}")

    if user_score == 21 and len(user_hand) == 2:
        print("Blackjack! You win!")
        return
    
    game_over = False
    while not game_over:
        should_continue = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
        if should_continue == 'y':
            user_hand.append(deal_card())
            user_score = calculate_score(user_hand)
            print(f"Your cards: {user_hand}, current score: {user_score}")
            print(f"Computer's first card: {computer_hand[0]}")
            if user_score > 21:
                game_over = True
        elif should_continue == 'n':
            game_over = True
        else:
            print("Invalid input, please type 'y' or 'n'.")

    while calculate_score(computer_hand) < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"\nYour final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(user_score, computer_score))

def compare(user_score , computer_score):
    if user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score == computer_score:
        return "It's a draw."
    elif user_score == 21 and len(user_hand) == 2:
        return "Blackjack! You win!"
    elif computer_score == 21 and len(computer_hand) == 2:
        return "Computer has Blackjack. You lose!"
    elif user_score > computer_score:
        return "You won!"
    else:
        return "You lose."
    

def main():
    while True:
        ask = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
        if ask == 'y':
            play_game()
        elif ask == 'n':
            print("Goodbye 👋")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

main()
