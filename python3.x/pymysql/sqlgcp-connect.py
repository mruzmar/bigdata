import pymysql

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             db='ejemplo')

sql="CREATE TABLE `users` (\
    `id` int(11) NOT NULL AUTO_INCREMENT,\
    `email` varchar(255) COLLATE utf8_bin NOT NULL,\
    `password` varchar(255) COLLATE utf8_bin NOT NULL,\
    PRIMARY KEY (`id`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin \
AUTO_INCREMENT=1 ;"

with connection.cursor() as cursor:
        # create table
        cursor.execute(sql, ())

with connection.cursor() as cursor:
    # Create a new record
    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

with connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    cursor.execute(sql, ('webmaster@python.org',))
    result = cursor.fetchone()
    print(result)                                         