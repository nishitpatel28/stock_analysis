from base_class import BaseClass
from plot_data import PlotData
from portfolio import PortFolio
from stock_data import StockData

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
        pf = PortFolio(data, tickers, amount)
        pf.get_portfolio()
        pf.get_comb_portfolio()
        plot_data = PlotData(data, tickers)
        plot_data.generate_graphs()

if __name__ == "__main__":
    ABC().run()