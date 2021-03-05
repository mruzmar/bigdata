# Desarrollo de programa Python que descarga fichero log
# de una aplicación móvil. Se utiliza Hive
# como herramienta de análisis de los campos
# que se encuentran en dicho log ejecución de aplicación
import shlex, subprocess

# python3 -m pip install pyhive
from pyhive import hive

host_name = "localhost"
port = 10000  #default is 10000
user = "" # user name  
password = "" # pass 
database="default"

def hiveconnection(host_name, port, user,password, database):
    conn = hive.Connection(host=host_name, port=port, username=user,password=password,database=database, auth='CUSTOM')
    cur = conn.cursor()
    cur.execute('select * from log4jLogs limit 2')
    result = cur.fetchall()

    return result

# Call above function
output = hiveconnection(host_name, port, user,password, database)
print(output) 

exit()

# Sel fichero existiera al descargar lo renombra, así que borramos antes el fichero
cmd="rm sample.log"
print ("Ejecutando "+cmd)
# Ejecución del comando a través del shell
subprocess.call(cmd, shell=True)

# pasamos fichero a stating
cmd="wget https://download.microsoft.com/download/7/F/3/7F35E2C0-B84F-4B45-A9F2-2A888D51C1D9/sample.log"
print ("Ejecutando "+cmd)
subprocess.call(cmd, shell=True)


# Creación del directorio en nuestro DataLake
cmd="hdfs dfs -mkdir -p /datalake/logs/mobile/application1"
print ("Ejecutando "+cmd)
output = subprocess.call(cmd, shell=True)


# Ingestamos fichero descargado en el directorio, opción -f para hacer overwrite
cmd="hdfs dfs -put -f sample.log /datalake/logs/mobile/application1/"
print ("Ejecutando "+cmd)
output = subprocess.call(cmd, shell=True)


# Creamos tabla en Hive
cmd="""hive -S -e "CREATE EXTERNAL TABLE log4jLogs (t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' STORED AS TEXTFILE LOCATION '/home/info/';" """
print ("Ejecutando "+cmd)

output = subprocess.call(cmd, shell=True)


# Cargamos el fichero en la tabla previamente cargada
cmd="""hive -S -e "LOAD DATA INPATH '/datalake/logs/mobile/application1/sample.log' OVERWRITE INTO TABLE log4jLogs;" """
print ("Ejecutando "+cmd)
subprocess.call(shlex.split(cmd))


# Seleccionamos los registros que han producido un error en al aplicación Móvil
cmd = """ hive -S -e "SELECT * FROM log4jLogs WHERE t4 = '[ERROR]';" """
print ("Ejecutando "+cmd)
subprocess.call(shlex.split(cmd))


print (output)


