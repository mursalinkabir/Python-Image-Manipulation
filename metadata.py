import os
from PIL import Image
from PIL.ExifTags import TAGS

#creating a dictionary
exif = {}

img_file = 'naba1.jpg'
image = Image.open(img_file)
#printing the exif tags 
for tag,value in image.getexif().items():
     if tag in TAGS:
          #converting tags in images to exif tags
          exif[TAGS[tag]] = value
if 'GPSInfo' in exif:
     geo
         
print(exif)
              
    