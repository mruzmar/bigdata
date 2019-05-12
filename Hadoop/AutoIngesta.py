#!/usr/bin/env python
import commands
import datetime


now = datetime.datetime.now()
dateStr= str(now.year)+"_"+str(now.month)+"_"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)



c = commands.getoutput("wget https://github.com/hortonworks/data-tutorials/raw/master/tutorials/hdp/manage-files-on-hdfs-via-cli-ambari-files-view/assets/drivers-datasets/geolocation.csv")

c=commands.getoutput("hdfs dfs -mkdir -p /user/hadoop/geolocation ")

c=commands.getoutput("hdfs dfs -put geolocation.csv /user/hadoop/geolocation/geolocation"+dateStr+".csv")

c=commands.getoutput("hdfs dfs -ls /user/hadoop/geolocation")

print ("resultado "+c)