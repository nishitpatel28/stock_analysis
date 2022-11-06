from os import listdir
import random
from typing import List

from portfolio import PortFolio

existing = {}
i = 0


def random_set(target=100000, i=1):
    while True:
        rand_nums = random.sample(range(1, target), 5)
        if sum(rand_nums) == target:
            if rand_nums not in existing.values():
                existing.update({i: existing})
                i += 1
                return rand_nums

# Method to generate a random set summing to 1.
# (0.1, 0.3, 0.2, 0.3, 0.1)

# Method to calculate stock units and value in a set.
# 0.1*amount*stock_price

# track min and mix.


class TotalReturn:
    """
    Class to calculate best and worst overall return based on
    a combination of different amount generated randomly.
    """

    def __init__(self, invest_amount, tickers, data):
        self.invest_amount = invest_amount
        self.tickers = tickers
        self.data = data
        self.portfolio = PortFolio(data, self.tickers)
        self.counter = 0
        self.min, self.max = 0, 0
        self.min_values = []
        self.max_values = []
        self.existing_dict = {}

    def calculate_values(self, iteration: int = 5000) -> None:
        """
        Main method which calculates values, best overall return and
        worst overall return.
        Input Parameters:
            iteration: Number of iteration to generate random numbers.
        """
        while iteration != 0:
            rand_set = self.generate_random_set(
                len(self.tickers), self.invest_amount)
            self.get_stock_values(rand_set)
            iteration -= 1
        print('*'*40)
        print('-'*40)
        print("Best overall return within last year")
        print('-'*40)
        self.portfolio.get_custom_portfolio(self.max_values)
        print('-'*40)
        print("Worst overall return within last year")
        print('-'*40)
        self.portfolio.get_custom_portfolio(self.min_values)
        print('*'*40)

    def generate_random_set(self, num_tickers: int, target: int):
        """
        Method to generate a list of random numbers which represent
        amount invested in each stock.
        Get a random index and calculate a random number which is 
        in range from 0 to remaining amount(total). 
        Input Parameters:
            num_tickers: number of stock tickers
            target: Total amount to invest.
        """
        total = 0
        visited = {}
        while True:
            rand_index = random.randint(0, num_tickers)
            if rand_index not in visited:
                value = random.randint(0, target - total)
                total += value
                visited[rand_index] = value
            if len(visited) == num_tickers:
                break
        temp_list = [visited[keys] for keys in sorted(visited)]
        return temp_list

    def get_stock_values(self, rand_set: List) -> None:
        """
        Method to get portfolio of each set and then
        set the min and max class variables.
        Input Parameters:
            rand_set: Random list generated from generate random set
        """
        total_value = 0
        temp_dict = dict(zip(self.tickers, rand_set))
        for data in temp_dict:
            portfolio = self.portfolio.calculate_portfolio(
                ticker=data, amount=temp_dict[data]
            )
            total_value += portfolio[3]
        self.set_min_max(total_value, rand_set)

    def set_min_max(self, total_value: float, rand_set: list):
        """
        Method to set min and max values for class variables.
        Input Parameters:
            total_value: Total amount to invest.
            rand_set: Random list generated from generate random set
        """
        # Set Minimum
        if total_value < self.max and self.min and total_value < self.min:
            self.min = total_value
            self.min_values = rand_set
        elif not self.min:
            self.min = total_value
            self.min_values = rand_set
        # Set Maximum
        if total_value > self.max:
            self.max = total_value
            self.max_values = rand_set
