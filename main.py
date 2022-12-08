from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def enter_resource(coffemaker):
    for item in coffemaker.resources:
        if item=="coffee":
         coffemaker.resources[item] += int(input(f"Enter the amount of {item} in gr "))
        else:
            coffemaker.resources[item] += int(input(f"Enter the amount of {item} in ml "))




money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.process_coins()
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                continue_coin="yes"
                while continue_coin == "yes" and input("Would you like to enter more coins? Type 'yes or no': ")== "yes":
                    money_machine.process_coins()
                    if(money_machine.money_received>=drink.cost):
                        print(f"Money you entered are enough to purchase {drink.name}")
                        continue_coin="no"
                        if money_machine.make_payment(drink.cost):
                            coffee_maker.make_coffee(drink)
                    else:
                        print(f"The total amount of money you entered is not enough to purchase {drink.name}")
                        if input("Type 'no' if you dont want to enter more coins and get your coins back.: ").lower() == "no":
                            print(f"Here is your {money_machine.money_received} $ change. Goodbye")
                            money_machine.money_received=0
                            continue_coin="no"

        else:
            ask_resource = input(
                "Would you like to enter resources inside the machine? Type 'yes' or 'no' please:").lower()
            if ask_resource == "yes":
                enter_resource(coffee_maker)
