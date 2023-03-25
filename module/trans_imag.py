from wand.image import Image

input_file = 'image.png'
img = Image(filename=input_file)
print(img.height, img.width)
img = img.convert('jpeg')
img.save(filename="image.jpeg")
