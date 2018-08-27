
############################################################################################################
#
#   Script to crawl IMDB and pull down images (and movie info) for use in Apps and ML models.
#
############################################################################################################

import re,sys
import requests
import time


movie_titles = [u'Avatar', u"Pirates of the Caribbean: At World's End", u'Spectre', u'The Dark Knight Rises', u'John Carter', u'Spider-Man 3', u'Tangled', u'Avengers: Age of Ultron', u'Harry Potter and the Half-Blood Prince', u'Batman v Superman: Dawn of Justice', u'Superman Returns', u'Quantum of Solace', u"Pirates of the Caribbean: Dead Man's Chest", u'The Lone Ranger', u'Man of Steel', u'The Chronicles of Narnia: Prince Caspian', u'The Avengers', u'Pirates of the Caribbean: On Stranger Tides', u'Men in Black 3', u'The Hobbit: The Battle of the Five Armies', u'The Amazing Spider-Man', u'Robin Hood', u'The Hobbit: The Desolation of Smaug', u'The Golden Compass', u'King Kong', u'Titanic', u'Captain America: Civil War', u'Battleship', u'Jurassic World', u'Skyfall', u'Spider-Man 2', u'Iron Man 3', u'Alice in Wonderland', u'X-Men: The Last Stand', u'Monsters University', u'Transformers: Revenge of the Fallen', u'Transformers: Age of Extinction', u'Oz: The Great and Powerful', u'The Amazing Spider-Man 2', u'TRON: Legacy', u'Cars 2', u'Green Lantern', u'Toy Story 3', u'Terminator Salvation', u'Furious 7', u'World War Z', u'X-Men: Days of Future Past', u'Star Trek Into Darkness', u'Jack the Giant Slayer', u'The Great Gatsby']


def save_imdb_image(movie_title):
    try:
        time.sleep(0.2)
        movie_title_clean = re.sub('[^a-zA-Z0-9 ]','_',movie_title)
        movie_title = re.sub('[ ]+',' ',movie_title).lower().strip()
        movie_title = re.sub(' ','+',movie_title)
        
        search_url  = 'http://www.imdb.com/find?ref_=nv_sr_fn&q=' + str(movie_title) + '&s=all'
        print '[ INFO ] Crawling ' + str(search_url)
        
        search_data = re.sub('(\r|\n|\t)',' ',requests.get(search_url).content)
        
        movie_url = re.findall('<tr class="findResult odd">.*?</tr>',search_data)[0]
        movie_url = re.findall('<a href=.*?\" >', movie_url)[0]
        movie_url = 'http://www.imdb.com/' + movie_url.replace('<a href="','').replace('" >','')
        
        movie_details = re.sub('(\r|\t|\n)',' ',requests.get(movie_url).content)
        movie_img     = re.findall('<div class="poster">.*?</div>',movie_details)[0]
        movie_img     = re.findall('https.*?\"',movie_img)[0].replace('"','')
        
        # Download Image
        filename  = movie_title_clean + '.jpg'
        get_image = requests.get(movie_img)
        f = open(filename,'wb')
        f.write(get_image.content)
    except:
        print '[ ERROR ] Passed on ' + str(movie_title)


for movie_title in movie_titles:
    save_imdb_image(movie_title)







#ZEND