
from requests import Session
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  
import os

def getPrice (): 

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = { 'slug': 'bitcoin', 'convert': 'USD' } 

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '5439fc0f-cfda-4c0b-a06a-96323ddd906e',
    }
    session = Session() 
    session.headers.update(headers) 
    response = session.get(url, params=parameters) 
    price = (response.json().get("data").get("1").get("quote").get("USD").get("price"))
    return price

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        # readData = open('data.txt', 'r')

        self.x = [1]
        self.y = [getPrice()]
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000 * 30)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        self.graphWidget.plot(self.x, self.y)
    def update_plot_data(self):
        self.x.append(self.x[-1] + 1) 
        self.y.append(getPrice())
        # writeData = open('data.txt', 'w').write(f"{}")
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

