import pymysql.cursors

connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject", cursorclass = pymysql.cursors.DictCursor)

try: 
   with connection.cursor() as cursor:
    sqlQuery = "CREATE TABLE IF NOT EXISTS guests( LoginID INT PRIMARY KEY, Password INT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Email TEXT NOT NULL, Phone INT NOT NULL, Address TEXT)"
    sqlQuery2 = "CREATE TABLE IF NOT EXISTS rooms(Number INT PRIMARY KEY , Level INT , Style TEXT,  Beds INT,Smoking BOOLEAN) "
    sqlQuery3 = "CREATE TABLE IF NOT EXISTS reservations(ResNumber INT PRIMARY KEY, CheckIn DATETIME, CheckOut DATETIMe,GuestID INT)"
          
    cursor.execute(sqlQuery)
    cursor.execute(sqlQuery2)
    cursor.execute(sqlQuery3)
         
finally:
    connection.close()
