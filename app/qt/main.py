from PyQt5.QtWidgets import QApplication
from src.router import MyApp
import sys


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
