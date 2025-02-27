"""
vending_machine.py

This script implements a vending machine that sells plain and fizzy water in multiple proportions.
It tracks inventory, accepts coins, provides change, and allows user interaction.

Author: Marco Chong (marco@marcochong.com)
"""
from vendingmachine.inventoryhandler.inventory_handler import InventoryHandler
from vendingmachine.coinhandler.coin_handler import CoinHandler
from vendingmachine.mixturehandler.mixture_handler import MixtureHandler

class VendingMachine:

    _coin_handler = CoinHandler()
    _inventory_handler = InventoryHandler()
    _mixture_handler = MixtureHandler()

    def __init__(self):
        pass

    ###
    ### coin handler
    ###

    def add_supported_coins(self, coin: float):
        self._coin_handler.add_supported_coins(float(coin))

    def insert_coin(self, coin: float, count: int = 1):
        return self._coin_handler.insert_coin(float(coin), int(count))
    
    def store_coin(self, coin: float, count: int = 1):
        return self._coin_handler.store_coin(float(coin), int(count))

    def store_inserted_coin(self):
        self._coin_handler.store_inserted_coin()

    def print_supported_coins(self):
        print(self._coin_handler.supported_coins)

    def print_stored_coins(self):
        print(self._coin_handler.stored_coins)

    def print_inserted_coins(self):
        print(self._coin_handler.inserted_coins)

    def print_total_coins(self):
        print(self._coin_handler.total_coins)

    ###
    ### inventory handler
    ###

    def set_inventory_price(self, inventory_name: str, price: float):
        self._inventory_handler.set_inventory_price(str(inventory_name), float(price))

    def clear_inventory_price(self):
        self._inventory_handler.clear_inventory_price()

    def print_inventory_price(self):
        print(self._inventory_handler.inventory_prices)
    
    def add_inventory(self, inventory_name: str, count: float):
        self._inventory_handler.add_inventory(str(inventory_name), float(count))

    def clear_inventory(self):
        self._inventory_handler.clear_all_inventory()

    def print_inventory(self):
        print(self._inventory_handler.inventories)

    ###
    ### mixture handler
    ###

    def add_supported_mixture(self, mixture_id: int, mixture: dict):
        self._mixture_handler.add_supported_mixture(int(mixture_id), dict(mixture))

    def clear_supported_mixtures(self):
        self._mixture_handler.clear_supported_mixtures()

    def print_supported_mixtures(self):
        print(self._mixture_handler.supported_mixtures)

    ###
    ### debug
    ###
    def resolve_change_coins_combination(self, amount: float):
        return self._coin_handler.resolve_change_coins_combination(amount)
    
    def get_supported_mixture(self, mixture_id: int):
        return self._mixture_handler.get_supported_mixtures(int(mixture_id))