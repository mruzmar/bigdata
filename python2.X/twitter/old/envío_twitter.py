#!/usr/bin/python
import twitter
import datetime

now = datetime.datetime.now()

with open('lista.txt', 'r') as f:
  first_line = f.readline()
  first_line = first_line.strip('\n')
  print first_line
f.close()

logfile = open('procesados.txt','a')
fecha=now.strftime("%Y-%m-%d_%H:%M:%S")
logfile.write(fecha + ' ' + first_line + '\n')
logfile.close()

#send tweet
api = twitter.Api(consumer_key='',
  consumer_secret='',
  access_token_key='',
  access_token_secret='')

status = api.PostUpdate(first_line)
print status.text

#removing status from queue
lines = open('lista.txt').readlines()
open('lista.txt', 'w').writelines(lines[1:])
