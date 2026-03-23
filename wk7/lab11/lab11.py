#Task 1
import PySide6.QtCore

#Task 2
'''
PySide6.QtWidgets.QBoxLayout

class QBoxLayout
The QBoxLayout class lines up child widgets horizontally or vertically.
QBoxLayout takes the space it gets (from its parent layout or from the parentWidget() ), 
divides it up into a row of boxes, and makes each managed widget fill one box.

If the QBoxLayout ‘s orientation is Qt::Horizontal the boxes are placed in a row
If the QBoxLayout ‘s orientation is Qt::Vertical, the boxes are placed in a column

The margin default is provided by the style. The default margin most Qt styles specify is 9 for child widgets and 11 for windows.
The spacing defaults to the same as the margin width for a top-level layout, or to the same as the parent layout.

To remove a widget from a layout, call removeWidget().

'''

#Task 3
import sys

# import classes from PySide6.QtWidgets module
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from __feature__ import snake_case, true_property

# create a QApplication object
my_app = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Andrew Ryer")

        vBox = QVBoxLayout()
        vBox.add_widget(label)

        self.set_layout(vBox)
        self.resize(400,400)

        self.show()

# create a MyWindow object
my_win = MyWindow()

# enter the Qt main loop and start to execute the Qt code
sys.exit(my_app.exec())
