from base_class import BaseClass
from plot_data import PlotData
from portfolio import PortFolio
from stock_data import StockData
from total_return import TotalReturn

class ABC:
    """
    Main runner class.
    """
    def run(self):
        """
        Main method to run stock_analysis program.
        """
        baseclass = BaseClass()
        tickers = baseclass.tickers
        amount = baseclass.investment_amount
        stock_data = StockData(tickers)
        data = stock_data.get_data()
        pf = PortFolio(data, tickers)
        pf.get_sep_portfolio(amount)
        pf.get_comb_portfolio(amount)
        total_return = TotalReturn(amount, tickers, data)
        if amount > 5:
            total_return.calculate_values(5000)
        plot_data = PlotData(data, tickers)
        plot_data.generate_graphs()

if __name__ == "__main__":
    ABC().run()