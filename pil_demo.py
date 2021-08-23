from PIL import Image, ImageFilter
import os

# size_300 = (300,300)
# size_700 = (700,700)
# #looping through all the files of this directory
# for f in os.listdir('.'):
#      if f.endswith('.jpg'):
#           i = Image.open(f)
#           # changing sizes
#           fn, fext = os.path.splitext(f)
#           i.thumbnail(size_700)
#           i.save('700/{}_700{}'.format(fn,fext))
#           i.thumbnail(size_300)
#           i.save('300/{}_300{}'.format(fn,fext))
              

         
# image1 = Image.open('sappororiver.jpg')
# image1.save('sappororiver.png')
# image1 = Image.open('sappororiver.jpg')
# #rotating image
# image1.rotate(90).save('sappororiver_mod.jpg')

# image1 = Image.open('sappororiver.jpg')
# #rmaking image black and white
# image1.convert(mode='L').save('sappororiver_mod.jpg')

image1 = Image.open('sappororiver.jpg')
#adding filter
image1.filter(ImageFilter.GaussianBlur(15)).save('sappororiver_mod.jpg')