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


def check_resources(drink):
    if beverage != 'espresso':
        if resources['water'] < MENU[drink]['ingredients']['water']:
            print("Sorry, there is not enough water.")
            exit()
        elif resources['coffee'] < MENU[drink]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee.")
            exit()
        elif resources['milk'] < MENU[drink]['ingredients']['milk']:
            print("Sorry, there is not enough milk.")
            exit()
    else:
        if resources['water'] < MENU[drink]['ingredients']['water']:
            print("Sorry, there is not enough water.")
            exit()
        elif resources['coffee'] < MENU[drink]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee.")
            exit()


def pay_beverage(drink):
    print(f'It costs ${MENU[drink]["cost"]}.')
    print('Please insert coins.')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))
    payment = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    return payment


def check_enough_payment(amount, profit):
    if amount < MENU[beverage]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        exit()
    elif amount > MENU[beverage]['cost']:
        change = round(amount - MENU[beverage]['cost'], 2)
        profit += MENU[beverage]['cost']
        print(f'Here is ${change} dollars in change.')
        return profit


def deduct_resources(drink):
    if drink != 'espresso':
        resources['water'] = resources['water'] - MENU[drink]['ingredients']['water']
        resources['milk'] = resources['milk'] - MENU[drink]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - MENU[drink]['ingredients']['coffee']
    else:
        resources['water'] = resources['water'] - MENU[drink]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[drink]['ingredients']['coffee']
    print(f'Here is your {beverage}, enjoy!')


def refill_resources():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

money = 0
new_order = True
while new_order == True:
    beverage = input('What would you like? (espresso/latte/cappuccino): ')

    if beverage.lower() == "off":
        print('Machine turned off.')
        exit()

    if beverage.lower() == "report":
        print(f'Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${money}')
        exit()

    check_resources(beverage)
    paid_amount = pay_beverage(beverage)
    money = check_enough_payment(paid_amount, money)
    deduct_resources(beverage)