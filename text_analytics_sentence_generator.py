

#############################################################################################################
##
##  Markov Chain
##  Sentence Generator
##  http://www.statsblogs.com/2014/02/20/how-to-fake-a-sophisticated-knowledge-of-wine-with-markov-chains/
##
#############################################################################################################


import sys,re,csv
import pickle       # Convert python object hierarchy into a byte stream
import random


def import_csv(filepath_with_name):
    try:
        file = csv.reader(open(filepath_with_name, 'rb'))
        
        # Header
        header  = file.next()
        
        row_count = 0
        rows      = []
        for row in file:
            rows.append(row)
            row_count = row_count + 1
        
        col_count = len(row)
    except: 
        rows = 'Error in data location or format'
        header    = ''
        col_count = ''
        row_count = ''
    
    return(rows, header, col_count, row_count)

data, header, cols, rows = import_csv('/Users/dzaratsian/Dropbox/data/wine_reviews.csv')


data2 = []
for i in data:
    text = i[6]
    #text = re.sub('(\.|\,)',' ',text).strip()
    text = re.sub('[ ]+',' ',text).strip()
    text = 'ZSTART HERE ' + str(text) + ' ZEND'
    data2.append(text)


chains = {}


def generate_trigram(words):
    if len(words) < 3:
        return
    for i in xrange(len(words) - 2):
        yield (words[i], words[i+1], words[i+2])


for line in data2:
    words = line.split()
    for word1, word2, word3 in generate_trigram(words):
        key = (word1, word2)
        if key in chains:
            chains[key].append(word3)
        else:
            chains[key] = [word3]



#############################################################################################################
##
##  Sentence Generator
##
#############################################################################################################
def myreview():
    new_review = []
    sword1 = "ZSTART"
    sword2 = "HERE"
    
    while True:
        sword1, sword2 = sword2, random.choice(chains[(sword1, sword2)])
        if sword2 == "ZEND":
            break
        
        new_review.append(sword2)
    
    print ' '.join(new_review)


myreview()



#############################################################################################################
##
##  Query to find sequential word(s)
##
#############################################################################################################

query = 'chocolate'

count = 0
for bi_gram in chains:
    if bi_gram[0] == query:                                     # If first word equal to query
        if (count <= 10):                                       # Only list first XX matches
            if (len(bi_gram[0]) > 3) and (len(bi_gram[1]) > 3): # If word character count is greater than 3 characters
                count = count + 1
                print bi_gram



#ZEND