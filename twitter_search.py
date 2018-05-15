
##################################################################################################################################
#
#   Twitter - Collect tweets based on search term
#   Created in 2016
#
#   References:
#       https://developer.twitter.com/en/docs/api-reference-index
#
#   Usage:
#       script.py <search_term_or_phrase>
#
##################################################################################################################################

import oauth2 as oauth
import time
import re
import json
#import simplejson
import csv
import codecs
import datetime


try:
    consumer = oauth.Consumer(
        key="ILuwhmqTTlPBMJmWo09HJMyeS",
        secret="MMbOu3YJFZXcrINs2me60MN1k22480IV8KH4i6n2UH94F67PT4")
    
    token = oauth.Token(
        key="1138224962-7ISJ4AMOXwKSIer60ogZfIUSTeHVx8W5xQfp27M", 
        secret="4InN8NJMIFYwCePyoXqBvhT7nCX1l2eJTIIlSLx0OEV32")
    
    client = oauth.Client(consumer, token)
except:
    print('[ ERROR ] Issue with twitter authentication. Make sure you have added your twitter keys and tokens.')
    sys.exit()


try:
    query1 = sys.argv[1]
    query1 = re.sub(' ','%20',query1)
    query1 = re.sub('"','%22',query1)
    query1 = re.sub('@','%40',query1)
    query1 = re.sub('#','%23',query1)
    query1 = re.sub('_','%5F',query1)
    query1 = re.sub('\+','%2B',query1)
    query1 = re.sub('&','%26',query1)
    query1 = re.sub('$','%24',query1)
except:
    print('[ ERROR ] Issue with twitter search term. Usage: script.py <search_term_or_phrase>')
    sys.exit()


query = []

for i in [query1]: #[query1,query2,query3,query4,query5]:
    if i != '':
        query.append(i)


tweet       = []
tweets      = []
text        = []
screen_name = []
location    = []
followers   = []
friends     = []
created_at  = []
retweeted   = []
entities    = []
since_id    = []
test        = []
table       = []
twitter_ids = []
language    = []
content     = []

for z in query:
    try:
        for i in range(1,16):
            #Twitter APIs  (https://dev.twitter.com/docs/api/1.1/get/search/tweets)
            if i == 1:
                #url = "https://api.twitter.com/1.1/search/tweets.json?q=" + z + "&result_type=mixed&count=100&lang=en"
                url = "https://api.twitter.com/1.1/search/tweets.json?q=" + z + "&result_type=mixed&count=100"
            else:
                #url = str("https://api.twitter.com/1.1/search/tweets.json?q=" + z + "&max_id=" + max_id + "&result_type=mixed&count=100&lang=en")
                url = str("https://api.twitter.com/1.1/search/tweets.json?q=" + z + "&max_id=" + max_id + "&result_type=mixed&count=100")
                resp,content = client.request(url)
                data = json.loads(content)
                tweets = data["statuses"]
            for tweet in tweets:
                text.append(tweet["text"])
                created_at.append(tweet["created_at"])
                retweeted.append(tweet["retweeted"])
                try:
                    screen_name.append(tweet["user"]["screen_name"])
                except:
                    screen_name.append('')
                try:
                    location.append(tweet["user"]["location"])
                except:
                    location.append('')
                try:
                    followers.append(tweet["user"]["followers_count"])
                except:
                    followers.append('')
                try:
                    friends.append(tweet["user"]["friends_count"])
                except:
                    friends.append('')
                try:
                    language.append(tweet["user"]["lang"])
                except:
                    language.append('')
                twitter_ids.append(tweet["id_str"])
            since_id = twitter_ids[0]
            max_id = str(int(twitter_ids[len(twitter_ids)-1])-1)
    except:
        print('Query ' + z + ' did not run because there was no content')

