
####################################################################################################
#
#   Convert Video (.MOV) to several image files (.jpeg)
#
#   Usage:
#       file.py <video_file> <number_of_images_per_second>
#       file.py "/assets/IMG_7942.MOV" 2
#
#   Dependencies:
#       sudo apt-get install python-opencv
#
####################################################################################################

import sys
import datetime,time
import cv2


try:
    video_file = sys.argv[1]
except:
    print('[ ERROR ] Usage: file.py <video_file> <number_of_images_per_second>')
    sys.exit()

try:
    img_per_sec = float(sys.argv[2])
except:
    print('[ WARNING ] Did not receive a valid argument. Proceeding with a sampling rate of 1 image per second.')
    print('[ WARNING ] Usage: file.py <video_file> <number_of_images_per_second>')


# Set Desired Image Width and Height
img_width = 400 # 400 pixels


video_obj = cv2.VideoCapture(video_file)
success,image = video_obj.read()
count = 1
while success:
    video_obj.set(cv2.CAP_PROP_POS_MSEC,(count * (1/float(img_per_sec)) * 1000))    # CAP_PROP_POS_MSEC is the current position of the video file in milliseconds or video capture timestamp.
    
    (h, w) = image.shape[:2]                                                        # Get image height and width
    r = img_width / float(w)
    resized_image = cv2.resize(image, (img_width, int(h * r)))                      # Resize image based on img_width, and keep scale / aspect ratio.
    
    cv2.imwrite("frame" + str(count) + ".jpg", resized_image)                       # Save frame as .jpg file      
    success,image = video_obj.read()
    print('Processed ' + str(count) + ' frames. Reading new frame...')
    count += 1



#ZEND
