Bid = {}

def max_bid():
    max = 0
    name = ""

    for key in Bid:
        if int(Bid[key]) > int(max):
            max = Bid[key]
            name = key
    print(f"{name} has the maximum bid of Rs.{max}")

def add_bid():
    name = input("What us your name? \n")
    bid_amount = input("What's your bid? \n")
    Bid[name] = bid_amount

    next_bid()

def next_bid():
    next = input("Are there any other bidder? Type 'yes' or 'no'\n").lower()
    print("\n" * 20)
    if next == "yes" :
        add_bid()
    elif next == "no" :
        max_bid()
    else:
        print("Invalid input.")
        next_bid()

add_bid()