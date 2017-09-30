
##########################################################################################################
#
#   Track Flight Times & Inbound Flight Status
#
#   Usage: flightaware_tracker.py <airline> <flight_number>
#          flightaware_tracker.py delta 5538
#          flightaware_tracker.py american 2222
#          flightaware_tracker.py southwest 3333
#          flightaware_tracker.py united 4444
#
##########################################################################################################

import re,sys,requests
from lxml import html
import datetime,time
import json

airline       = sys.argv[1]
flight_number = sys.argv[2]

if   airline.lower().strip() == 'delta':        airline = 'DAL'
elif airline.lower().strip() == 'southwest':    airline = 'SWA'
elif airline.lower().strip() == 'american':     airline = 'AAL'
elif airline.lower().strip() == 'united':       airline = 'ULA'

myflight_url = 'https://flightaware.com/live/flight/' + str(airline) + str(flight_number)

print '[ INFO ] Crawling ' + str(myflight_url)
req = requests.get(myflight_url)

if req.status_code == 200:
    data = re.sub('(\n|\t|\r)',' ',req.content)
    
    jsondata = json.loads(re.findall('<script>var trackpollBootstrap.*?</script>', data)[0].replace('<script>var trackpollBootstrap = ','').replace(';</script>',''))
    
    myflight_origin              = jsondata['flights'][list(jsondata['flights'])[0]]['origin']['friendlyLocation']
    myflight_destination         = jsondata['flights'][list(jsondata['flights'])[0]]['destination']['friendlyLocation']
    myflight_scheduled_departure = datetime.datetime.fromtimestamp(jsondata['flights'][list(jsondata['flights'])[0]]['gateDepartureTimes']['scheduled']).strftime('%Y-%m-%d %H:%M:%S')
    myflight_estimated_departure = datetime.datetime.fromtimestamp(jsondata['flights'][list(jsondata['flights'])[0]]['gateDepartureTimes']['estimated']).strftime('%Y-%m-%d %H:%M:%S')
    myflight_gate_arrival_time   = datetime.datetime.fromtimestamp(jsondata['flights'][list(jsondata['flights'])[0]]['gateArrivalTimes']['estimated']).strftime('%Y-%m-%d %H:%M:%S')
    myflight_cancelled           = jsondata['flights'][list(jsondata['flights'])[0]]['cancelled']
    inbound_flight_url           = 'https://flightaware.com/' + str(jsondata['flights'][list(jsondata['flights'])[0]]['inboundFlight']['linkUrl'])
    #inbound_flight_url          = 'https://flightaware.com/' + str(re.sub('.*?"linkUrl":"','',re.findall('"inboundFlight.*?}', data)[0]).replace('"}',''))
    
    print '[ INFO ] Crawling ' + str(inbound_flight_url)
    req = requests.get(inbound_flight_url)
    
    if req.status_code == 200:
        data = re.sub('(\n|\t|\r)',' ',req.content)
        
        jsondata = json.loads(re.findall('<script>var trackpollBootstrap.*?</script>', data)[0].replace('<script>var trackpollBootstrap = ','').replace(';</script>',''))
        
        inbound_flight_origin              = jsondata['flights'][list(jsondata['flights'])[0]]['origin']['friendlyLocation']
        inbound_flight_destination         = jsondata['flights'][list(jsondata['flights'])[0]]['destination']['friendlyLocation']
        inbound_flight_scheduled_departure = datetime.datetime.fromtimestamp(jsondata['flights'][list(jsondata['flights'])[0]]['gateDepartureTimes']['scheduled']).strftime('%Y-%m-%d %H:%M:%S')
        inbound_flight_estimated_departure = datetime.datetime.fromtimestamp(jsondata['flights'][list(jsondata['flights'])[0]]['gateDepartureTimes']['estimated']).strftime('%Y-%m-%d %H:%M:%S')
        inbound_flight_gate_arrival_time   = datetime.datetime.fromtimestamp(jsondata['flights'][list(jsondata['flights'])[0]]['gateArrivalTimes']['estimated']).strftime('%Y-%m-%d %H:%M:%S')
        try:
            inbound_flight_actual_departure = datetime.datetime.fromtimestamp(jsondata['flights'][list(jsondata['flights'])[0]]['gateDepartureTimes']['actual']).strftime('%Y-%m-%d %H:%M:%S')
        except:
            inbound_flight_actual_departure = 'Did not takeoff yet'
        inbound_flight_cancelled           = jsondata['flights'][list(jsondata['flights'])[0]]['cancelled']
        inbound_flight_url2                = 'https://flightaware.com/' + str(jsondata['flights'][list(jsondata['flights'])[0]]['inboundFlight']['linkUrl'])
        
        jsondata_delays = json.loads(re.findall('<script>var rosettaBootstrap.*?</script>', data)[0].replace('<script>var rosettaBootstrap = ','').replace(';</script>',''))
        #inbound_flight_url2               = 'https://flightaware.com/' + str(re.sub('.*?"linkUrl":"','',re.findall('"inboundFlight.*?}', data)[0]).replace('"}',''))
    else:
        print '[ ERROR ] Status Code (inbound flight): ' + str(req.status_code)
else:
    print '[ ERROR ] Status Code (my flight): ' + str(req.status_code)


print '\n\n####################################################################\n'
print 'My Flight Details:\n' 
print 'My Flight Gate Arrival Time:       ' + str(myflight_gate_arrival_time)
print 'My Flight Origin:                  ' + str(myflight_origin)
print 'My Flight Destination:             ' + str(myflight_destination)
print 'My Flight Scheduled Dept:          ' + str(myflight_scheduled_departure)
print 'My Flight Estimated Dept:          ' + str(myflight_estimated_departure)
print 'My Flight Cancelled:               ' + str(myflight_cancelled)
print 'My Flight URL:                     ' + str(myflight_url)
print '\n\n'
print 'Inbound Flight Details:\n'
print 'Inbound Flight Gate Arrival Time:  ' + str(inbound_flight_gate_arrival_time)
print 'Inbound Flight Origin:             ' + str(inbound_flight_origin)
print 'Inbound Flight Destination:        ' + str(inbound_flight_destination)
print 'Inbound Flight Scheduled Dept:     ' + str(inbound_flight_scheduled_departure)
print 'Inbound Flight Estimated Dept:     ' + str(inbound_flight_estimated_departure)
print 'Inbound Flight Actual Dept:        ' + str(inbound_flight_actual_departure)
print 'Inbound Flight Cancelled:          ' + str(myflight_cancelled)
print 'Inbound Flight URL:                ' + str(inbound_flight_url)
print '\n####################################################################\n\n'




#ZEND

