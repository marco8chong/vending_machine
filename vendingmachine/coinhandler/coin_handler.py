"""
coin_handler.py

This script implements a coin handler for vending machine that allowing
inserting and changing coins.

Author: Marco Chong (marco@marcochong.com)
"""

from decimal import Decimal

class CoinHandler:

    _stored_coins = {}
    _inserted_coins = {}

    _no_change_solution = False

    def __init__(self):
        pass

    @property
    def supported_coins(self):
        coins = []
        for coin in self._stored_coins:
            coins.append(coin)
        coins.sort()
        return coins
    
    @property
    def stored_coins(self):
        return dict(self._stored_coins)
    
    @property
    def stored_coins_amount(self):
        stored_coins_amount = Decimal(str(0.0))
        for key in self._stored_coins:
            stored_coins_amount += key * self._stored_coins[key]
        return stored_coins_amount
    
    @property
    def inserted_coins(self):
        return dict(self._inserted_coins)
    
    @property
    def inserted_coins_amount(self):
        inserted_coins_amount = Decimal(str(0.0))
        for key in self._inserted_coins:
            inserted_coins_amount += key * self._inserted_coins[key]
        return inserted_coins_amount

    @property
    def total_coins(self):
        total_coins = dict(self._stored_coins)

        for coin in self._inserted_coins:
            total_coins[coin] += self._inserted_coins[coin]

        return total_coins

    def add_supported_coins(self, coin: Decimal):
        if coin not in self._stored_coins:
            self._stored_coins[coin] = 0
        
        if coin not in self._inserted_coins:
            self._inserted_coins[coin] = 0

    def clear_supported_coins(self):
        self._stored_coins = {}
        self._inserted_coins = {}

    def insert_coin(self, coin: Decimal, count = int):
        if count > 0:
            if coin in self._inserted_coins:
                self._inserted_coins[coin] += count
                return True
            else:
                return False
        else:
            return False
        
    def store_coin(self, coin: Decimal, count = int):
        if count > 0:
            if coin in self._stored_coins:
                self._stored_coins[coin] += count
                return True
            else:
                return False
        else:
            return False
        
    def return_inserted_coins(self):
        for coin in self._inserted_coins:
            self._inserted_coins[coin] = 0
        
    def store_inserted_coin(self):
        for coin in self._inserted_coins:
            self._stored_coins[coin] += self._inserted_coins[coin]
            self._inserted_coins[coin] = 0

    def resolve_change_coins_combination(self, amount: Decimal):

        # terminate if no change is needed
        if amount <= Decimal(str(0.0)):
            return []

        # the calculation is based on both stored and inserted coins
        coins_available = self.total_coins

        coin_list = []
        for coin_key in coins_available:
            if coin_key <= amount:
                for coin in range(0, coins_available[coin_key]):
                    coin_list.append(coin_key)
        coin_list.sort(reverse=True)

        # for detecting the cases without a solution
        self._no_change_solution = False
        
        # recursive function to find the best combination for change
        def search_combination(index, last_coin_used, last_amount_remain):

            if self._no_change_solution:
                return []

            coin_used = list(last_coin_used)

            amount_remain = last_amount_remain - coin_list[index]
            coin_used.append(coin_list[index])
 
            # print(coin_used)

            if amount_remain == 0:
                return coin_used
            
            if len(coin_used) == len(coin_list):
                self._no_change_solution = True
                return []
           
            if amount_remain < 0:
                return []
            
            i = index + 1
            while i < len(coin_list):
                result = search_combination(i, coin_used, amount_remain)
                if len(result) > 0:
                    return result
                i += 1

            if i >= len(coin_list):
                self._no_change_solution = True

            return []

        if coin_list:    
            return search_combination(0, [], amount)
        else:
            return []

    def change(self, change_coins_combination: list):
        # excluding the coins for change from the stored coins
        for coin in change_coins_combination:
            self._stored_coins[coin] -= 1
