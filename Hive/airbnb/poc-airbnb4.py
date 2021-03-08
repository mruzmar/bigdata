



cmd = """ hive -S -e "SELECT picture_url FROM listings_raw limit 1;" """
print ("Ejecutando "+cmd)
output = subprocess.check_output(cmd, shell=True)
output = str(output.decode("utf-8"))



#Descargamos la imagen del alojamiento
cmd="wget "+str(output)
print ("Ejecutando "+cmd)
subprocess.call(cmd, shell=True)

file_name = output.split('/')[-1]
file_name= file_name.rstrip("\n")
print ("Nombre del fichero de la imagen: "+"./"+file_name)

import io
import os
# Imports the Google Cloud client library
# conda install -c conda-forge google-cloud-vision
# Imports the Google Cloud client library
# Hay que hacer en Linux 
# export GOOGLE_APPLICATION_CREDENTIALS="/home/template/work-bigdata/Proyecto EAE-517b6a6a592f.json"
from google.cloud import vision
from google.cloud.vision import types
# Instantiates a client
client = vision.ImageAnnotatorClient()
# The name of the image file to annotate


# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
image = types.Image(content=content)
# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations
print('Labels:')
for label in labels:
    print(label.description)



