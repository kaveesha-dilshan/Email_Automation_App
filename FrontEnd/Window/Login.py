import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QDialog)
from PyQt6.QtCore import Qt
from Dashboard import DashboardWindow

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setFixedSize(350, 220)
        self.setStyleSheet("background-color: #00041f;")

        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        title = QLabel("Login")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(" font-size: 20px; font-weight: bold;")

        self.username = QLineEdit()
        self.resize(100,50)
        self.username.setStyleSheet("""
            QLineEdit {
                background-color: #1b1f3b;
                color: white;
                padding: 10px;
                border-redius: 6px;
                font-size: 14px;
            }
        """)
        self.username.setPlaceholderText("Enter your Email")

        self.password = QLineEdit()
        self.password.setStyleSheet("""
            QLineEdit {
                background-color: #1b1f3b;
                color: white;
                padding: 10px;
                border-redius: 6px;
                font-size: 14px;
            }
        """)
        self.password.setPlaceholderText("Enter your Email App Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_btn = QPushButton("Login to System")
        self.login_btn.setFixedSize(160, 40)
        self.login_btn.setStyleSheet("""
            QPushButton {
                background-color: #1E90FF;
                color: white;
                border-radius: 6px;
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #1873CC
            }
        """)

        self.login_btn.clicked.connect(self.handle_login)

        layout.addWidget(title)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_btn, alignment=Qt.AlignmentFlag.AlignHCenter)


    def handle_login(self):
        print(self.username.text(), self.password.text())
        self.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = LoginDialog()
    dlg.exec()
