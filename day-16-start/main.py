from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

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

# beverage = input('What would you like? (espresso/latte/cappuccino): ')
# MenuItem.name = beverage
# MenuItem.cost = MENU[beverage]['cost']
# MenuItem.ingredients = MENU[beverage]['ingredients']

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

new_order = True
while new_order == True:
    options = menu.get_items()
    beverage = input(f'What would you like? ({options}): ')

    if beverage.lower() == "off":
        print('Machine turned off.')
        new_order = False

    elif beverage.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        choice = menu.find_drink(beverage)
        if coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)
