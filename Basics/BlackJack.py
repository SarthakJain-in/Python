import random

graphics = """ _     _            _      _            _   
| |   | |          | |    (_)          | |  
| |__ | | __ _  ___| | __  _  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / | |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <  | | (_| | (__|   <| 
|_.__/|_|\__,_|\___|_|\_\ | |\__,_|\___|_|\_
                         _/ |
                         |__/                  
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def score(cards):
    sum = 0
    for num in cards:
        sum += num
    return sum

def print_score(your_cards, dealer_cards):
    your_score = score(your_cards)
    dealer_score = score(dealer_cards)
    
    print(f"    Your cards : {your_cards}, Current score : {your_score}")
    print(f"    Dealers first cards : {dealer_score}")

    # if your_score > 21:
    #     print("You went over, you lose.")
    #     blackjack(cards)
    # elif dealer_score > 21:
    #     print("Dealer went over, you win.")
    #     blackjack(cards)
    # else:
    #     return


def print_result(your_cards, dealer_cards):
    your_score = score(your_cards)
    dealer_score = score(dealer_cards)
    
    print(f"    Your final hand : {your_cards}, final score : {your_score}")
    print(f"    Dealer's final hand : {dealer_cards}, final score : {dealer_score}")

    if your_score > 21:
        print("You went over, you lose.")
    elif dealer_score > 21:
        print("Dealer went over, you win.")
    else:
        if your_score > dealer_score:
            print("You win.")
        elif your_score < dealer_score:
            print("You lose")
        else:
            print("Draw")
    
    blackjack(cards)
    

def blackjack(cards):
    restart = input("Do you want to play a game of BlackJack?, type 'y' or 'n' : ")
    if restart == 'y' :
        print(graphics)

        your_cards = []
        dealers_cards = []

        your_cards.append(random.choice(cards))
        your_cards.append(random.choice(cards))
        
        dealers_cards.append(random.choice(cards))

        print_score(your_cards, dealers_cards)

        add_card = input("Type 'y' to get another card, type 'n' to pass : ")
        
        if add_card == "y":
            your_cards.append(random.choice(cards))
            print_score(your_cards, dealers_cards)
            dealers_cards.append(random.choice(cards))
            print_result(your_cards, dealers_cards)
        elif add_card == "n":
            dealers_cards.append(random.choice(cards))
            print_result(your_cards, dealers_cards)
    elif restart == 'n':
        print("Game closed.")
        return
    else:
        print("Invalid onput, type again.")
        blackjack(cards)
    


blackjack(cards)