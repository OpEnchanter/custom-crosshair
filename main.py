import sys, json
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor

config = {}

with open("conf.json", "r") as configFile:
    config = json.load(configFile)


class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(config["screenx"]-int(config["size"]/2), config["screeny"]-int(config["size"]/2), config["size"], config["size"])

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(config["r"], config["g"], config["b"], config["a"]))  # Semi-transparent red
        painter.drawEllipse(0, 0, config["size"], config["size"])

app = QApplication(sys.argv)
window = TransparentWindow()

window.show()
sys.exit(app.exec_())