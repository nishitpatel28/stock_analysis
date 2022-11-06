from typing import Dict, List, Tuple


class PortFolio:
    """
    Class for generating portfolio details.
    """
    def __init__(self, data: Dict, tickers: List):
        self.tickers = tickers
        self.data = data
    
    def calculate_portfolio(self, ticker: str, amount: int) -> Tuple[int, int, int, int]:
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
        if amount < old_price:
            return(0, 0, 0, 0)
        purchased_units = int(amount / old_price)
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
        current_value = round(purchased_units * curr_price,4)
        profit = current_value - purchased_value
        per_profit = ((current_value - purchased_value)/purchased_value) * 100
        return (profit, per_profit, current_value)
    
    def get_portfolio(self, ticker, amount) -> None:
        """
        Method to get and print portfolio data based on amount invested
        in a specific stock.
        """
        profit, per_profit, purchased_value, current_value = self.calculate_portfolio(ticker, amount)
        print(f"\nData for {ticker} with investment amount of {amount}")
        print(f"Previous Value (1-year): {purchased_value}")
        print(f"Current Value: {current_value}")
        print(f"Profit: {round(profit,4)}")
        print(f"Profit (%): {round(per_profit,2)}%")
    
    def get_comb_portfolio(self, invest_amount: int) -> None:
        """
        Method to get and print portfolio data in case where equally
        divided amount is invested across all stocks.
        """
        print(f"Portfolio if ${invest_amount} was evenly invested:")
        print('-'*40)
        amount = int(invest_amount)/len(self.tickers)
        for ticker in self.tickers:
            self.get_portfolio(ticker, amount)
        print('-'*40)

    def get_sep_portfolio(self, invest_amount: int) -> None:
        """
        Method to get portfolio if same amount is invested across
        each stock.
        """
        print(f"Portfolio if {invest_amount} was invested in each stock:")
        print('-'*40)
        for ticker in self.tickers:
            self.get_portfolio(ticker, invest_amount)
        print('-'*40)
    
    def get_custom_portfolio(self, amounts: List) -> None:
        """
        Method to get portfolio for a custom amount invested 
        for a selected stock.
        """
        temp_dict = dict(zip(self.tickers, amounts))
        for data in temp_dict:
            self.get_portfolio(ticker=data, amount=temp_dict[data])