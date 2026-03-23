#Task 1

import sys

from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDialog, QTextBrowser)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property


#my_qt_app = QApplication([])

class ColorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_title = 'Background'
        self.palette = Qt.darkMagenta

class ColorWindow2(QWidget):
    def __init__(self):
        super().__init__()

        self.window_title = 'Background'
        self.palette = Qt.cyan

'''
my_window = ColorWindow()
my_window.move(0,0)
my_window.show()

my_window2 = ColorWindow2()
my_window2.move(700,0)
my_window2.show()

sys.exit(my_qt_app.exec())
'''

#task 2
#app = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        h_layout = QHBoxLayout()
        b1 = QPushButton("A")
        b2 = QPushButton("B")

        h_layout.add_widget(b1)
        h_layout.add_widget(b2)

        v_layout = QVBoxLayout()
        b4 = QPushButton("D")
        b5 = QPushButton("E")

        v_layout.add_widget(b4)
        v_layout.add_widget(b5)

        v_layout2 = QVBoxLayout()

        b6 = QPushButton("F")
        b7 = QPushButton("G")

        v_layout.add_widget(b6)
        v_layout.add_widget(b7)

        main_layout = QHBoxLayout()

        main_layout.add_layout(v_layout2)
        main_layout.add_layout(h_layout)
        main_layout.add_layout(v_layout)
        self.set_layout(main_layout)

'''
a = MyWindow()
a.show()
sys.exit(app.exec())
'''

#Task 3
#app = QApplication([])

my_list = ['RED', 'GREEN', 'BLUE']

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.combo = QComboBox()
    self.combo.add_items(my_list)
    btn = QPushButton('CLICK ME')
    vbox = QVBoxLayout()
    vbox.add_widget(self.combo)
    vbox.add_widget(btn)
    self.set_layout(vbox)
    btn.clicked.connect(self.open_win)

  @Slot() 
  def open_win(self):
    color_name = self.combo.current_text
    self.new_win = ColorWindow(color_name)
    self.new_win.show()

class ColorWindow(QWidget):
  def __init__(self, color_name: str):
    super().__init__()

    self.window_title = f"Color: {color_name}"

    # Convert "RED" -> Qt.red
    qt_color = getattr(Qt, color_name.lower(), Qt.white)

    self.palette = qt_color

    label = QLabel(f"Selected: {color_name}")
    label.alignment = Qt.AlignCenter

    self.layout = QVBoxLayout()
    self.layout.add_widget(label)
    self.set_layout(self.layout)

'''
main = MyWindow()
main.show()
sys.exit(app.exec())
'''

#Task 4
# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from pathlib import Path
import sys
from PySide6.QtCore import QObject, Property, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView

from __feature__ import snake_case, true_property

# This example illustrates exposing a list of QObjects as a model in QML
class DataObject(QObject):

    nameChanged = Signal()
    colorChanged = Signal()

    def __init__(self, name, color, parent=None):
        super().__init__(parent)
        self._name = name
        self._color = color

    def name(self):
        return self._name

    def set_name(self, name):
        if name != self._name:
            self._name = name
            self.nameChanged.emit()

    def color(self):
        return self._color

    def set_color(self, color):
        if color != self._color:
            self._color = color
            self.colorChanged.emit()

    name = Property(str, name, set_name, notify=nameChanged)
    color = Property(str, color, set_color, notify=colorChanged)


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    dataList = [DataObject("Item 1", "red"),
                DataObject("Item 2", "green"),
                DataObject("Item 3", "blue"),
                DataObject("Item 4", "yellow")]

    view = QQuickView()
    #view.set_resize_mode(QQuickView.ResizeMode.SizeRootObjectToView)
    view.set_initial_properties({"model": dataList})

    qml_file = Path(__file__).parent / "view.qml"
    view.engine().add_import_path(Path(__file__).parent)
    view.load_from_module("ObjectListModel", "Main")
    view.show()

    r = app.exec()
    del view
    sys.exit(r)