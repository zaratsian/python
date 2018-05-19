
##########################################################################################################
#
#   Networks Data Transfer Rates (Tags: network, bandwidth, data rate, data transfer)
#
#   Usage:
#       script.py <file_size_in_GB> <data_transfer_speed_in_Gbps>
#       script.py 100 1         # Time to transfer 100GB on a 1Gbps network
#       script.py 1 .1          # Time to transfer 1GB on a 100 Mbps network
#       script.py .01 .05       # Time to transfer 10MB on a 50 Mbps network
#
##########################################################################################################

import sys

try:
    file_size_in_GB = float(sys.argv[1])
    #file_size_in_GB = 1000 # 1 GB
except:
    print('[ ERROR ] Error with data file size. Usage: script.py <file_size_in_GB> <data_transfer_speed_in_Gbps>')
    sys.exit()

try:
    data_transfer_speed_in_Gbps = float(sys.argv[2])
    #data_transfer_speed_in_Gbps = 1 # 1 Gbps
except:
    print('[ ERROR ] Error with data transfer speed param. Usage: script.py <file_size_in_GB> <data_transfer_speed_in_Gbps>')
    sys.exit()

#   MB_per_sec = Mbps / .008
#   GB_per_sec = Mbps / 8
#   TB_per_sec = Mbps / 8000

GB_per_sec = data_transfer_speed_in_Gbps / float(8)

time_to_transfer_in_seconds = file_size_in_GB * (1 / float(GB_per_sec)) 
time_to_transfer_in_seconds = time_to_transfer_in_seconds * 1.1 # 10% Overhead

print('[ INFO ] Time to transfer (seconds):  ' + str(round(time_to_transfer_in_seconds,4))               + ' seconds')
print('[ INFO ] Time to transfer (minutes):  ' + str(round(time_to_transfer_in_seconds/float(60),4))     + ' minutes')
print('[ INFO ] Time to transfer (hours):    ' + str(round(time_to_transfer_in_seconds/float(3600),4))   + ' hours')

#ZEND
