"""
vending_machine_ascii_ui.py

This script implements an ASCII based UI for the vending machine.

Author: Marco Chong (marco@marcochong.com)
"""
from decimal import ROUND_CEILING, Decimal

from vendingmachine.vending_machine import VendingMachine

class VendingMachineAsciiUi(VendingMachine):

    def __init__(self):
        super().__init__()

    # coin handler
    def print_supported_coins(self):
        print(self._coin_handler.supported_coins)

    def print_stored_coins(self):
        print(self._coin_handler.stored_coins)

    def print_inserted_coins(self):
        print(self._coin_handler.inserted_coins)

    def print_total_coins(self):
        print(self._coin_handler.total_coins)

    # inventory handler
    def print_inventory_price(self):
        print(self._inventory_handler.inventory_prices)
 
    def print_inventory(self):
        print(self._inventory_handler.inventories)

    # mixture handler
    def print_supported_mixtures(self):
        print(self._mixture_handler.supported_mixtures)

    # ui
    def print_vending_machine(self):
        mixtures_available = super()._mixture_handler.supported_mixtures
        mixtures_keys = sorted(mixtures_available.keys())

        print(f"************************************************************************************************************************")
        print(f"* Vending Machine                                                                                                      *")
        print(f"************************************************************************************************************************")
        print(f"- Supported Coins: {super()._coin_handler.supported_coins}")
        print(f"- Inventory Prices: {super()._inventory_handler.inventory_prices} (per unit)")
        print(f"- Mixtures Available:")
        for key in mixtures_keys:
            mixture_selected = mixtures_available[key]
            price = Decimal(0.0)
            for water_key in mixture_selected:
                price += self._inventory_handler.get_inventory_price(water_key) * mixture_selected[water_key]    
            price_ceil = price.to_integral_value(rounding=ROUND_CEILING)
            print(f"    {key}: {mixtures_available[key]} (Price: {price_ceil} ({price}))")
        print(f"------------------------------------------------------------------------------------------------------------------------")
        print(f"- Inventories: {super()._inventory_handler.inventories}")
        print(f"------------------------------------------------------------------------------------------------------------------------")
        print(f"- Stored Coins: {super()._coin_handler._stored_coins} (Amount: {super().get_stored_coins_amount()})")
        print(f"- Inserted Coins: {super()._coin_handler.inserted_coins} (Amount: {super().get_inserted_coins_amount()})")
        print(f"************************************************************************************************************************")
