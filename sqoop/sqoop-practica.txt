

cmd="hdfs dfsadmin -safemode leave"
print ("Ejecutando "+cmd)
output = subprocess.call(cmd, shell=True)

cmd="hdfs dfs -mkdir -p /datalake/airbnb/listings"
print ("Ejecutando "+cmd)
output = subprocess.call(cmd, shell=True)


cmd="hdfs dfs -put listings_airbnb.csv /datalake/airbnb/listings/"
print ("Ejecutando "+cmd)
output = subprocess.call(cmd, shell=True)

