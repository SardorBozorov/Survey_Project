import sys
import pandas as pd
import random
import time
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
    QFileDialog, QGraphicsOpacityEffect, QFrame
)
from PyQt5.QtCore import QTimer, Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QFont, QPalette, QColor, QMovie

class RandomGameApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('🎲 Random Winner Picker')
        self.setGeometry(500, 300, 600, 500)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#1e1e2f"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)

        self.result_label = QLabel("Click 'Pick a Winner' to start", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.result_label.setStyleSheet("color: white;")
        self.layout.addWidget(self.result_label)

        self.confetti_label = QLabel(self)
        self.confetti_label.setAlignment(Qt.AlignCenter)
        self.confetti_label.setVisible(False)
        self.layout.addWidget(self.confetti_label)

        self.load_file_button = QPushButton('📂 Load Users Data', self)
        self.load_file_button.setFont(QFont("Arial", 12))
        self.load_file_button.setStyleSheet("background-color: #6ca0dc; color: white; padding: 10px; border-radius: 8px;")
        self.load_file_button.clicked.connect(self.load_file)
        self.layout.addWidget(self.load_file_button)

        self.pick_winner_button = QPushButton('🎉 Pick a Winner', self)
        self.pick_winner_button.setFont(QFont("Arial", 12))
        self.pick_winner_button.setStyleSheet("background-color: #28a745; color: white; padding: 10px; border-radius: 8px;")
        self.pick_winner_button.clicked.connect(self.pick_winner)
        self.layout.addWidget(self.pick_winner_button)

        self.setLayout(self.layout)
        self.users_data = None
        self.animation = None

        # Setup confetti animation
        self.confetti_movie = QMovie("confetti.gif")  # Place a confetti.gif in your project directory
        self.confetti_label.setMovie(self.confetti_movie)

    def load_file(self):
        file_path = r"users_data_with_ids.csv"
        if file_path:
            try:
                self.users_data = pd.read_csv(file_path, encoding='utf-8', dtype={'☎️ Tel. raqamingiz:': str})
            except UnicodeDecodeError:
                self.users_data = pd.read_csv(file_path, encoding='ISO-8859-1', dtype={'☎️ Tel. raqamingiz:': str})

            self.result_label.setText(f"✅ Loaded {len(self.users_data)} users.")

    def pick_winner(self):
        if self.users_data is not None and len(self.users_data) > 0:
            self.result_label.setText("🔄 Picking a winner...")
            self.result_label.setStyleSheet("color: yellow;")
            QApplication.processEvents()

            for _ in range(30):
                temp_user = self.users_data.sample(1).iloc[0]
                temp_name = self.clean_name(temp_user['user_id'])
                self.result_label.setText(f"🎲 Rolling... {temp_name}")
                QApplication.processEvents()
                time.sleep(0.1)

            winner = self.users_data.sample(1).iloc[0]
            winner_user_id = winner['user_id']
            winner_name = self.clean_name(winner['👤 Ism-familiyangiz:'])
            winner_phone = winner['☎️ Tel. raqamingiz:']
            winner_email = winner['📩 Elektron pochtangiz:']

            winner_details = f"🎉 <b>Winner</b> 🎉<br><br>"
            winner_details += f"<b>User ID:</b> {winner_user_id}<br>"
            winner_details += f"<b>Name:</b> {winner_name}<br>"
            if pd.notnull(winner_phone) and winner_phone != "":
                winner_details += f"<b>Phone:</b> {winner_phone}<br>"
            if pd.notnull(winner_email) and winner_email != "":
                winner_details += f"<b>Email:</b> {winner_email}<br>"

            self.result_label.setTextFormat(Qt.RichText)
            self.result_label.setText(winner_details)
            self.result_label.setStyleSheet("color: #00ffcc;")

            # Play confetti animation
            self.confetti_label.setVisible(True)
            self.confetti_movie.start()

            # Fade in effect
            opacity_effect = QGraphicsOpacityEffect()
            self.result_label.setGraphicsEffect(opacity_effect)
            animation = QPropertyAnimation(opacity_effect, b"opacity")
            animation.setDuration(1200)
            animation.setStartValue(0)
            animation.setEndValue(1)
            animation.setEasingCurve(QEasingCurve.OutBounce)
            animation.start()
            self.animation = animation

            # Stop confetti after a delay
            QTimer.singleShot(4000, self.stop_confetti)
        else:
            self.result_label.setText("⚠️ No data loaded!")

    def stop_confetti(self):
        self.confetti_movie.stop()
        self.confetti_label.setVisible(False)

    def clean_name(self, name):
        name = str(name).strip()
        return ' '.join(word.capitalize() for word in name.split())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomGameApp()
    window.show()
    sys.exit(app.exec_())
