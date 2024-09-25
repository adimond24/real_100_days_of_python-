import random
def deal_card():
    """yReturns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """take list of cards and return score calcuated from cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(m_score, computer_score):
    if m_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "lose, opponent has blackjack"
    elif m_score == 0:
        return "win with a blackjack"
    elif m_score > 21:
        return "you went over. you lose"
    elif computer_score > 21:
        return "Opponent went over. you win"
    elif m_score> computer_score:
        return "you win"
    else:
        return "you lose"

def play_game():   
    

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over: 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, current score: {user_score} ")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand:{user_cards}, final score: {user_score} ")
    print(f"computers final hand: {computer_cards}, final score{computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want t0 play a game of blackjack? Type 'y' or 'n': ") == "y": 
    print("\n" * 20)
    play_game()
# start = input("Do you want to play a game of Black Jack? Type 'y' or 'n': ")

# if start == 'y':
#     num1 = int(random.choice(cards))
#     num2 = int(random.choice(cards))
#     comp = int(random.choice(cards))
#     print(f"Your cards: [{num1, num2}], current score:{num1 + num2} ")
#     print(f"Computer's first card: {comp}")
#     input("Type 'y' to get another card, type 'n' to pass: ")
