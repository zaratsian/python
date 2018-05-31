
#################################################################################################
#
#   Hipchat Analysis
#
#   API Docs: https://www.hipchat.com/docs/apiv2/
#
#   Usage: hipchat_extract.py <hipchat_token> <room_id_or_name>'
#
#################################################################################################


import sys,re
import requests
import datetime,time
import json


#################################################################################################
#
#   Functions - Hipchat
#
#################################################################################################

def get_room_messages(room_id_or_name, hipchat_token):
    
    base_url = 'https://hipchat.hortonworks.com'
    endpoint = '/v2/room/' + str(room_id_or_name) + '/history?max-results=100&end-date=2017-01-01&start-index=0&date=' + datetime.datetime.today().strftime('%Y-%m-%d')
    url      = base_url + endpoint
    
    messages = []
    
    while url != '':
        time.sleep(1.5)
        r = requests.get(url, headers={"Authorization": "Bearer " + str(hipchat_token) })
        print('Crawled ' + str(url))
        if r.status_code == 200:
            response = json.loads(r.content)
            messages  = messages + response['items']
            try:
                url = response['links']['next']
            except:
                print('[ INFO ] End of results: ' + str(response['links']))
                url = '' 
        else:
            print('[ WARNING ] Bad Status Code (' + str(r.status_code) + ')')
            url = ''
        
    print('Total Messages: ' + str(len(messages)))
    
    payload = {"room":room_id_or_name, "datetimestamp":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "total_messages":len(messages) ,"messages":messages}
    return payload


#################################################################################################
#
#   Functions - Text Analytics
#
#################################################################################################

def cleanup_text(text):
    text = re.sub('[ ]+',' ',re.sub('(\n|\r|\t)',' ',text))
    text = text.lower().strip()
    return text


def search_text(messages, search_term):
    '''
    Return all message payloads, where the text contains 'search_term'
    
    USAGE: search_results = search_text( results['sme-spark']['messages'], 'anaconda')
    '''
    search_results = []
    for message in messages:
        text = message['message']
        if re.search(search_term.lower(), text.lower()):
            print('\n')
            print(message)
            search_results.append(message)
    return search_results



if __name__ == "__main__":
    
    try:
        hipchat_token = sys.argv[1]
    except:
        print('[ USAGE ] file.py <hipchat_token> <room_id_or_name>')
        sys.exit()
    
    try:
        room_id_or_name = sys.argv[2]
    except:
        print('[ USAGE ] file.py <hipchat_token> <room_id_or_name>')
        sys.exit()
    
    results = {}
    results[room_id_or_name] = get_room_messages(room_id_or_name, hipchat_token)



#ZEND
