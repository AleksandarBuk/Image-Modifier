import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageFilter
import subprocess
import os

from PIL import Image, ImageFilter, ImageQt
import sys
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QVBoxLayout,
    QLabel, QLabel,QCheckBox,
    QComboBox, QListWidget, QLineEdit, QSpinBox,
    QDoubleSpinBox, QSlider,
)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("sad")

        #Creates a central widget and a vertical layout for it
        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)
        # self.layout = QVBoxLayout(central_widget)

        #Creates a QLabel to display the image
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img_path_entry.delete(0, tk.END)
        img_path_entry.insert(0, file_path)

def on_resize_click():
    file_path = img_path_entry.get()
    if not file_path:
        return

    try:
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())

        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if save_path:
            # Call the image processing function
            process_image(file_path, new_width, new_height, save_path)
    except Exception as e:
        error_label.config(text=f"Error: {e}")

def process_image(image_path, new_width, new_height, save_path):
    # Get the absolute file path of the image
    image_path = os.path.abspath(image_path)

    try:
        img = Image.open(image_path)
        filter_img = img.filter(ImageFilter.SHARPEN)
        resized_img = filter_img.resize((new_width, new_height))
        resized_img.save(save_path, format='JPEG')  # Save as JPG format
        resized_img.show()
    except Exception as e:
        print(f"Error: {e}")
    except FileNotFoundError as fnfe:
        error_label.config(f'FileNotFound: {fnfe}')
    except ValueError as ve:
        error_label.config(f'ValueError: {ve}')

# Create the main window
root = tk.Tk()
root.title("Image Resizer")

# Image Selection
img_path_label = tk.Label(root, text="Select an image:")
img_path_label.pack()
img_path_entry = tk.Entry(root, width=50)
img_path_entry.pack()
select_btn = tk.Button(root, text="Browse", command=select_image)
select_btn.pack()

# Resize Options
width_label = tk.Label(root, text="New width:")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

height_label = tk.Label(root, text="New height:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

resize_btn = tk.Button(root, text="Resize and Save", command=on_resize_click)
resize_btn.pack()

# Error Label
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()

app = QApplication(sys.argv)


w = MainWindow()
w.show()
app.exec()
