import pymysql.cursors

connection = pymysql.connect(host = "localhost", user = "root" , port = 3306, password = "")

try:
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS hotelproject")
finally:
    
    connection.close() 
