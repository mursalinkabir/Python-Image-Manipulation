from PIL import Image
import numpy as np

#reading images
image1 = Image.open('tokoname1.jpeg')
image2 = Image.open('tokoname2.jpeg')
# image2.show()
# shows the image width x Height
print(image2.size)

#saving image 
# image2.save('newimg.jpg')

#cropping image
# left top and right bottom two points will form a rectangular
# left= 50
# top=120
# right=250
# bottom = 230
# crop_img = image2.crop((left,top,right,bottom))
# crop_img.show()

#tranposing (changing orientation)

# transpose_img1 = image2.transpose(Image.FLIP_LEFT_RIGHT)
# transpose_img1.show()
# transpose_img2 = image2.transpose(Image.ROTATE_90)
# transpose_img2.show()

#Resizing 
#need tuple(width , height)
# it have several algo for resizing
# newsize = (300,300)
#here Image.Hamming is the algo
# resized_image1 = image2.resize(newsize,Image.HAMMING)
# resized_image1.show()

#rotating image
# angle= 30 
# rotated_img = image2.rotate(angle)
# rotated_img.show()

#Text watermark 
# from PIL import ImageFont
# from PIL import ImageDraw
# watermarked_image = image2.copy()
# #making an editable image
# draw = ImageDraw.Draw(watermarked_image)
# #choosing font 
# font = ImageFont.load_default()
# #(pos.text,filling color,font object)
# draw.text((0,0),'Sample Text',(0,0,0),font=font)
# watermarked_image.show()

#Draw a line
# from PIL import Image, ImageDraw
# #creating a canvas with RGB backgroud 500x300 width and height and the backgroud color 125,125,125
# img = Image.new('RGB', (500, 300), (125, 125, 125))
# draw = ImageDraw.Draw(img)
# #drwaing line left,top,right,bottom 
# draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)
# #drwaing a ellipse

# draw.ellipse((200, 150, 300, 200), fill=(255, 0, 0), outline=(0, 0, 0))
# img.show()

#image watermark
size= (500,500)
crop_image = image1.copy()
crop_image.thumbnail(size)

copied_image = image1.copy()
copied_image.paste(crop_image,(0,0))
copied_image.show()