import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QVBoxLayout, QComboBox)
from PySide6.QtCore import Slot  
from __feature__ import snake_case, true_property
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import numpy

def patch_asscalar(a):
  return a.item()
setattr(numpy, "asscalar", patch_asscalar)

#Task 1

# app = QApplication([])

class ButtonOne(QWidget):
  def __init__(self):
      super().__init__()
      vbox = QVBoxLayout()

      my_btn = QPushButton('button 1')
      my_btn2 = QPushButton('button 2')
      self.my_lbl = QLabel('button not yet clicked')

      my_btn.clicked.connect(self.on_click)
      my_btn2.clicked.connect(self.on_click2)

      vbox.add_widget(self.my_lbl)
      vbox.add_widget(my_btn)
      vbox.add_widget(my_btn2)

      self.set_layout(vbox)
      self.resize(400, 400)
      self.show()

  @Slot()
  def on_click(self):
      self.my_lbl.text = 'button 1 has been clicked!'
    
  @Slot()
  def on_click2(self):
      self.my_lbl.text = 'button 2 has been clicked!'

# btn_win = ButtonOne()
# sys.exit(app.exec())

#Task 2

# app2 = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.colorDictionary = {
            "Pick a color":"",
            "Red": "RGB: (255, 0, 0)    Hex: #FF0000",
            "Green": "RGB: (0, 255, 0)    Hex: #00FF00",
            "Blue": "RGB: (0, 0, 255)    Hex: #0000FF"
        }

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.colorDictionary)
        self.my_label = QLabel("")

        vbox = QVBoxLayout()
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_label)

        self.set_layout(vbox)
        self.resize(400, 400)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

    @Slot()
    def update_ui(self):
        my_text = self.my_combo_box.current_text
        my_index = self.my_combo_box.current_index
        if my_text == 'Pick a color':
            self.my_label.text = ''
        else:
            self.my_label.text = f'{self.colorDictionary[my_text]}.'

# my_win = MyWindow()
# my_win.show()
# sys.exit(app2.exec())

#Task 3
class ColorExchange(QWidget):
    def __init__(self):
        super().__init__()

        self.colorDictionary = {
            "Pick a color": None,
            "Red":   {"rgb": (255, 0, 0),   "hex": "#FF0000"},
            "Green": {"rgb": (0, 255, 0),   "hex": "#00FF00"},
            "Blue":  {"rgb": (0, 0, 255),   "hex": "#0000FF"},
        }

        self.combo = QComboBox()
        self.combo.add_items(list(self.colorDictionary.keys()))

        self.rgb_label = QLabel("")
        self.hex_label = QLabel("")
        self.lab_label = QLabel("")

        vbox = QVBoxLayout()
        vbox.add_widget(self.combo)
        vbox.add_widget(self.rgb_label)
        vbox.add_widget(self.hex_label)
        vbox.add_widget(self.lab_label)

        self.set_layout(vbox)
        self.resize(400, 400)

        self.combo.currentIndexChanged.connect(self.update_ui)

    def rgb_to_lab(self, rgb_255):
        r, g, b = rgb_255

        #creates a colormath color object
        srgb = sRGBColor(r, g, b, is_upscaled=True)

        # Convert to Lab
        lab = convert_color(srgb, LabColor)
        return lab.lab_l, lab.lab_a, lab.lab_b

    @Slot(int)
    def update_ui(self, index):
        color_name = self.combo.current_text

        if color_name == "Pick a color":
            self.rgb_label.text = ""
            self.hex_label.text = ""
            self.lab_label.text = ""
            return

        data = self.colorDictionary[color_name]
        rgb = data["rgb"]
        hx = data["hex"]

        L, a, b = self.rgb_to_lab(rgb)

        self.rgb_label.text = f"RGB: {rgb}"
        self.hex_label.text = f"Hex: {hx}"
        self.lab_label.text = f"CIELAB:  L*={L:.2f}   a*={a:.2f}   b*={b:.2f}"

app3 = QApplication([])
win = ColorExchange()
win.show()
sys.exit(app3.exec())