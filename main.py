
from requests import Session
from PyQt5 import QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  
# import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import time



# def getPrice (crypto): 

#     url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
#     parameters = { 'slug': crypto, 'convert': 'USD' } 

#     headers = {
#         'Accepts': 'application/json',
#         'X-CMC_PRO_API_KEY': '5439fc0f-cfda-4c0b-a06a-96323ddd906e',
#     }
#     session = Session() 
#     session.headers.update(headers) 
#     response = session.get(url, params=parameters) 
#     price = (response.json().get("data").get("1").get("quote").get("USD").get("price"))
#     return price

# class MainWindow(QtWidgets.QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#         self.graphWidget = pg.PlotWidget()
#         self.setCentralWidget(self.graphWidget)
        

#         self.x = [1]
#         self.y = [getPrice()]
#         self.timer = QtCore.QTimer()
#         self.timer.setInterval(1000 * 60)
#         self.timer.timeout.connect(self.update_plot_data)
#         self.timer.start()

#         self.graphWidget.plot(self.x, self.y)
#     def update_plot_data(self):
#         self.x.append(self.x[-1] + 1) 
#         self.y.append(getPrice())
#         # writeData = open('data.txt', 'w').write(f"{}")
#         pen = pg.mkPen(color=(0, 255, 0))
#         self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
        


# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     main = MainWindow()
#     main.show()
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()

class Window(QWidget):
    def __init__(self,parent=None):
        super(Window, self).__init__(parent)
        self.graphs = []
        self.layout = QVBoxLayout()
        self.layout.addWidget()
        self.setLayout(self.layout)
        self.x = [0]
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000 * 60)
        self.timer.timeout.connect(self.plot)
        self.timer.start()
    def createGraph(self):
        self.graphs.append(Graph())
    def plot(self):
        for graph in self.graphs:
            graph.getPrice()
            # graph.plot(self.x, graph.prices)
            

class Graph(pg.plotWidget()):
    def __init__(self, crypto):
        super(Graph, self).__init__(crypto)
        self.crypto = crypto
        self.prices = []
    def getPrice (self): 
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = { 'slug': self.crypto, 'convert': 'USD' } 

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '5439fc0f-cfda-4c0b-a06a-96323ddd906e',
        }
        session = Session() 
        session.headers.update(headers) 
        response = session.get(url, params=parameters) 
        price = (response.json().get("data").get("1").get("quote").get("USD").get("price"))
        self.prices.append(price)


# app = QApplication([])
# window = Window(sys.argv)
# layout = QVBoxLayout()
# graphWidget = pg.PlotWidget()
# pen = pg.mkPen(color=(0, 255, 0))
# graphWidget.plot(x, y, pen=pen)
# layout.addWidget(graphWidget)
# window.setLayout(layout)
# window.show()
# app.exec()



