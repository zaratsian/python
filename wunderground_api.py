
#################################################################################################
#
#   WUnderground
#
#   https://www.wunderground.com/weather/api/d/docs
#
#################################################################################################

import re,requests
import json
import datetime,time

apikey = 'xxxx'

latitude  = '35.7796'
longitude = '-78.6382'
localtime = '02/15/2017 08:30'


def convert_convert_geo(latitude, longitude):
    geo_url = 'http://maps.googleapis.com/maps/api/geocode/json?latlng=' + str(latitude) + ',' + str(longitude)
    geo_req = requests.get(geo_url)
    if geo_req.status_code==200:
        geo_jsondata = json.loads(geo_req.content)
        city  = geo_jsondata['results'][0]['address_components'][4]['long_name'].strip().replace(' ','_')
        state = geo_jsondata['results'][0]['address_components'][6]['short_name'].strip().replace(' ','_')
    else:
        print '[ ERROR ] Google Maps Geocode API Status Code: ' + str(geo_req.status_code)
    return city, state

seen_city_state_yyyymmdd = {}

def get_historical_weather(localtime, latitude, longitude):
    date_yyyymmdd   = datetime.datetime.strptime(localtime, '%m/%d/%Y %H:%M').strftime("%Y%m%d")
    date_hour       = datetime.datetime.strptime(localtime, '%m/%d/%Y %H:%M').strftime("%H")
    city, state     = convert_convert_geo(latitude, longitude)
    
    city_state_yyyymmdd = str(city) + '|' + str(state) + '|' + str(date_yyyymmdd)
    
    if city_state_yyyymmdd not in seen_city_state_yyyymmdd:
        
        weather_url = 'http://api.wunderground.com/api/0e3197f91b73b013/history_' + str(date_yyyymmdd) + '/q/' + str(state) + '/' + str(city) + '.json'
        print '[ INFO ] Crawling ' + str(weather_url)
        weather_req = requests.get(weather_url)
        if weather_req.status_code==200:
            jsondata    = json.loads(weather_req.content)
        else:
            print '[ ERROR ] WUnderground.com Status Code: ' + str(weather_req.status_code)
        
        seen_city_state_yyyymmdd[city_state_yyyymmdd] = jsondata
    else:
        print '[ INFO ] Data has already been collected (no need to call API), using existing data'
        jsondata = seen_city_state_yyyymmdd[city_state_yyyymmdd]
    
    record      = [hour_obs for hour_obs in jsondata['history']['observations'] if hour_obs['utcdate']['hour'] == date_hour ]
    heatindexm  = record[0]['heatindexm']
    windchillm  = record[0]['windchillm']
    wdire       = record[0]['wdire']
    wdird       = record[0]['wdird']
    windchilli  = record[0]['windchilli']
    hail        = record[0]['hail']
    heatindexi  = record[0]['heatindexi']
    precipi     = record[0]['precipi']
    thunder     = record[0]['thunder']
    pressurei   = record[0]['pressurei']
    snow        = record[0]['snow']
    pressurem   = record[0]['pressurem']
    fog         = record[0]['fog']
    icon        = record[0]['icon']
    precipm     = record[0]['precipm']
    conds       = record[0]['conds']
    tornado     = record[0]['tornado']
    hum         = record[0]['hum']
    tempi       = record[0]['tempi']
    tempm       = record[0]['tempm']
    dewptm      = record[0]['dewptm']
    rain        = record[0]['rain']
    dewpti      = record[0]['dewpti']
    date        = record[0]['date']
    visi        = record[0]['visi']
    vism        = record[0]['vism']
    utcdate     = record[0]['utcdate']
    wgusti      = record[0]['wgusti']
    metar       = record[0]['metar']
    wgustm      = record[0]['wgustm']
    wspdi       = record[0]['wspdi']
    wspdm       = record[0]['wspdm']
    return heatindexm,windchillm,wdire,wdird,windchilli,hail,heatindexi,precipi,thunder,pressurei,snow,pressurem,fog,icon,precipm,conds,tornado,hum,tempi,tempm,dewptm,rain,dewpti,date,visi,vism,utcdate,wgusti,metar,wgustm,wspdi,wspdm




'''

Usage:

get_historical_weather(localtime, latitude, longitude)

'''


#ZEND