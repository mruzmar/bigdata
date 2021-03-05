from pyhive import hive

host_name = "localhost"
port = 10000  #default is 10000
user = "" # user name mysql 
password = "" # pass mysql
database="default"

def hiveconnection(host_name, port, user,password, database):
    conn = hive.Connection(host=host_name, port=port, username=user,password=password,
                           database=database, auth='CUSTOM')
    cur = conn.cursor()
    cur.execute('select name  from demo2 return limit 2')
    result = cur.fetchall()

    return result

# Call above function
output = hiveconnection(host_name, port, user,password, database)
print(output) 

