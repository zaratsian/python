
#################################################################################################
#
#   Rename Images
#
#   This script renames images based on the directory in which they are located and the 
#   timestamp of the image (if it is contained within the image metadata).
#
#   Usage: python rename_images_in_folders.py <directory>
#
#   Directory Structure:
'''
        /
        /glacier_trek
            image_that_needs_to_be_renamed1.jpeg
            image_that_needs_to_be_renamed2.jpeg
            image_that_needs_to_be_renamed3.jpeg
        /hiking_torres
            image_that_needs_to_be_renamed4.jpeg
            image_that_needs_to_be_renamed5.jpeg
            image_that_needs_to_be_renamed6.jpeg
        /food_pics
            image_that_needs_to_be_renamed7.jpeg
            image_that_needs_to_be_renamed8.jpeg
            image_that_needs_to_be_renamed9.jpeg
'''
#################################################################################################


import sys, os, re
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


allowable_file_extensions = ['jpg','jpeg','png','m4v','mov']


def get_folder_and_images(directory):
    '''
    Returns tuple of (image_directory, images)
    '''
    return [(x[0],x[2]) for x in os.walk(directory)][1:]


def extract_image_metadata(image_path):
    enriched_metadata = {}
    image = Image.open(image_path)
    image_metadata = image._getexif()
    for tag, value in image_metadata.items():
        tag_desc = TAGS.get(tag, tag)
        enriched_metadata[tag_desc] = value
    return enriched_metadata


def rename_image(current_filepath, new_filepath):
    os.rename(current_filepath, new_filepath)


if __name__ == '__main__':
    
    directory = sys.argv[1]
    print('[ INFO ] Using directory = ' + directory)
    
    folder_and_images = get_folder_and_images(directory)
    
    print('[ INFO ] About to rename images within these directories...\n')
    
    for item in folder_and_images:
        print(item[0])
    
    response = input('\n[ INFO ] Press "y" to continue or any other key to abort\n\n')
    
    if response == 'y':
        
        for image_directory,images in get_folder_and_images(directory):

            print('[ INFO ] Renaming images within ' + image_directory)
            counter = 20000000
            
            for image in images:
                
                image_extension = image.split('.')[-1]
                
                if image_extension.lower() in allowable_file_extensions:
                    
                    current_filepath = image_directory + '/' + image
                    
                    try:
                        image_metadata   = extract_image_metadata(current_filepath)
                        image_timestamp  = image_metadata['DateTime'].replace(':','').replace(' ','_')
                        
                        new_filepath     = image_directory + '/' + str(image_directory.split('/')[-1]) + '_' + image_timestamp + '.' + image_extension
                        os.rename(current_filepath, new_filepath)
                    except:
                        new_filepath     = image_directory + '/' + str(image_directory.split('/')[-1]) + '_' + str(counter) + '.' + image_extension
                        os.rename(current_filepath, new_filepath)
                        counter += 1

#ZEND