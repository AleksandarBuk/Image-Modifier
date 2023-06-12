from PIL import Image, ImageFilter

img = Image.open('./assets/images/interior-cleaning.jpeg')
filter_img = img.convert('L')
filter_img = filter_img.filter(ImageFilter.SHARPEN)
resize = filter_img.resize((1920,1080))
resize.save('./assets/resized_photos/interiorhd.png')
resize.show()