try:
    text2 = []
    for j in text:
        #out = "".join(i for i in j if ord(i)<128)
        out = re.sub('\n',' ',j)
        out = re.sub('\r',' ',out)
        out = re.sub('\t',' ',out)
        out = re.sub(',',' ',out)
        out = re.sub('[ ]+',' ',out)
        out = re.sub('http.{1,7}$','',out)
        out = re.sub('http$','',out)
        text2.append(out)
    
    screen_name2 = []
    for j in screen_name:
        out = "".join(i for i in j if ord(i)<128)
        screen_name2.append(out)
    
    created_at2 = []
    for j in created_at:
        out = "".join(i for i in j if ord(i)<128)
        created_at2.append(out)
    
    location2 = []
    for j in location:
        out = "".join(i for i in j if ord(i)<128)
        location2.append(out)
    
    day = []
    for j in created_at2:
        out = re.findall('[0-9]{1,2} [0-9]{2}:',str(j))
        out = re.sub(' .+','',str(out[0]))
        day.append(out)
    
    month = []
    for j in created_at2:
        out = re.findall('[a-zA-Z]{3} [0-9]{1,2} [0-9]{2}:',str(j))
        out = re.sub(' .+','',str(out[0]))
        if out == 'Jan': out='01'
        elif out == 'Feb': out='02'
        elif out == 'Mar': out='03'
        elif out == 'Apr': out='04'
        elif out == 'May': out='05'
        elif out == 'Jun': out='06'
        elif out == 'Jul': out='07'
        elif out == 'Aug': out='08'
        elif out == 'Sep': out='09'
        elif out == 'Oct': out='10'
        elif out == 'Nov': out='11'
        elif out == 'Dec': out='12'
        month.append(out)
    
    year = []
    for j in created_at2:
        out = re.findall('0000 [0-9]{4}',str(j))
        out = re.sub('0000 ','',str(out[0]))
        year.append(out)
    
    hour = []
    for j in created_at2:
        out = re.findall(' [0-9]{2}:',str(j))
        out = re.sub(':','',re.sub(' ','',str(out[0])))
        hour.append(out)
    
    minute = []
    for j in created_at2:
        out = re.findall(':[0-9]{2}:',str(j))
        out = re.sub(':','',re.sub(' ','',str(out[0])))
        minute.append(out)    
    
    date = []
    for j in range(len(created_at2)):
        out = datetime.datetime(int(year[j]),int(month[j]),int(day[j]),int(hour[j]),int(minute[j]))
        out1 = out - datetime.timedelta(0,(4*3600))
        date.append(out1)
    
    day = []
    for j in date:
        out = re.findall('[0-9]{1,2} [0-9]{2}:',str(j))
        out = re.sub(' .+','',str(out[0]))
        day.append(out)
    
    month = []
    for j in date:
        out = re.findall('-[0-9]{1,2}-',str(j))
        out = re.sub('-','',str(out[0]))
        month.append(out)
    
    year = []
    for j in date:
        out = re.findall('[0-9]{4}-',str(j))
        out = re.sub('-','',str(out[0]))
        year.append(out)
    
    hour = []
    for j in date:
        out = re.findall(' [0-9]{2}:',str(j))
        out = re.sub(':','',re.sub(' ','',str(out[0])))
        hour.append(out)
    
    date_id = []
    for j in range(len(date)):
        out = year[j] + '-' + month[j] + '-' + day[j] + 'hr:' + hour[j]
        date_id.append(out)
    
    date_time = []
    for j in date:
        out = str(j)
        date_time.append(out)
    
    weekday = []
    for j in date:
        out = int(j.weekday())
        if out == 0: out = 'SUN'
        elif out == 1: out = 'MON'
        elif out == 2: out = 'TUE'
        elif out == 3: out = 'WED'
        elif out == 4: out = 'THU'
        elif out == 5: out = 'FRI'
        elif out == 6: out = 'SAT'
        weekday.append(out)
except:
    pass


############################################################################
#
#   Enrichment
#
############################################################################
try:
    hashtags     = []
    hashtag_all = []
    for j in text2:
        out = re.findall('\#[a-zA-Z0-9\_]+',str(j))
        hashtag_all.append(out)
        if len(out)>0:
              out2 = out[0]
        else: out2 = ''
        hashtags.append(out2)
    
    tweeted_at     = []
    tweeted_at_all = []
    for j in text2:
        out = re.findall('\@[a-zA-Z0-9\_]+',str(j))
        tweeted_at_all.append(out)
        if len(out)>0:
              out2 = out[0]
        else: out2 = ''
        tweeted_at.append(out2)
    
    is_retweet = []
    for j in text2:
        out = re.findall('RT \@[a-zA-Z0-9\_]+',str(j))
        if out:
            is_retweet.append(1)
        else:
            is_retweet.append(0)
except:
    pass

source = []
for j in range(len(twitter_ids)):
    out = 'twitter'
    source.append(out)


headers = ['source','id','datetime','date_id','year','month','day','hour','weekday','author','location','text','followers','friends','hashtags','tweeted at','is_retweet','language']
table = zip(source,twitter_ids,date_time,date_id,year,month,day,hour,weekday,screen_name2,location2,text2,followers,friends,hashtags,tweeted_at,is_retweet,language)


timestamp = str(datetime.datetime.now())
timestamp = re.sub('(:|\.)','',re.sub(' ','_',re.sub('-','',timestamp)))
filepath = '/tmp/twitter_' + timestamp + '.csv'
file = open(filepath,'w')    
csvout = csv.writer(file)
csvout.writerow(headers)    
csvout.writerows(table)    
file.close()

#ZEND
