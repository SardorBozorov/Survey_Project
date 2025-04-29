import pandas as pd
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
import sys

class RandomGameApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the UI
        self.init_ui()

    def init_ui(self):
        # Create layout
        self.layout = QVBoxLayout()

        # Create a label to display the result
        self.result_label = QLabel("Click 'Pick a Winner' to start", self)
        self.layout.addWidget(self.result_label)

        # Create a button to pick the winner
        self.pick_winner_button = QPushButton('Pick a Winner', self)
        self.pick_winner_button.clicked.connect(self.pick_winner)
        self.layout.addWidget(self.pick_winner_button)

        # Create a button to load the CSV file
        self.load_file_button = QPushButton('Load Users Data', self)
        self.load_file_button.clicked.connect(self.load_file)
        self.layout.addWidget(self.load_file_button)

        # Set layout for the window
        self.setLayout(self.layout)

        # Initialize users_data
        self.users_data = None

        # Set window properties
        self.setWindowTitle('Random Game')
        self.setGeometry(100, 100, 300, 200)

    def load_file(self):
        # Open file dialog to select the CSV file
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        
        if file_path:
            try:
                # Attempt to read the CSV file with UTF-8 encoding
                self.users_data = pd.read_csv(
                r"users_data_combined_cleaned.csv",
                keep_default_na=False,
                encoding='utf-8',
                dtype={'☎️ Tel. raqamingiz:': str}  # Replace with your actual column name
                )

                self.result_label.setText(f"Loaded {len(self.users_data)} users data.")
            except UnicodeDecodeError:
                try:
                    # If UTF-8 fails, try reading with ISO-8859-1 encoding
                    self.users_data = pd.read_csv(file_path,  keep_default_na=False,  encoding='utf-8',dtype={'☎️ Tel. raqamingiz:': str} )
                    self.result_label.setText(f"Loaded {len(self.users_data)} users data with ISO-8859-1 encoding.")
                except Exception as e:
                    # Handle errors gracefully
                    self.result_label.setText(f"Error loading file: {e}")

    def pick_winner(self):
        if self.users_data is not None and len(self.users_data) > 0:
            # Randomly pick a winner from the loaded data
            winner = self.users_data.sample(1)
            winner_info = winner.iloc[0]

            winner_user_id = winner_info['user_id']  # Replace with the correct column name for user_id
            winner_name = winner_info['👤 Ism-familiyangiz:']
            winner_phone = winner_info['☎️ Tel. raqamingiz:']
            winner_email = winner_info['📩 Elektron pochtangiz:']

            # Check for null/empty values and display accordingly
            winner_details = f"User ID: {winner_user_id}\n"
            winner_details += f"Name: {self.clean_name(winner_name)}\n"
            
            if pd.notnull(winner_phone) and winner_phone != "":
                winner_details += f"Phone: {winner_phone}\n"
            if pd.notnull(winner_email) and winner_email != "":
                winner_details += f"Email: {winner_email}\n"
            
            self.result_label.setText(f"Winner:\n{winner_details}")
        else:
            self.result_label.setText("No data loaded!")

    def clean_name(self, name):
        """Capitalizes the name properly"""
        name = str(name).strip()
        return ' '.join(word.capitalize() for word in name.split())

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomGameApp()
    window.show()
    sys.exit(app.exec_())
