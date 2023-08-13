from PIL import Image, ImageFilter
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QLabel, QCheckBox,
    QComboBox, QListWidget, QLineEdit, QSpinBox,
    QDoubleSpinBox, QSlider
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("ImageResizer")

app = QApplication(sys.argv)
w = MainWindow()
w.show()


img = Image.open('./assets/images/WordPress.png')
filter_img = img.convert('L')
# filter_img = filter_img.filter(ImageFilter.SHARPEN)
filter_img.save('./assets/resized_photos/GWordPress.png')
filter_img.show()
# resize = filter_img.resize((1920,1080))
# resize.save('./assets/resized_photos/GitHub.png')
# resize.show()

app.exec()
