from typing import Dict, List
import matplotlib.pyplot as plt

HEIGHT = 2
WIDTH = 2


class PlotData:
    """
    Class for plotting data to graph imported from matplotlib.
    """
    def __init__(self, data: Dict, ticker: List) -> None:
        self.data = data
        self.tickers = ticker
        self._initialize_graph()
    
    def _initialize_graph(self):
        axis = int(len(self.tickers)) + 1
        self.fig, self.axis = plt.subplots(axis)
        self.fig.tight_layout()
        self.fig.suptitle("Stock Data for 1 Year")

    def generate_graphs(self) -> None:
        """
        Main method to plot graphs.
        """
        inst = 0
        for ticker in self.tickers:
            self.plot_graphs(inst, ticker=ticker)
            inst +=1
        # Generate Combined Graph
        self.plot_multi_lines(inst)
        plt.show()

    def plot_graphs(self, inst: int, ticker: str) -> None:
        """
        Method to plot individual graphs for each ticker.
        Input Parameters:
            inst: Instance of ticker.
            ticker: Ticker symbol
        """
        temp_data = self.data[ticker]
        x_values = []
        y_values = []
        for key, value in temp_data.items():
            x_values.append(key)
            y_values.append(value)
        self.axis[inst].set_title(ticker)
        self.axis[inst].plot(x_values[::-1], y_values[::-1])
  
    def plot_multi_lines(self, inst: int) -> None:
        """
        Method to plot combined graph for each ticker
        Input Parameters:
            inst: Instance of ticker.
        """
        for ticker in self.data.items():
            label = ticker[0]
            x_values = []
            y_values = []
            for key, value in ticker[1].items():
                x_values.append(key)
                y_values.append(value)
            self.axis[inst].plot(x_values[::-1], y_values[::-1], label = label)
        self.axis[inst].legend(loc='upper right')
        self.axis[inst].set_title("Combined Graph")