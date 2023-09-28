
from requests import Session
from PyQt5 import QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel



##Subclass QWidget created to make slot functions to handle timout signal
class Window(QWidget):
    def __init__(self,parent=None):
        super(Window, self).__init__(parent)
        self.crypto = []
        self.graphs = []
        self.labels = []
        self.textbox = QLineEdit(self)
        self.button = QPushButton('SEARCH', self)
        layout.addWidget(self.textbox)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.add)
        self.x = 0
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000 * 5)
        self.timer.timeout.connect(self.plot, )
        self.timer.start()
    def add(self):
        slug = self.textbox.text()
        self.textbox.setText('')
        self.crypto.append(Crypto(slug))
        newGraph = PlotWidget()
        newGraph.setTitle(slug, color='orange', size="10pt")
        layout.addWidget(newGraph)
        self.graphs.append(newGraph)
        print(self.crypto[0].prices)
        newLabel = QLabel(f'{slug}: (price: {self.crypto[-1].prices[0]})')
        layout.addWidget(newLabel)
        self.labels.append(newLabel)
    def plot(self):
        for i in range(len(self.crypto)):
            
            self.crypto[i].x.append(self.x)
            pen = pg.mkPen(color=(0, 255, 0))
            self.crypto[i].getPrice()
            self.graphs[i].plot(self.crypto[i].x, self.crypto[i].prices, pen=pen)
            self.labels[i].text = f'{self.crypto[i].slug}: (price: {self.crypto[i].prices[-1]})'
            self.setLayout(layout)
            if len(self.graphs) > 0:
                self.x+=1
class Crypto:
    def __init__(self, slug):
        self.slug = slug
        self.x = []
        self.prices = []
        self.getPrice
    def getPrice (self): 
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = { 'slug': self.slug, 'convert': 'USD' } 

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '5439fc0f-cfda-4c0b-a06a-96323ddd906e',
        }
        session.headers.update(headers) 
        response = session.get(url, params=parameters) 
        price = response.json().get('data').get(list(response.json().get('data').keys())[0]).get('quote').get('USD').get('price')
        self.prices.append(price)




session = Session() 
layout = QVBoxLayout()
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()