
####################################################################################################
#
#   Convert Video (.MOV) to several image files (.jpeg)
#
#   Usage:
#       file.py --image_prefix IMAGE_PREFIX --video_filepath VIDEO_FILEPATH --sampling_rate SAMPLING_RATE [--image_width IMAGE_WIDTH]
#       file.py --image_prefix oceans_11 --video_filepath /tmp/youtube_imm6OR605UI.mp4 --sampling_rate 1000 --image_width 400
#
#   Dependencies:
#       sudo apt-get install python-opencv
#
#   To Do:
#       Add exception handling
#
####################################################################################################

import sys,re
import datetime,time
import cv2
import argparse



def convert_video_to_images(image_prefix, video_filepath, sampling_rate, image_width):
    
    print('[ INFO ] Converting {} into images within current directory...'.format(video_filepath))
    time.sleep(3)
    start_time = datetime.datetime.now()
    
    video_obj = cv2.VideoCapture(video_filepath)
    success,image = video_obj.read()
    frame_count = 1
    while success:
        
        video_obj.set(cv2.CAP_PROP_POS_MSEC,(frame_count * sampling_rate))      # CAP_PROP_POS_MSEC is the current position of the video file in milliseconds or video capture timestamp.
        
        (h, w) = image.shape[:2]                                                # Get image height and width
        r = image_width / float(w)
        resized_image = cv2.resize(image, (image_width, int(h * r)))            # Resize image based on image_width, and keep scale / aspect ratio.
        
        frame_timestamp = re.sub('(\:|\.)','_',str(datetime.timedelta(seconds=frame_count * (sampling_rate/1000))).zfill(15))
        cv2.imwrite("{}_{}.jpg".format(image_prefix, frame_timestamp), resized_image)               # Save frame as .jpg file
        success,image = video_obj.read()
        frame_count += 1
        if (frame_count % 500) == 0:
            print('[ INFO ] {} frames have been processed.'.format(frame_count))
    
    end_time = datetime.datetime.now()
    run_time = (end_time - start_time).seconds
    print('[ INFO ] Complete - Processed {} frames in {} seconds'.format(frame_count, run_time) )



if __name__ == "__main__":
    
    ap = argparse.ArgumentParser()
    ap.add_argument("--image_prefix",   required=True,            help="Prefix / Name that is appended to each image filename")
    ap.add_argument("--video_filepath", required=True,            help="Video file path")
    ap.add_argument("--sampling_rate",  required=True,  type=int, help="Sampling Rate (in milliseconds). i.e. 500 ms sampling will produce 2 images per second")
    ap.add_argument("--image_width",    required=False, type=int, default=400, help="Desired image width, in pixels (Default: 400 pixels)")
    args = vars(ap.parse_args())
    
    convert_video_to_images(args['image_prefix'], args['video_filepath'], args['sampling_rate'], args['image_width'])
    


#ZEND
