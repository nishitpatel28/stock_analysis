import re

COMMA = ","


class BaseClass:
    """
    Base Class for taking user input and initializing variables.
    """
    def __init__(self) -> None:
        self.tickers = []
        self.investment_amount = 0
        self._get_user_inputs()
    
    def _get_user_inputs(self) -> None:
        """
        Method to retrieve user inputs like stock tickers and investment amount.
        Valid ticker symbols should be provided and should be space seperated.
        If More than 5 symbols are provided, data will be generated for
        only first 5 symbols. Investment amount will be parsed to ignore special
        characters such as ',' and currency symbols.
        """

        tickers = input("Enter stock tickers seperated by whitespace: ")
        self.tickers = tickers.split(" ")
        if len(self.tickers) > 5:
            self.tickers = self.tickers[:5]
            print("Showing data for first 5 tickers provided.")
        amount = input("Enter Investment Amount: ")
        self.investment_amount = self._parse_amount(amount)

    def _parse_amount(self, amount: str) -> int:
        """
        Method to parse investment amount and removes special characters and
        currency symbols.
        Input Parameters:
            amount: Investment amount taken from user input.
        Returns:
            Parsed investment amount converted to int.

        Example:
            Input: "100,000 USD"
            Returns: 100000
        """
        pattern = "([0-9]+,*[0-9]*)"
        match = re.search(pattern, amount)
        if match:
            str_amount = match.group(1)
            int_amount = int(str_amount.replace(COMMA, "")) if COMMA in str_amount else int(str_amount)
            return int_amount
        else:
            print("Invalid investment amount entered. Try Again.")
