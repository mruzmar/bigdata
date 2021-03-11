import subprocess


# Iniciamos los servicios Hadoop
cmd="start-all.sh"
print ("Ejecutando "+cmd)
subprocess.call(cmd, shell=True)

# pasamos fichero a stating
#cmd="wget http://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2021-02-08/data/listings.csv.gz"
#print ("Ejecutando "+cmd)
#subprocess.call(cmd, shell=True)

# Descomprensión del fichero gz
#cmd="gunzip listings.csv.gz listings.csv"
#print ("Ejecutando "+cmd)
#subprocess.call(cmd, shell=True)



# pasamos fichero a stating

cmd="rm listings_airbnb.csv"
print ("Ejecutando "+cmd)
subprocess.call(cmd, shell=True)

cmd="wget https://github.com/mruzmar/bigdata/raw/master/Hive/airbnb/listings_airbnb.csv"
print ("Ejecutando "+cmd)
subprocess.call(cmd, shell=True)

