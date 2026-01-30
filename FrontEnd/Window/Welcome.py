import sys
from PyQt6.QtCore import Qt 
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap 
from PyQt6.QtCore import Qt 
from Login import LoginDialog
from Dashboard import DashboardWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Email Automation System")
        self.setFixedSize(900,532)

        # ------ central widget -------
        central = QWidget()
        self.setCentralWidget(central)
        central.setStyleSheet("background-color: #00041f;")  # dark blue/black


        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)


        # -------------- LEFT SIDE ---------------

        # --------- welcome Image ---------
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.image_label.setContentsMargins(0, 0, 0, 0)

        pixmap = QPixmap("Assests/profile.png")
        scaled = pixmap.scaledToWidth(400, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled)

        left_layout.addWidget(self.image_label)



        # ------------------- RIGHT SIDE -------------------------
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        right_layout.setContentsMargins(25, 80, 0, 0)

        # create 3 containers
        content_layout = QVBoxLayout()
        content_layout.setSpacing(50)
        

         #  -------- HEDING ---------
        text_label = QLabel("Welcome to\nBulky\nEmail Automation System")
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setStyleSheet("""
            QLabel {
                font-size: 30px;
                font-weight: 600;
                color: white;
            }
        """)

        # --------- description -------------
        desc_label = QLabel(
            "Automate your email sending process efficiently and securely."\
            "This software processes email data locally and does not store or share user information." \
            "All emails, attachments, and credentials remain private and are used only for sending emails initiated by the user."
        )
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #AAAAAA;
            
            }
         """)
        
        # ----------- button ------------
        gt_btn = QPushButton("Get Started")
        gt_btn.clicked.connect(self.open_login)
        gt_btn.setFixedSize(160, 40)
        gt_btn.setStyleSheet("""
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

        

        # add widget to containers
        content_layout.addWidget(text_label)
        content_layout.addWidget(desc_label)
        content_layout.addSpacing(20)
        content_layout.addWidget(gt_btn, alignment=Qt.AlignmentFlag.AlignHCenter)   

        # add containers to right layout
        right_layout.addLayout(content_layout)
        right_layout.addStretch()

        layout.addWidget(left_widget)
        layout.addWidget(right_widget)

    def open_login(self):
        dlg = LoginDialog()
        if dlg.exec():
            self.close()
            self.dashboard = DashboardWindow()
            self.dashboard.show()



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()