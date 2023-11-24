import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QMessageBox,
)
from PyQt5.QtGui import QPixmap, QFont, QPainter, QColor
from PyQt5.QtCore import pyqtSignal, Qt


class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()


class LoginApp(QWidget):
    login_success_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(200, 200, 512, 512)  # Set the window size
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()

        # Create a vertical layout for the login section
        login_layout = QVBoxLayout()

        # Add widgets to the login section
        self.username_label = QLabel("Username:")
        self.setup_label(self.username_label)

        self.username_entry = QLineEdit(self)
        self.setup_entry(self.username_entry)

        self.password_label = QLabel("Pas2sword:")
        self.setup_label(self.password_label)

        self.password_entry = QLineEdit(self)
        self.setup_entry(self.password_entry)
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.setup_button(self.login_button)
        self.login_button.clicked.connect(self.login)

        login_layout.addWidget(self.username_label)
        login_layout.addWidget(self.username_entry)
        login_layout.addSpacing(20)  # Increase spacing to move "Username" label lower
        login_layout.addWidget(self.password_label)
        login_layout.addWidget(self.password_entry)
        login_layout.addSpacing(10)  # Add some spacing
        login_layout.addWidget(self.login_button, alignment=Qt.AlignRight)

        # Create a transparent widget to hold the login section
        login_widget = QWidget(self)
        self.setup_widget(login_widget)
        login_widget.setLayout(login_layout)

        # Set the width of the login section
        login_widget.setFixedWidth(300)

        # Set the stretch factor for the login section to push it to the left
        main_layout.addWidget(login_widget)

        # Set background image using ClickableLabel
        background_label = ClickableLabel(self)
        background_label.clicked.connect(self.background_clicked)
        pixmap = QPixmap("Bgimage.png")
        pixmap = pixmap.scaled(self.size())  # Scale the image to the window size
        background_label.setPixmap(pixmap)

        main_layout.addWidget(background_label)

        self.setLayout(main_layout)

        # Add "Sign In with Face" button to the top right corner
        face_sign_in_button = QPushButton("Sign In with Face", self)
        self.setup_button(face_sign_in_button)
        face_sign_in_button.clicked.connect(self.sign_in_with_face)
        face_sign_in_button.setGeometry(
            20,
            20,
            face_sign_in_button.sizeHint().width(),
            40,
        )

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw a semi-transparent overlay on top of the background
        overlay_color = QColor(0, 0, 0, 150)
        painter.fillRect(self.rect(), overlay_color)

    def setup_label(self, label):
        label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        label.setStyleSheet("color: white;")

    def setup_entry(self, entry):
        entry.setFont(QFont("Segoe UI", 12))
        entry.setStyleSheet(
            "background-color: transparent; border: 1px solid white; color: white; padding: 5px;"
        )

    def setup_button(self, button):
        button.setStyleSheet(
            "background-color: #007ACC; color: white; border: 2px solid #005F91; border-radius: 5px; padding: 8px;"
        )

    def setup_widget(self, widget):
        widget.setStyleSheet(
            "background-color: #1E1E1E; border: 1px solid #333333; border-radius: 5px; padding: 15px;"
        )

    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        if not username or not password:
            self.show_message(
                "Error", "Please fill out both username and password boxes."
            )
            return

        if (username == "Nelson" and password == "CreoAI") or (
            (username == "Bruce" and password == "2KualaLumpur")
        ):
            self.show_message("Login Successful", f"Welcome, {username}")
            self.login_success_signal.emit()  # Emit the login success signal
        else:
            self.show_message(
                "Login Failed", "Incorrect username or password. Please try again."
            )

    def background_clicked(self):
        pass

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def sign_in_with_face(self):
        msg = QMessageBox()
        msg.setWindowTitle("Face Sign In")
        msg.setText("Face recognition feature is not implemented yet.")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()
    sys.exit(app.exec_())
