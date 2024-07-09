MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money=0
is_on = True

def resources_check(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def fill(resource):
    for item in resources:
        resource[item] += 100


def money_enough(paid, cost):
    global money
    if paid < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(paid - cost, 2)
        print(f"Here is your change: ${change}")
        money += cost
        return True

def make_coffee(coffee_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffee_name}")
def coin_check():
    insert_coin=(int(input("How many pennies: "))*0.01 + int(input("How many nickles: "))*0.05 +
                 int(input("How many dimes: "))*0.10 + int(input("How many quarters: "))*0.25)
    return insert_coin


while is_on:
    ask=input("What would you like? (espresso/latte/cappuccino): ")
    if ask == "off":
        print("Turning off.")
        is_on = False
    elif ask == "report":
        print(f"""Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}
""")
    elif ask == "fill":
        fill(resources)
    else:
        drink=MENU[ask]
        if resources_check(drink["ingredients"]):
            payment=coin_check()
            if money_enough(payment, drink["cost"]):
                make_coffee(ask, drink["ingredients"])
