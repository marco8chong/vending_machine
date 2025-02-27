"""
run.py

This script creates and runs a vending machine.

Author: Marco Chong (marco@marcochong.com)
"""

from vendingmachine.vending_machine import VendingMachine

if __name__ == "__main__":
    vending_machine = VendingMachine()

    ###
    ### define the coins supported
    vending_machine.add_supported_coins(1.0)
    vending_machine.add_supported_coins(2.0)
    vending_machine.add_supported_coins(5.0)
    vending_machine.add_supported_coins(10.0)
    # vending_machine.print_supported_coins()

    ###
    ### set the water prices
    vending_machine.set_inventory_price("plain_water", 30.0)
    vending_machine.set_inventory_price("fizzy_water", 35.0)
    # vending_machine.print_inventory_price()

    ###
    ### set the water mixtures
    vending_machine.add_supported_mixture(1, {"plain_water": 0.4, "fizzy_water":  0.6})
    vending_machine.add_supported_mixture(2, {"plain_water": 0.5, "fizzy_water":  0.5})
    vending_machine.add_supported_mixture(3, {"plain_water": 0.6, "fizzy_water":  0.4})
    vending_machine.print_supported_mixtures()

    # preparing coins for change
    vending_machine.store_coin(1, 1000)
    vending_machine.store_coin(2, 1000)
    vending_machine.store_coin(5, 1000)
    vending_machine.store_coin(10, 1000)
    # vending_machine.print_stored_coins()

    # preparing water for sale
    vending_machine.add_inventory("plain_water", 100)
    vending_machine.add_inventory("fizzy_water", 100)
    # vending_machine.print_inventory()

    # debugging only
    result = vending_machine.resolve_change_coins_combination(168.0)
    print("Result")
    print(result)
    print(sum(result))