from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# making my own copies of the class
menu_list = Menu()
menu_item = MenuItem
drink_maker = CoffeeMaker()
money_calc = MoneyMachine()
is_on = True
while is_on:
    choice = input(f"What would you like? {menu_list.get_items()} :").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        drink_maker.report()
        money_calc.report()
    else:
        drink = menu_list.find_drink(choice)
        if drink is not None:
            if drink_maker.is_resource_sufficient(drink):
                if money_calc.make_payment(drink.cost):
                    drink_maker.make_coffee(drink)