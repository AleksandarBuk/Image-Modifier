from PIL import Image, ImageFilter
<<<<<<< HEAD
import sys
import os

if len(sys.argv) != 5:
    print("Usage: main.py <image_path> <new_width> <new_height> <save_path>")
    sys.exit(1)

image_path = sys.argv[1]
new_width = int(sys.argv[2])
new_height = int(sys.argv[3])
save_path = sys.argv[4]

image_path = os.path.abspath(image_path)

try:
    img = Image.open(image_path)
    filter_img = img.filter(ImageFilter.SHARPEN)
    resized_img = filter_img.resize((new_width, new_height))
    resized_img.save(save_path, format='png')
    resized_img.show()
except Exception as e:
    print(f"Error: {e}")
=======

img = Image.open('./assets/images/Website.png')
filter_img = img
filter_img = filter_img.filter(ImageFilter.SHARPEN)
resize = filter_img.resize((1920,1080))
resize.save('./assets/resized_photos/TravelBlog.png')
resize.show()
>>>>>>> origin/main
