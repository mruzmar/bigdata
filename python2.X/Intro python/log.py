from datetime import datetime, timedelta
import time
import hashlib
import hmac
import base64
import urllib.request
import urllib.parse
import json
from pip._vendor import requests
import pypyodbc
import pandas as pd
import urllib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib

import logging


def enviarMailError(texto,emailto):
    username = "@correo
    password = "xxxxxxx"
    print ("Conectando.....")


    msg = MIMEMultipart()
    msg['Subject'] = "Error conexión "
    msg['From'] = username
    msg['Reply-to'] = emailto
    msg.preamble = 'Multipart massage.\n'

    part = MIMEText(texto)
    msg.attach(part)



    server = smtplib.SMTP("smtp.servidor.com")
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(msg['From'], emailto , msg.as_string())
    server.quit()
    print ("Email enviado")



try:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # create a file handler
    handler = logging.FileHandler("/Users/xxxx/log-proceso.log")
    handler.setLevel(logging.INFO)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)

    logger.info('Init conexion_CRM')

    connection = pypyodbc.connect('Driver={SQL Server};'
                                  'Server=xxxxx;'
                                  'Database=db_YYYY;'
                                  'uid=usuario;pwd=password')
    cursor = connection.cursor()


    sql="select idAlcance,FinLanzamiento from opinator.Alcances where datediff(m,FinLanzamiento,getdate())>=2 and IdAlcance not in (select idAlcance from [temp].[Informes_Profesores])  and nameOrigin='-ASIGTEORICA'"

    cursor.execute(sql)

    fecha2 = datetime.now()
    fechaA = str(format(fecha2, "%Y%m%d"))
    fechaA = str(fechaA)

    for row in cursor.fetchall():
	print ("dato 0 "+str(row[0]))


    connection.close()


except Exception as e:
    print("Oops!  error..." + str(e))
    logger.error('Error....' + str(e))
    enviarMailError(str(e),'miguelruz@campus.eae.es')
