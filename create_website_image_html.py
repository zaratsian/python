import os
 
directory = '/Users/dzaratsian/Desktop/photos_patagonia/images_for_website'
images    = [image for image in os.listdir(directory) if image[0] != '.']
 
for i, image in enumerate(images):
     
    if image.split('_')[0] == 'torres':
        tag      = 'torres'
        location = 'Torres del Paine, Chile'
    elif image.split('_')[0] == 'puntas':
        tag      = 'puntas_arenas'
        location = 'Punta Arenas, Chile'
    elif image.split('_')[0] == 'ushuaia':
        tag      = 'ushuaia'
        location = 'Ushuaia, Argentina'
    else:
        tag      = 'unknown_tag'
        location = 'unknown_location'
     
    #print tag
    print '''
                        <div class="span3 project ''' + str(tag) + '''">
                            <img src="images/''' + str(image) + '''" alt="" class="project-img">
                            <span class="overlay"></span>
                            <div class="cnt">
                                <a href="images/''' + str(image) + '''" class="fancybox-media btn btn-normal" data-title-id="image_''' + str(10000+i) + '''"  rel="portfolio">View details</a>
                            </div>
                            <div id="image_''' + str(10000+i) + '''" class="info hidden">
                                <h2>Image Details</h2>
                                <div class="fancybody">''' + str(location) + '''</div>
                            </div>
                        </div>
      
    '''
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
import os
 
directory = '/Users/dzaratsian/Desktop/photos_patagonia/images_for_website'
images    = [image for image in os.listdir(directory) if image[0] != '.']
 
for i, image in enumerate(images):
     
    if image.split('_')[0] == 'torres':
        tag      = 'torres'
        location = 'Torres del Paine, Chile'
    elif image.split('_')[0] == 'puntas':
        tag      = 'puntas_arenas'
        location = 'Punta Arenas, Chile'
    elif image.split('_')[0] == 'ushuaia':
        tag      = 'ushuaia'
        location = 'Ushuaia, Argentina'
    else:
        tag      = 'unknown_tag'
        location = 'unknown_location'
     
    #print tag
    print '''
                        <div class="show-on-desktop">
                            <div class="span1 project ''' + str(tag) + '''">
                                <img src="images/thumbnail_''' + str(image) + '''" alt="" class="project-img">
                                <span class="overlay"></span>
                                <div class="cnt">
                                    <a href="images/''' + str(image) + '''" class="fancybox-media btn btn-normal" data-title-id="image_''' + str(10000+i) + '''"  rel="portfolio">View details</a>
                                </div>
                                <div id="image_''' + str(10000+i) + '''" class="info hidden">
                                    <h2>Image Details</h2>
                                    <div class="fancybody">''' + str(location) + '''</div>
                                </div>
                            </div>
                        </div>
                        <div class="show-on-mobile">
                            <div class="span1 project ''' + str(tag) + '''">
                                <img src="images/resized_''' + str(image) + '''" alt="" class="project-img">
                            </div>
                        </div>
      
    '''
 
 
 
 
 
 
 
 
 
 
import os, re
 
directory = '/Users/dzaratsian/Desktop/photo_hiking/images_for_website'
images    = [image for image in os.listdir(directory) if image[0] != '.']
 
for i, image in enumerate(images):
     
    if not re.search('thumbnail_',image.lower()) and not re.search('resized',image.lower()):
         
        if image.split('_')[0] == 'antelope':
            tag      = 'antelope_canyon'
            location = 'Antelope Canyon, AZ'
        elif image.split('_')[0] == 'grand':
            tag      = 'grand_canyon'
            location = 'Grand Canyon, AZ'
        elif image.split('_')[0] == 'horseshoe':
            tag      = 'horseshoe_bend'
            location = 'Horseshoe Bend, AZ'
        elif image.split('_')[0] == 'sedona':
            tag      = 'sedona'
            location = 'Sedona, AZ'
        elif image.split('_')[0] == 'tucson':
            tag      = 'tucson'
            location = 'Tucson, AZ'
        elif image.split('_')[0] == 'zion':
            tag      = 'zion'
            location = 'Zion National Park, UT'
        else:
            tag      = 'unknown_tag'
            location = 'unknown_location'
         
        #print tag
        print('''
                            <div class="show-on-desktop">
                                <div class="span1 project ''' + str(tag) + '''">
                                    <img src="images/national_parks/thumbnail_''' + str(image) + '''" alt="" class="project-img">
                                    <span class="overlay"></span>
                                    <div class="cnt">
                                        <a href="images/national_parks/''' + str(image) + '''" class="fancybox-media btn btn-normal" data-title-id="image_''' + str(10000+i) + '''"  rel="portfolio">View details</a>
                                    </div>
                                    <div id="image_''' + str(10000+i) + '''" class="info hidden">
                                        <h2>Image Details</h2>
                                        <div class="fancybody">''' + str(location) + '''</div>
                                    </div>
                                </div>
                            </div>
                            <div class="show-on-mobile">
                                <div class="span1 project ''' + str(tag) + '''">
                                    <img src="images/national_parks/resized2000_''' + str(image) + '''" alt="" class="project-img">
                                </div>
                            </div>
          
        ''')
 
 
 
#ZEND
