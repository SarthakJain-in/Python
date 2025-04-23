MENU = {
     "espresso": {
          "ingredients": {
               "water": 50,
               "milk": 0,
               "coffee": 18,
          },
          "cost": 1.5,
     },
     "latte": {
          "ingredients": {
               "water": 200,
               "milk": 150,
               "coffee": 24,
          },
          "cost": 2.5,
     },
     "cappuccino": {
          "ingredients": {
               "water": 250,
               "milk": 100,
               "coffee": 24,
          }, 
          "cost": 3.0,
     },
}

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def print_report():
    for item in resource:
        if item == "water" or item == "milk":
            print(f"{item}: {resource[item]}ml")
        if item == "coffee":
            print(f"{item}: {resource[item]}gm")
        if item == "money":
            print(f"{item}: ${resource[item]}")


def insert_coins(order):
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nicles? "))
    pennies = float(input("How many pennies? "))

    total_money = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    extra_money = 0

    if total_money == MENU[order]["cost"]:
        resource["money"] += total_money
        return True
    elif total_money > MENU[order]["cost"]:
        extra_money = total_money - MENU[order]["cost"]
        resource["money"] += total_money - extra_money
        print(f"Here is your ${round(extra_money, 2)} in change.")
        return True
    else:
        return False


def make_order(order):
    global resource
    for item in resource:
        if item == "water" or item == "milk" or item == "coffee":
            resource[item] -= MENU[f"{order}"]["ingredients"][item]

    print(f"Here is your {order}. Enjoy!")


def take_order():
    global resource

    is_on = True
    while is_on:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        is_sufficient_resource = True
        is_enough_money = False

        if order == "off":
            is_on = False

        elif order == "report":
            print_report()
        
        elif order == "latte" or order == "espresso" or order == "cappuccino":
            # Check resource sufficient
            for item in resource:
                if item == "water" or item == "milk" or item == "coffee":
                    if resource[item] < MENU[f"{order}"]["ingredients"][item] :
                        print(f"Sorry there is not enough {item}.")
                        is_sufficient_resource = False

            if is_sufficient_resource:
                is_enough_money = insert_coins(order)
                if is_enough_money:
                    make_order(order)
                else:
                    print("Sorry that's not enough money. Money refunded.")

        else:
            print("Invalid input. Type again.")

take_order()
