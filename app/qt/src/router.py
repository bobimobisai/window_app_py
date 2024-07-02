from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
)
import sys


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Multi-Page App")
        self.setGeometry(100, 100, 400, 300)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_page = QWidget()
        self.create_main_page()
        self.stacked_widget.addWidget(self.main_page)

        self.page_1 = QWidget()
        self.create_page_1()
        self.stacked_widget.addWidget(self.page_1)

        self.page_2 = QWidget()
        self.create_page_2()
        self.stacked_widget.addWidget(self.page_2)

        self.stacked_widget.setCurrentWidget(self.main_page)

    def create_main_page(self):
        layout = QVBoxLayout()

        btn_page_1 = QPushButton("Go to Page 1")
        btn_page_1.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.page_1)
        )
        layout.addWidget(btn_page_1)

        btn_page_2 = QPushButton("Go to Page 2")
        btn_page_2.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.page_2)
        )
        layout.addWidget(btn_page_2)

        self.main_page.setLayout(layout)

    def create_page_1(self):
        layout = QVBoxLayout()

        label = QLabel("This is Page 1")
        layout.addWidget(label)

        btn_back = QPushButton("Back to Home")
        btn_back.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.main_page)
        )
        layout.addWidget(btn_back)

        self.page_1.setLayout(layout)

    def create_page_2(self):
        layout = QVBoxLayout()

        label = QLabel("This is Page 2")
        layout.addWidget(label)

        btn_back = QPushButton("Back to Home")
        btn_back.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.main_page)
        )
        layout.addWidget(btn_back)

        self.page_2.setLayout(layout)
