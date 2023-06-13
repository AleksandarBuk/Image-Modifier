from PIL import Image, ImageFilter

img = Image.open('./assets/images/Website.png')
filter_img = img
filter_img = filter_img.filter(ImageFilter.SHARPEN)
resize = filter_img.resize((1920,1080))
resize.save('./assets/resized_photos/TravelBlog.png')
resize.show()
