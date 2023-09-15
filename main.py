
from requests import Session
from PyQt5 import QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit

class Window(QWidget):
    def __init__(self,parent=None):
        super(Window, self).__init__(parent)
        self.graphs = []
        self.textbox = QLineEdit(self)
        self.button = QPushButton('SEARCH', self)
        layout.addWidget(self.textbox)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.createGraph)
        self.x = [0]
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000 * 5)
        self.timer.timeout.connect(self.plot)
        self.timer.start()
    def createGraph(self):
        currency = self.textbox.text()
        self.graphs.append(Graph(currency))
    def plot(self):
        for graph in self.graphs:
            pen = pg.mkPen(color=(0, 255, 0))
            graph.getPrice()
            graph.plot(self.x, graph.prices, pen=pen)
            self.setLayout(layout)
        self.x.append(self.x[-1] + 1)

            
            

class Graph(PlotWidget):
    def __init__(self, crypto):
        super(Graph, self).__init__()
        self.crypto = crypto
        self.prices = []
        layout.addWidget(self)
        self.getPrice
    def getPrice (self): 
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = { 'slug': self.crypto, 'convert': 'USD' } 

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '5439fc0f-cfda-4c0b-a06a-96323ddd906e',
        }
        session.headers.update(headers) 
        response = session.get(url, params=parameters) 
        price = (response.json().get("data").get("1").get("quote").get("USD").get("price"))
        self.prices.append(price)

session = Session() 
layout = QVBoxLayout()
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
