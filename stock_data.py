from typing import Dict, List
import requests


API_KEY = "1UT88AMAZLFR2NT9"
FUNCTION = "TIME_SERIES_DAILY"
BASE_URL = "https://www.alphavantage.co/query?"


class StockData:
    """
    Class to collect data related to requested stock from AlphaVantage API.
    """
    def __init__(self, tickers: List):
        self.tickers = tickers

    def get_data(self) -> Dict:
        """
        Method to retreive and parse data returned from API.
        returns:
            Data in dictionary form.
        Example:
            {
                'AAPL': {*stock data for AAPL*},
                'IBM': {*stock data for IBM*}
            }
        """
        stock_data = {}
        for ticker in self.tickers:
            data = self.send_request(ticker)
            parsed_data = self.parse_data(data)
            stock_data.update({ticker.upper(): parsed_data})
        return stock_data

    def send_request(self, ticker: str) -> Dict:
        """
        Method to collect data from API for the requested ticker.
        Input Parameters:
            ticker: Ticker Symbol.
        returns:
            Dict containing raw json data from API.
        """
        params = f"function={FUNCTION}&symbol={ticker.upper()}&apikey={API_KEY}&outputsize=full"
        url = f"{BASE_URL}"+params
        try:
            request = requests.get(url=url)
            data = request.json()
            return data
        except Exception as exc:
            print(f"Failed to get data from API due to:\n{exc}")

    def parse_data(self, data: Dict) -> Dict[str, float]:
        """
        Method to parse raw json data from API. 'Time Series (Daily)' data
        is filtered and entries are limited to 365 (to indicate full year) and 
        in case for newly registed entity all entries are considered.

        Input Parameters:
            data: data is dict form which is retrieved from API.
        Returns:
            return dict containing date and closing price for that specific date.
        """
        data_dict = {}
        daily_data = data["Time Series (Daily)"]
        if len(list(daily_data.items())) >= 365:
            filtered_data = list(daily_data.items())[:365]
        else:
            filtered_data = list(daily_data.items())[-1]
        for items in filtered_data:
            date = items[0]
            closing_price = float(items[1]["4. close"])
            data_dict.update({date: closing_price})
        
        return data_dict