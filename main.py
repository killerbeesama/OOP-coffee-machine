import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_running = True
while is_running:
    promp_users = input(f"What would you like? ({menu.get_items()}): ")
    if promp_users == "espresso" or promp_users == "latte" or promp_users == "cappuccino":
        os.system("cls")
        drink = menu.find_drink(promp_users)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    elif promp_users == "report":
        os.system("cls")
        coffee_maker.report()
        money_machine.report()
    elif promp_users == "off":
        os.system("cls")
        print("Turning off")
        is_running = False
    else:
        print("Please type in a valid keyword and try again.")




