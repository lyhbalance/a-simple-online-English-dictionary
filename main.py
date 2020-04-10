import sys
import main_window
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(window)

    window.show()

    sys.exit(app.exec_())
