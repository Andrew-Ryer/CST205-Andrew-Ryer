"""
Name: Andrew Ryer
Class: CST 205
Date: 3-13-2026
Homework 3 - GUI will contain at least the following widgets: QLineEdit, QComboBox, and QPushButton.
"""
from pathlib import Path

import sys

from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDialog, QTextBrowser)

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt

from __feature__ import snake_case, true_property

from hw3Functions import my_search, image_path_from_id, apply_manipulation

# Referenced: display_image.py, drop.py, line_edit.py

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Dropdown list
        self.my_list = ["None", "Sepia", "Negative", "Grayscale", "Thumbnail"]

        self.current_image = "no_results.jpg"

        # Create dropdown
        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_label = QLabel("")

        # Create vertical layout
        vbox = QVBoxLayout()
        
        # Create line editor
        self.my_le = QLineEdit("Example search terms to test: “village”, “vessel”, “salt”, “airport”, “bridge”, ect.")
        self.my_le.minimum_width = 500
        self.my_le.select_all()

        # Create button to submit the line editer text
        my_btn = QPushButton("Search")
        self.status_label = QLabel('')
        # Label for image
        self.image_label = QLabel()
        self.image_label.alignment = Qt.AlignCenter
        # Conect Button
        my_btn.clicked.connect(self.on_submit)
        self.my_le.returnPressed.connect(self.on_submit)

        # add dropdown to vertical
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_label)

        # add dropdown response to vertical
        self.set_layout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

        # add line editor to vertical
        vbox.add_widget(self.my_le)
        vbox.add_widget(my_btn)
        vbox.add_widget(self.status_label)
        vbox.add_widget(self.image_label)
        self.resize(600, 600)

        self.set_layout(vbox)
        # Show image
        self.show_image(self.current_image)

    # Function to show the image
    def show_image(self, image_file):
        my_pixmap = QPixmap(image_file)
        my_pixmap = my_pixmap.scaled(500, 500, Qt.KeepAspectRatio)
        self.image_label.pixmap = my_pixmap

    # Connect response for the Line editor (make this display the correct image)
    @Slot()
    def on_submit(self):
        search_term = self.my_le.text.strip()
        image_id = my_search(search_term)
        self.current_image = image_path_from_id(image_id)

        selected_filter = self.my_combo_box.current_text
        display_image = apply_manipulation(self.current_image, selected_filter)

        if image_id == "no results":
            self.status_label.text = "No results found."
        else:
            self.status_label.text = f'Result for "{search_term}"'

        self.show_image(display_image)

    # Connect response for the dropdown (make this apply correct filter to image)
    @Slot()
    def update_ui(self):
        selected_filter = self.my_combo_box.current_text
        display_image = apply_manipulation(self.current_image, selected_filter)
        self.show_image(display_image)


app = QApplication([])
my_win = MyWindow()
my_win.show()
sys.exit(app.exec())