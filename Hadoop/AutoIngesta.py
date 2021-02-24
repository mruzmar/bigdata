#!/usr/bin/env python
#import commands
#A partir de python 3.X sustituimos por subprocess
import subprocess
import datetime


now = datetime.datetime.now()
dateStr= str(now.year)+"_"+str(now.month)+"_"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)


print ("Recogiendo datos geolocation......")
c = subprocess.getoutput("wget https://github.com/hortonworks/data-tutorials/raw/master/tutorials/hdp/manage-files-on-hdfs-via-cli-ambari-files-view/assets/drivers-datasets/geolocation.csv")

print ("hdfs dfs -mkdir -p /user/hadoop/geolocation......")
c=subprocess.getoutput("hdfs dfs -mkdir -p /user/hadoop/geolocation ")

print ("hdfs dfs -put geolocation.csv /user/hadoop/geolocation/geolocation"+dateStr+".csv")
c=subprocess.getoutput("hdfs dfs -put geolocation.csv /user/hadoop/geolocation/geolocation"+dateStr+".csv")

print ("hdfs dfs -ls /user/hadoop/geolocation")
c=subprocess.getoutput("hdfs dfs -ls /user/hadoop/geolocation")

print ("resultado "+c)