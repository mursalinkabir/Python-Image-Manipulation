import os
from exif import DATETIME_STR_FORMAT, Image
img_file = 'naba1.jpg'


# Source Tutorial Link
# https://auth0.com/blog/read-edit-exif-metadata-in-photos-with-python/

#opening images in exif
with open("drn1.jpg", "rb") as naba_1_file:
    naba_1_image = Image(naba_1_file)
with open("tokoname2.jpeg", "rb") as naba_2_file:
    naba_2_image = Image(naba_2_file)
#assigning them to a variable
images = [naba_1_image,naba_2_image]
## checking if the image has exif data
# for index, image in enumerate(images):
#      if image.has_exif:
#           status = f'contains exif (version {image.exif_version}) information'
#      else:
#           status = 'Does not has exif version'
#      print(f'Image {index}{status}')


 # all the attributes will be there is this array             
image_members =[]
# loading image members array with all the attributes of the image using
#python dir
for image in images:
     image_members.append(dir(image))
# printinh all the exif tags of that image
for index,image_members_list in enumerate(image_members):
     print(f'Image {index} contains {len(image_members_list)} members')
     print(f'{image_members_list}\n')

   #formating the gps coordinates to dms  
def format_dms_coordinates(coordinates):
         return f"{coordinates[0]}° {coordinates[1]}\' {coordinates[2]}\""
# formatting the gps coordinates to deciman 
def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    decimal_degrees = coordinates[0] + \
                      coordinates[1] / 60 + \
                      coordinates[2] / 3600
    
    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees
    
    return decimal_degrees        
for index,image in enumerate(images):
#     print(f"Device information - Image {index}")
#     print("----------------------------")
#     print(f"Make: {image.make}")
#     print(f"Model: {image.model}\n")
#     print(f"Lens and OS - Image {index}")
#     print("---------------------")
#     print(f"Lens make: {image.get('lens_make', 'Unknown')}")
#     print(f"Lens model: {image.get('lens_model', 'Unknown')}")
#     print(f"Lens specification: {image.get('lens_specification', 'Unknown')}")
#     print(f"OS version: {image.get('software', 'Unknown')}\n")

# Printing the gps coordinates
    print(f"Coordinates - Image {index}")
    print("---------------------")
    print(f"Latitude (DMS): {format_dms_coordinates(image.gps_latitude)} {image.gps_latitude_ref}")
    print(f"Longitude (DMS): {format_dms_coordinates(image.gps_longitude)} {image.gps_longitude_ref}\n")
    print(f"Latitude (DD): {dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)}")
    print(f"Longitude (DD): {dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)}\n")
#opening the images in browser maps
def draw_map_for_location(latitude, latitude_ref, longitude, longitude_ref):
    import webbrowser
    decimal_latitude = dms_coordinates_to_dd_coordinates(latitude, latitude_ref)
    decimal_longitude = dms_coordinates_to_dd_coordinates(longitude, longitude_ref)
    url = f"https://www.google.com/maps?q={decimal_latitude},{decimal_longitude}"
    webbrowser.open_new_tab(url)

for index, image in enumerate(images):
         draw_map_for_location(image.gps_latitude, 
                          image.gps_latitude_ref, 
                          image.gps_longitude,
                          image.gps_longitude_ref)