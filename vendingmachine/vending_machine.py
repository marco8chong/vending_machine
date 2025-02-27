"""
vending_machine.py

This script implements a vending machine that sells plain and fizzy water in multiple proportions.
It tracks inventory, accepts coins, provides change, and allows user interaction.

Author: Marco Chong (marco@marcochong.com)
"""

import math

from vendingmachine.inventoryhandler.inventory_handler import InventoryHandler
from vendingmachine.coinhandler.coin_handler import CoinHandler
from vendingmachine.mixturehandler.mixture_handler import MixtureHandler

class VendingMachine:

    _coin_handler = CoinHandler()
    _inventory_handler = InventoryHandler()
    _mixture_handler = MixtureHandler()

    def __init__(self):
        pass

    # coin handler
    def add_supported_coins(self, coin: float):
        self._coin_handler.add_supported_coins(float(coin))

    def insert_coin(self, coin: float, count: int = 1):
        return self._coin_handler.insert_coin(float(coin), int(count))
    
    def store_coin(self, coin: float, count: int = 1):
        return self._coin_handler.store_coin(float(coin), int(count))

    def get_inserted_coins_amount(self):
        return self._coin_handler.inserted_coins_amount
    
    def get_stored_coins_amount(self):
        return self._coin_handler.stored_coins_amount

    def store_inserted_coin(self):
        self._coin_handler.store_inserted_coin()

    def return_inserted_coins(self):
        self._coin_handler.return_inserted_coins()

    # inventory handler
    def set_inventory_price(self, inventory_name: str, price: float):
        self._inventory_handler.set_inventory_price(str(inventory_name), float(price))

    def clear_inventory_price(self):
        self._inventory_handler.clear_inventory_price()
    
    def add_inventory(self, inventory_name: str, count: float):
        self._inventory_handler.add_inventory(str(inventory_name), float(count))

    def clear_inventory(self):
        self._inventory_handler.clear_all_inventory()

    # mixture handler
    def add_supported_mixture(self, mixture_id: int, mixture: dict):
        self._mixture_handler.add_supported_mixture(int(mixture_id), dict(mixture))

    def clear_supported_mixtures(self):
        self._mixture_handler.clear_supported_mixtures()

    def get_supported_mixture(self, mixture_id: int):
        return self._mixture_handler.get_supported_mixtures(int(mixture_id))        

    # purchase water
    def purchase_water(self, mixture_id: int):
        mixture_selected = self.get_supported_mixture(int(mixture_id))

        if mixture_selected:
            # check inventory stock
            have_stock = self._inventory_handler.check_inventories(mixture_selected)

            if have_stock:
                # calculate purchase price
                purchase_amount = 0.0
                for water_key in mixture_selected:
                    # price = inventory price * mixture proportion
                    purchase_amount += self._inventory_handler.get_inventory_price(water_key) * mixture_selected[water_key]    
                purchase_amount = float(math.ceil(purchase_amount))

                # check inserted coins amount
                if self._coin_handler.inserted_coins_amount >= purchase_amount:
                    change_coin_amount = self._coin_handler.inserted_coins_amount - purchase_amount
                    change_coin_combination = self._coin_handler.resolve_change_coins_combination(change_coin_amount)

                    no_change = (change_coin_amount > 0.0) and (not change_coin_combination) 

                    if not no_change:
                    # store the inserted coins
                        self._coin_handler.store_inserted_coin()

                        # consume inventory
                        for key in mixture_selected:
                            self._inventory_handler.consume_inventory(key, mixture_selected[key])

                        # change
                        self._coin_handler.change(change_coin_combination)

                        return f"Purchase success ({mixture_selected}). Changed {change_coin_combination} (Sum: {sum(change_coin_combination)})."
                    else:
                        return f"No change available."
                else:
                    return f"Insufficient coins."
            else:
                return f"Out of stock: {mixture_selected}"
        else:
            return "Incorrect water mixture selection."