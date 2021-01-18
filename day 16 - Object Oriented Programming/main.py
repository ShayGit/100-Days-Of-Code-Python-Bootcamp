from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def order_coffee():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True
    while is_on:
        user_input = input(f"What would you like? {menu.get_items()}:")
        if user_input == 'off':
            is_on = False
        elif user_input == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(user_input)
            if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


if __name__ == '__main__':
    order_coffee()

