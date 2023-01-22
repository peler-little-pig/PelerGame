import sys
from PyQt5.QtWidgets import QApplication
from Extra.MapEditor.MainControl import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainControl()
    main_window.show()
    sys.exit(app.exec_())
