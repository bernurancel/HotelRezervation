import pymysql.cursors


connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject", cursorclass = pymysql.cursors.DictCursor)

try:
   with connection.cursor() as cursor:
    adding= "INSERT INTO guests  (Password,Fname,Lname,Email,Phone,Address) VALUES (1234,'Berfin','Gokmen','berfin@gmail.com',1234,'Bolu')"
    adding2= "INSERT INTO guests (Password,Fname,Lname,Email,Phone,Address) VALUES (123,'Bernur','Ancel','bernur@gmail.com',123,'Ankara')"
    adding3= "INSERT INTO guests (Password,Fname,Lname,Email,Phone,Address) VALUES (12378,'Büşra','Durak','busra@gmail.com',53300,'İstanbul')"
    adding4= "INSERT INTO guests (Password,Fname,Lname,Email,Phone,Address) VALUES (987, 'Yagmur' ,'Demir' , 'yagmur@gmail.com', 0101,'Adana')"
    adding5= "INSERT INTO guests (Password,Fname,Lname,Email,Phone,Address) VALUES (12345,'Asile','Gerek','asile@gmail.com',12345,'Adana')"
    adding6= "INSERT INTO guests (Password,Fname,Lname,Email,Phone,Address) VALUES (123456, 'Merve' ,'Bozkurt' , 'merve@gmail.com', 2727,'Gaziantep')"

    cursor = connection.cursor()
    cursor.execute(adding)
    cursor.execute(adding2)
    cursor.execute(adding3)
    cursor.execute(adding4)
    cursor.execute(adding5)
    cursor.execute(adding6)
    

    connection.commit()

finally:
    connection.close()
    print("MySQL connection is closes")

