import commands


# pasamos fichero a stating
cmd="wget https://download.microsoft.com/download/7/F/3/7F35E2C0-B84F-4B45-A9F2-2A888D51C1D9/sample.log"
print ("Ejecutando "+cmd)
status, output = commands.getstatusoutput(cmd)

cmd="hdfs dfs -mkdir -p /datalake/logs/mobile/application1"
print ("Ejecutando "+cmd)
status, output = commands.getstatusoutput(cmd)


cmd="hdfs dfs -put sample.log /datalake/logs/mobile/application1/"
print ("Ejecutando "+cmd)
status, output = commands.getstatusoutput(cmd)



cmd="""hive -S -e "CREATE EXTERNAL TABLE log4jLogs (t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY " " STORED AS TEXTFILE LOCATION "/home/info/";" """
print ("Ejecutando "+cmd)

status, output = commands.getstatusoutput(cmd)

cmd="""hive -S -e "LOAD DATA INPATH '/datalake/logs/mobile/application1/sample.log' OVERWRITE INTO TABLE log4jLogs;" """
print ("Ejecutando "+cmd)
status, output = commands.getstatusoutput(cmd)

cmd = "hive -S -e 'SELECT * FROM log4jLogs WHERE t4 = \"[ERROR]\";'"
print ("Ejecutando "+cmd)
status, output = commands.getstatusoutput(cmd)
if status == 0:
	print output
else:
	print "error"

