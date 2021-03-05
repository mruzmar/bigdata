# Desarrollo de programa Python que descarga fichero log
# de una aplicación móvil. Se utiliza Hive
# como herramienta de análisis de los campos
# que se encuentran en dicho log ejecución de aplicación
import shlex, subprocess

# python3 -m pip install sqlalchemy
# conda install -c conda-forge sasl
# conda install -c conda-forge thrift_sasl


from sqlalchemy import create_engine



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


#Input Information
#/usr/local/apache-hive-3.1.2-bin/conf/hive-site.xml


host = 'localhost'
port = 10000
schema = 'default'
table = 'log4jLogs2'
engine = create_engine(f'hive://{host}:{port}/{schema}')

# Creamos tabla en Hive
#Execution
try:
	engine.execute('CREATE TABLE ' + table + ' (t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY " " STORED AS TEXTFILE LOCATION "/home/info/"  '  )
	#Data.to_sql(name=table, con=engine, if_exists='append')
except:
	print("Exception occurred CREATE TABLE")


# Cargamos el fichero en la tabla previamente cargada
engine.execute(' LOAD DATA INPATH "/datalake/logs/mobile/application1/sample.log" OVERWRITE INTO TABLE ' + table  )
#Data.to_sql(name=table, con=engine, if_exists='append')


# Seleccionamos los registros que han producido un error en al aplicación Móvil
query = ' SELECT * FROM ' + table  + ' WHERE t4 = "[ERROR]" '
connection = engine.connect()
results = connection.execute(query).fetchall()
for result in results:
	print(result)





