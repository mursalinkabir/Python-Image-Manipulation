from PIL import Image
img = Image.open("tokoname1.jpeg")
print(img.size)

# small_img = img.resize((200,300))

# # resize without aspect ratio
# small_img.save('Resizedimg/tokoname_small.jpeg')
# resize with aspect ratio
#aspect ration only cares about the width not the height here 200 is width
# img.thumbnail((200,300))
# img.save('Resizedimg/tokoname_tmb.jpeg')


