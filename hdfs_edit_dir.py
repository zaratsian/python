
################################################################################################################
#
#   Script to edit HDFS directory names (built to be edited for other uses)
#
#   Usage: script.py <hdfs_directory>
#
################################################################################################################

import subprocess,re
import time
import sys

try:
    hdfs_directory = sys.argv[1]
except:
    print('[ ERROR ] Usage script.py <hdfs_directory>')
    sys.exit()

p = subprocess.Popen(['hadoop', 'fs', '-ls', hdfs_directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = p.communicate()

files = stdout.split('\n')
files = [re.findall(hdfs_directory+'.+', file)[0] for file in files if re.search(hdfs_directory, file)]
files = [file for file in files if re.search(' ',file)]

for file in files:
    olddir = file
    newdir = file.replace(' ','_')
    print('[ INFO ] Replacing "' + olddir + '" with "' + newdir + '"')
    time.sleep(3)
    subprocess.Popen(['hadoop','fs','-mv',olddir,newdir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


#ZEND
