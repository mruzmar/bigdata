import subprocess




cmd="""hive -S -e "CREATE TABLE listings_raw (id string, listing_url string, picture_url string, host_id string, host_url string, amenities string
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ';' STORED AS TEXTFILE LOCATION '/home/info/';" """
print ("Ejecutando "+cmd)

output = subprocess.call(cmd, shell=True)


cmd="""hive -S -e "LOAD DATA INPATH '/datalake/airbnb/listings/listings_airbnb.csv' OVERWRITE INTO TABLE listings_raw;" """
print ("Ejecutando "+cmd)
output = subprocess.call(cmd, shell=True)

