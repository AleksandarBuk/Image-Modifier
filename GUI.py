import tkinter as tk
from tkinter import filedialog
import subprocess

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

        save_path = filedialog.asksaveasfilename(defaultextension=".png")
        if save_path:
            # Call the main.py script with the selected image and size parameters
            subprocess.run(['python', 'main.py', file_path, str(new_width), str(new_height), save_path])
    except Exception as e:
        error_label.config(text=f"Error: {e}")

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
