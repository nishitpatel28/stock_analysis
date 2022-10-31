from typing import Dict, List, Tuple


class PortFolio:
    """
    Class for generating portfolio details.
    """
    def __init__(self, data: Dict, tickers: List, invest_amount: int):
        self.tickers = tickers
        self.invest_amount = invest_amount
        self.data = data
    
    def calculate_portfolio(self, ticker: str) -> Tuple[int, int, int, int]:
        """
        Method to calculate portfolio value.
        Input Parameters:
            ticker: Ticker Symbol
        Returns:
            Tuple containing following entities:
                profit -> Total profit
                per_profit -> Total profit in percentage
                purchased_value -> Value at the time of purchase (1 Year later)
                currenct_value -> Current value after 1 year.
        """
        temp_data = self.data[ticker]
        old_date = list(temp_data)[-1]
        old_price = temp_data[old_date]
        purchased_units = int(self.invest_amount / old_price)
        purchased_value = purchased_units * old_price
        profit, per_profit, current_value = self.calculate_difference(purchased_units, purchased_value, ticker)
        return (profit, per_profit, purchased_value, current_value)

    def calculate_difference(self, purchased_units: int, purchased_value: int, ticker: str) -> Tuple[int, int, int]:
        """
        Method to calculate difference between previous value and current value.
        Input Parameters:
            purchased_units: Units purchased 1 Year ago.
            purchased_value: Total value 1 Year ago.
            ticker: Ticker Symbol
        Returns:
            Tuple containing following entities:
                profit -> Total profit
                per_profit -> Total profit in percentage
                current_value -> Current value after 1 year.
        """
        temp_data = self.data[ticker]
        curr_date = list(temp_data)[0]
        curr_price = temp_data[curr_date]
        current_value = purchased_units * curr_price
        profit = current_value - purchased_value
        per_profit = ((current_value - purchased_value)/purchased_value) * 100
        return (profit, per_profit, current_value)
    
    def get_portfolio(self) -> None:
        """
        Method to get and print portfolio data in case where same amount
        is invested across all stocks.
        """
        for ticker in self.tickers:
            profit, per_profit, purchased_value, current_value = self.calculate_portfolio(ticker)
            print(f"\nData for {ticker} with investment amount of {self.invest_amount}")
            print(f"Previous Value (1-year): {purchased_value}")
            print(f"Current Value: {current_value}")
            print(f"Profit: {round(profit,4)}")
            print(f"Profit (%): {round(per_profit,2)}%")
            print("*"*30)
    
    def get_comb_portfolio(self) -> None:
        """
        Method to get and print portfolio data in case where equal amount
        is invested across all stocks.
        """
        self.invest_amount = int(self.invest_amount)/len(self.tickers)
        self.get_portfolio()