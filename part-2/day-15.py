# from recipe_data import recipes
# from recipe_data import resources
# def pennies():
#     number_of_pennies = int(input("How many pennies"))
#     total_penny_value = number_of_pennies * 0.01
#     return total_penny_value
# def dimes():
#     number_of_dimes = int(input("How many dimes? "))
#     total_dime_value = number_of_dimes * 0.10
#     return total_dime_value
# def nickles():
#     number_of_nickles = int(input("How many nickles? "))
#     total_nickle_value = number_of_nickles * 0.05
#     return total_nickle_value
# def quarters():
#     number_of_quarters = int(input("How many quarters? "))
#     total_quarter_value = number_of_quarters * 0.25
#     return total_quarter_value

# def change_conversion():
#     pennies() 
#     nickles()
#     dimes()
#     quarters()

# type_of_coffee = input("Welcome to the coffee machine, what would you like? (espresso/latte/cappuccino):")

# if type_of_coffee == 'espresso':
#     espresso_order = recipes[0]
# elif type_of_coffee == 'latte':
#     print("you picked latte")
# elif type_of_coffee == 'cappuccino':
#     print("you picked cappuccino")
# elif type_of_coffee == 'report':
#     coffee = resources("coffee")[0]
#     print(f"there is {coffee}ml left")

MENU = {
    "espresso": {
        "ingredients": {
        'water': 50,
        'coffee': 18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients": {
        'water': 200,
        'coffee': 24,
        'milk': 150,
        },
        'cost': 2.50,
    },
    "cappuccino": {
        "ingredients":{
        'water':250,
        'coffee': 24,
        'milk': 100,
        },
        'cost': 3.00,
    },
}
profit = 0
resources = {
        'water': 300,
        'milk': 200,
        'coffee': 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """ returns the total calcuated from coins inserted"""
    print("please insert coins.")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.10
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """return true when the payment is accpted, or false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}")



is_on = True

while True: 
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off': 
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

