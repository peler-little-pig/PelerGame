from Extra.MapEditor.MainWindow import *
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QUrl, QDir, QFileInfo, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent


class MainControl(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainControl, self).__init__(parent)
        self.setupUi(self)

        self.init_ui()
        self.init_icon()
        self.event_connect()

    def init_ui(self):
        ...

    def init_icon(self):
        ...

    def event_connect(self):
        ...