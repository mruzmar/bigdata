import subprocess

def run_hive_query(query):
    logging.debug("Running query: %s" % (query))
    try:
        proc = subprocess.Popen(["hive -e \"%s\"" % (query)], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
    except:
        raise Exception('Failure in running query: %s!' % (query))

    logging.debug(out)
    logging.debug("\nreturncode: " + str(proc.returncode))
    return proc.returncode, str(out.decode('ascii'))
  


# pasamos fichero a stating
cmd="wget https://download.microsoft.com/download/7/F/3/7F35E2C0-B84F-4B45-A9F2-2A888D51C1D9/sample.log"
print ("Ejecutando "+cmd)
output = subprocess.check_output(cmd)

cmd="hdfs dfs -mkdir -p /datalake/logs/mobile/application1"
print ("Ejecutando "+cmd)
output = subprocess.check_output(cmd)


cmd="hdfs dfs -put sample.log /datalake/logs/mobile/application1/"
print ("Ejecutando "+cmd)
output = subprocess.check_output(cmd)



cmd="""hive -S -e "CREATE EXTERNAL TABLE log4jLogs (t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY \" \" STORED AS TEXTFILE LOCATION \"/home/info/\";" """
print ("Ejecutando "+cmd)
output = subprocess.check_output(cmd)




cmd="""hive -S -e "LOAD DATA INPATH '/datalake/logs/mobile/application1/sample.log' OVERWRITE INTO TABLE log4jLogs;" """
print ("Ejecutando "+cmd)
output = subprocess.check_output(cmd)


cmd = """ hive -S -e "SELECT * FROM log4jLogs WHERE t4 = '[ERROR]';" """
print ("Ejecutando "+cmd)
output = subprocess.check_output(cmd)

print (output)


