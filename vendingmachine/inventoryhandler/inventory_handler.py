"""
inventory_handler.py

This script implements an inventory handler for vending machine that tracking inventories.

Author: Marco Chong (marco@marcochong.com)
"""

from decimal import Decimal

class InventoryHandler:

    _inventory_price = {}
    _inventory = {}

    def __init__(self):
        pass

    @property
    def inventories(self):
        return dict(self._inventory)

    @property
    def inventory_prices(self):
        return dict(self._inventory_price)

    def get_inventory_price(self, inventory_name: str):
        if inventory_name in self._inventory_price:
            return self._inventory_price[inventory_name]
        else:
            return Decimal(str(0.0))

    def set_inventory_price(self, inventory_name: str, price: Decimal):
        self._inventory_price[inventory_name] = price

    def clear_inventory_price(self):
        self._inventory_price = {}

    def add_inventory(self, inventory_name: str, count: Decimal):
        if inventory_name in self._inventory:
            self._inventory[inventory_name] += count
        else:
            self._inventory[inventory_name] = count

    def consume_inventory(self, inventory_name: str, count: Decimal):
        success = False
        
        if inventory_name in self._inventory:
            if self._inventory[inventory_name] >= count:
                success = True
                self._inventory[inventory_name] -= count

        return success

    def check_inventory(self, inventory_name: str):
        if inventory_name in self._inventory:
            return self._inventory[inventory_name]
        else:
            return Decimal(str(0.0))
        
    def check_inventories(self, inventory_dict: dict):
        success = True
    
        for key in inventory_dict:
            if key in self._inventory:
                if inventory_dict[key] > self._inventory[key]:
                    success = False
                    break
            else:
                success = False
                break

        return success
        
    def clear_all_inventory(self):
        self._inventory = {}

    def clear_inventory(self, inventory_name: str):
        if inventory_name in self._inventory:
            self._inventory[inventory_name] = Decimal(str(0.0))
