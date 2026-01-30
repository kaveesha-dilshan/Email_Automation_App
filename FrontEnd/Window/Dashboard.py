from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
import sys

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.resize(900,600)

        #=============== central widget =================
        central = QWidget()
        self.setCentralWidget(central)
        central.setStyleSheet("background-color: #00041f;")

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)


        # =================== Left Side ====================
        # ==================================================
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        left_layout.setContentsMargins(25, 80, 0, 0)

        # create 3 containers
        content_layout = QVBoxLayout()
        content_layout.setSpacing(50)
        

         #  -------- HEDING ---------
        text_label = QLabel("One-Time\nEmail Sending")
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
            "One-Time Email Sending Automation is a tool that allows users to send a single email quickly and securely without repeating the same steps every time." \
            "The user enters their email credentials once, writes the message, adds an optional attachment, and sends the email with a single click." \
            "This automation saves time, reduces manual effort, and ensures accurate email delivery using a simple and user-friendly interface."
        )
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #AAAAAA;
            
            }
         """)
        
        # ----------- button ------------
        gt_btn = QPushButton("One-Time Sending")
        # gt_btn.clicked.connect()
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

        # add widgets to container
        content_layout.addWidget(text_label)
        content_layout.addWidget(desc_label)
        content_layout.addWidget(gt_btn,alignment=Qt.AlignmentFlag.AlignHCenter)

        # add containers to left 
        left_layout.addLayout(content_layout)
        left_layout.addStretch()


        # ================= RIGHT SIDE =====================
        # ==================================================       

        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        right_layout.setContentsMargins(25, 80, 0, 0)

        # create 3 containers
        content_layout = QVBoxLayout()
        content_layout.setSpacing(50)
        

         #  -------- HEDING ---------
        text_label = QLabel("Bulk \nEmail sending")
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
            "Bulk Email Sending Automation allows users to send the same email to multiple recipients at once using a single action.Email addresses are loaded from a file (such as CSV or Excel), and the system automatically sends emails to each recipient without manual repetition.This saves time, reduces errors, and makes email communication faster and more efficient" 
        )
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #AAAAAA;
            
            }
         """)
        
        # ----------- button ------------
        gt_btn = QPushButton("Bulk sending")
        # gt_btn.clicked.connect()
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

        # add widgets to container
        content_layout.addWidget(text_label)
        content_layout.addWidget(desc_label)
        content_layout.addWidget(gt_btn,alignment=Qt.AlignmentFlag.AlignCenter)

        # add containers to right 
        right_layout.addLayout(content_layout)
        right_layout.addStretch()


        #  ============= add all to central widget ==================
        layout.addWidget(left_widget)
        layout.addWidget(right_widget)
        



def main():
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()