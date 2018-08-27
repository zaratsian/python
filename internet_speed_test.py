
##########################################################################################################
#
#   Internet Speed Test (code to monitor/log internet speeds)
#
#   Usage: python internet_speed_test.py &
#
##########################################################################################################

'''
Dependancies:
pip install speedtest-cli

'''

import os
import re
import subprocess
import time
#import sqlite3

filename = os.getcwd() + '/internet_speed_results.txt'
dbname   = os.getcwd() + '/internet_speed_results.db'

response = subprocess.Popen('speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read()

speed_ping     = re.findall('[0-9\.]+', response.split('\n')[0])[0]     # Ping: 38.288 ms
speed_download = re.findall('[0-9\.]+', response.split('\n')[1])[0]     # Download: 31.83 Mbit/s
speed_upload   = re.findall('[0-9\.]+', response.split('\n')[2])[0]     # Upload: 4.17 Mbit/s

if os.path.isfile(filename): # If file exists
    file = open(filename,'a')
else:
    file = open(filename,'wb')
    file.write('Date, Time, Ping (ms), Download (Mbit/s), Upload (Mbit/s)')

file.write('\n' + str(time.strftime('%m/%d/%y')) + ', ' + str(time.strftime('%H:%M')) + ', ' + str(speed_ping) + ', ' + str(speed_download) + ', ' + str(speed_upload))
file.close()


'''
con = None
con = sqlite3.connect(dbname)
cur = con.cursor()

if not os.path.isfile(dbname): # If db does not exist
    cur.execute("CREATE TABLE internet_speed (date TEXT, time TEXT, speed_ping REAL, speed_download REAL, speed_upload REAL)")

cur.execute("INSERT INTO internet_speed VALUES (?,?,?,?,?)", str(time.strftime('%m/%d/%y')), str(time.strftime('%H:%M')), str(speed_ping), str(speed_download), str(speed_upload))

con.commit()
con.close()

'''

#ZEND