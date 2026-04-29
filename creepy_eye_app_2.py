import sys
import os
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import (
    QApplication, QCheckBox, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Creepy Eye App")
        self.setFixedSize(350,260)
        # 1. Container and Layout
        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.setStyleSheet("background-color: black;")
     
        
        #button (toggle style)
        self.my_button = QPushButton("Want to See?")
        self.my_button.setCheckable(True)
        layout.addWidget(self.my_button)
        self.my_button.toggled.connect(self.button_toggled)
        self.my_button.setStyleSheet("background-color: grey; color: white;")
        
        
        # 3. Label for the GIF
        self.my_label = QLabel()
        self.my_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Load the GIF
        self.movie = QMovie("creepy_eye.gif") #url for eye gif: https://giphy.com/gifs/horror-dark-eye-n3UBd63oVlQLC
        self.my_label.setMovie(self.movie)
        
        # FIX: setFixedSize usage
        #self.my_label.setFixedSize(300, 200)
        
        # Start hidden
        self.my_label.setVisible(False)

        # 4. Add to layout
        layout.addWidget(self.my_button)
        layout.addWidget(self.my_label)

    #logic for button
    def button_toggled(self, Checked):
        if Checked:
            self.my_button.setText("Now You see me...")
            self.my_label.setVisible(True)
            self.movie.start()
        else:
            self.my_button.setText("Now You Dont...")
            self.my_label.setVisible(False)
            self.movie.stop()
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()