import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QGridLayout)
from PyQt5.QtCore import QObject, pyqtSlot
import subprocess


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # create the input fields
        self.ip_address_field = QLineEdit()
        self.ip_address_field.setPlaceholderText("Enter IP address")
        self.ping_count_field = QLineEdit()
        self.ping_count_field.setPlaceholderText("Enter ping count")

        # create the start button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.on_start_clicked)

        # create the ping results label
        self.ping_results_label = QLabel("Press the Start button to begin pinging")

        # create a grid layout and add the widgets
        layout = QGridLayout()
        layout.addWidget(QLabel("IP address:"), 0, 0)
        layout.addWidget(self.ip_address_field, 0, 1)
        layout.addWidget(QLabel("Ping count:"), 1, 0)
        layout.addWidget(self.ping_count_field, 1, 1)
        layout.addWidget(self.start_button, 2, 0, 1, 2)
        layout.addWidget(self.ping_results_label, 3, 0, 1, 2)
        self.setLayout(layout)

        # set the window title and show the window
        self.setWindowTitle("Ping Tool")
        self.show()

    @pyqtSlot()
    def on_start_clicked(self):
        # get the IP address and ping count from the input fields
        ip_address = self.ip_address_field.text()
        ping_count = self.ping_count_field.text()

        # use the subprocess module to run the "ping" command
        # and capture the output
        try:
            output = subprocess.check_output(
                ["ping", "-c", ping_count, ip_address],
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
        except subprocess.CalledProcessError as e:
            output = e.output

        # display the output in the ping results label
        self.ping_results_label.setText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
