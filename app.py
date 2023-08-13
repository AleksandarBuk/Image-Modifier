from PIL import Image, ImageFilter, ImageQt
import sys
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QVBoxLayout,
    QLabel, QLabel,QCheckBox,
    QComboBox, QListWidget, QLineEdit, QSpinBox,
    QDoubleSpinBox, QSlider,
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("ImageResizer")

        #Creates a central widget and a vertical layout for it
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        #Add your UI elements to the layout
        #Results of the script
        self.result_label = QLabel("Result Logic")
        self.layout.addWidget(self.result_label)

        #Creates a QLabel to display the image
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

app = QApplication(sys.argv)
w = MainWindow()
w.show()

img = Image.open('./assets/images/WordPress.png')
filter_img = img.convert('L')
filter_img.save('./assets/resized_photos/GWordPress.png')

image = ImageQt.toqpixmap(filter_img)
w.image_label.setPixmap(image)

w.result_label.setText("Logic Result: Image processed and saved")
# resize = filter_img.resize((1920,1080))
# resize.save('./assets/resized_photos/GitHub.png')
# resize.show()

app.exec()
