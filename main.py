import sys
import os
from tkinter import filedialog
from PIL import Image, ImageFilter
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QVBoxLayout, QFormLayout,
    QLabel, QPushButton, QLineEdit,
)

class ImageResizer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Resizer")
        self.setGeometry(100, 100, 400, 200)  # Set initial window size

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        form_layout = QFormLayout()

        self.img_path_label = QLabel("Select an image:")
        self.img_path_entry = QLineEdit()
        self.select_btn = QPushButton("Browse", self)
        self.select_btn.setFixedWidth(100)
        self.select_btn.clicked.connect(self.select_image)

        self.dimensions_label = QLabel("Dimensions: N/A")
        self.resize_btn = QPushButton("Get Dimensions", self)
        self.resize_btn.setFixedWidth(100)
        self.resize_btn.clicked.connect(self.get_image_dimensions)

        self.width_label = QLabel("New width:")
        self.width_entry = QLineEdit()

        self.height_label = QLabel("New height:")
        self.height_entry = QLineEdit()

        self.resize_img_btn = QPushButton("Resize", self)
        self.resize_img_btn.setFixedWidth(100)
        self.resize_img_btn.clicked.connect(self.resize_image)

        self.error_label = QLabel("", self)

        form_layout.addRow(self.img_path_label, self.img_path_entry)
        form_layout.addRow(self.select_btn, self.dimensions_label)
        form_layout.addRow(self.width_label, self.width_entry)
        form_layout.addRow(self.height_label, self.height_entry)
        form_layout.addRow(self.resize_btn, self.resize_img_btn)
        form_layout.addRow(self.error_label)

        self.layout.addLayout(form_layout)

    def select_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.img_path_entry.setText(file_path)

    def get_image_dimensions(self):
        file_path = self.img_path_entry.text()
        if not file_path:
            return

        try:
            image = Image.open(file_path)
            width, height = image.size
            self.dimensions_label.setText(f"Dimensions: {width} x {height}")
        except Exception as e:
            self.error_label.setText(f"Error: {e}")

    def resize_image(self):
        file_path = self.img_path_entry.text()
        if not file_path:
            return

        try:
            new_width = int(self.width_entry.text())
            new_height = int(self.height_entry.text())

            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
            if save_path:
                process_image(file_path, new_width, new_height, save_path)
        except Exception as e:
            self.error_label.setText(f"Error: {e}")

def process_image(image_path, new_width, new_height, save_path):
    image_path = os.path.abspath(image_path)

    try:
        img = Image.open(image_path)
        # Calculate new dimensions while maintaining aspect ratio
        width, height = img.size
        aspect_ratio = width / height
        if new_width is None:
            new_width = int(new_height * aspect_ratio)
        elif new_height is None:
            new_height = int(new_width / aspect_ratio)
        resized_img = img.resize((new_width, new_height))
        resized_img.save(save_path, format='JPEG')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageResizer()
    window.show()
    sys.exit(app.exec())
