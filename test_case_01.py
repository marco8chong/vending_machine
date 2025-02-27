"""
run.py

This script creates and runs a vending machine.

Author: Marco Chong (marco@marcochong.com)
"""

from decimal import Decimal, getcontext

from vendingmachine.vending_machine_ascii_ui import VendingMachineAsciiUi

if __name__ == "__main__":

    vending_machine = VendingMachineAsciiUi()

    # define the coins supported
    vending_machine.add_supported_coins(Decimal(str(1.0)))
    vending_machine.add_supported_coins(Decimal(str(2.0)))
    vending_machine.add_supported_coins(Decimal(str(5.0)))
    vending_machine.add_supported_coins(Decimal(str(10.0)))

    # set the water prices
    vending_machine.set_inventory_price("plain_water", Decimal(str(30.0)))
    vending_machine.set_inventory_price("fizzy_water", Decimal(str(35.0)))

    # set the water mixtures
    vending_machine.add_supported_mixture(1, {"plain_water": Decimal(str(0.4)), "fizzy_water":  Decimal(str(0.6))})
    vending_machine.add_supported_mixture(2, {"plain_water": Decimal(str(0.5)), "fizzy_water":  Decimal(str(0.5))})
    vending_machine.add_supported_mixture(3, {"plain_water": Decimal(str(0.6)), "fizzy_water":  Decimal(str(0.4))})

    # prepare coins for change
    vending_machine.store_coin(1, 100)
    vending_machine.store_coin(2, 100)
    vending_machine.store_coin(5, 100)
    vending_machine.store_coin(10, 100)

    # prepare water for sale
    vending_machine.add_inventory("plain_water", Decimal(str(100.0)))
    vending_machine.add_inventory("fizzy_water", Decimal(str(100.0)))

    user_input = ""
    while user_input != "q":
        # print vending machine
        vending_machine.print_vending_machine()

        # get user input
        print(f"1: Insert a '1' coin, 2: Insert a '2' coin")
        print(f"5: Insert a '5' coin, 10: I1nsert a '10' coin")
        print(f"m1: Purchase mixture {vending_machine.get_supported_mixture(1)}")
        print(f"m2: Purchase mixture {vending_machine.get_supported_mixture(2)}")
        print(f"m3: Purchase mixture {vending_machine.get_supported_mixture(3)}")
        print(f"r: Refund")
        print(f"q: Quit")
        user_input = input("Please enter your choice: ")

        if user_input == "1":
            vending_machine.insert_coin(1)
        elif user_input == "2":
            vending_machine.insert_coin(2)
        elif user_input == "5":
            vending_machine.insert_coin(5)
        elif user_input == "10":
            vending_machine.insert_coin(10)
        elif user_input == "m1":
            print(vending_machine.purchase_water(1))
        elif user_input == "m2":
            print(vending_machine.purchase_water(2))
        elif user_input == "m3":
            print(vending_machine.purchase_water(3))
        elif user_input == "r":
            vending_machine.return_inserted_coins()
        elif user_input == "q":
            pass
        else:
            print("Incorrect input.")

        print()
