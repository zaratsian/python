
##########################################################################################
#
#   Download Images from URLs
#
#   NOTE: This script will download images to the directory where python is called from.
#
##########################################################################################

import sys, re
import requests
import datetime,time


try:
    file_with_urls = sys.argv[1]
except:
    print '[ ERROR ] No CSV file provided. Usage: file.py <csv_file_containing_list_of_urls>'
    sys.exit()


def save_imdb_image_url(url):
    time.sleep(0.2)
    try:
        filename = url.split('/')[-1]
        if re.search('\.jpg$', url):    
            # Download Image
            get_image = requests.get(url)
            f = open(filename,'wb')
            f.write(get_image.content)
    except:
        print '[ ERROR ] Passed on ' + str(url)



#file_with_urls = '/Users/dzaratsian/Downloads/theme_park_urls_only.csv'

csvfile = open(file_with_urls, 'rb')
csvdata = csvfile.read().split()

counter = 0

for url in csvdata:
    counter +=1 
    print '[ INFO ] Collected Image #' + str(counter)
    save_imdb_image_url(url)



#ZEND