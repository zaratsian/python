

#################################################################################################
#
#   Resize Images
#
#   Usage: python resize_images.py <image_directory> <width_px>
#
#   This script will resize images based on a specific width, the aspect ratio will be kept the same.
#
#################################################################################################


import os, sys, re
from PIL import Image
from resizeimage import resizeimage


try:
    image_directory = sys.argv[1]
    #image_directory = '/Users/dzaratsian/Desktop/photo_hiking/images_for_website'
except:
    print('[ USAGE ] resize_images.py <image_directory> <width_px=2000>')
    sys.exit()


try:
    width = int(sys.argv[2])
except:
    print('[ USAGE ] resize_images.py <image_directory> <width_px=2000>')
    sys.exit()


images = [image for image in os.listdir(image_directory) if image[0] != '.']


for image in images:
    
    if not re.search('thumbnail_',image.lower()):
        image_filepath = image_directory + '/' + str(image)
        image_outfile  = image_directory + '/' + 'resized2000_' + re.sub('(\.jpg|\.jpeg|\.png)','',image) + '.jpg'
        
        try:
            im = Image.open(image_directory + '/' + image)
            try:
                im = resizeimage.resize_width(im, width) 
            except:
                im = im
            im.save(image_outfile)
        except:
            print('[ WARNING ] Could not convert ' + str(image))


#ZEND