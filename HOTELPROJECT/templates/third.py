import pymysql.cursors


connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject", cursorclass = pymysql.cursors.DictCursor)

try:
   with connection.cursor() as cursor:
    adding= "INSERT INTO rooms  (Level,Style,Beds,Smoking,Counter) VALUES (1,'Suit',1,True,'Boş')"
    adding2= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (2,'Suit',2,True,'Boş')"
    adding3= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (3,'Normal',3,True,'Boş')"
    adding4= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (4,'Normal',3,False,'Boş')"
    adding5= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (5,'Normal',3,False,'Boş')"
    adding6= "INSERT INTO rooms  (Level,Style,Beds,Smoking,Counter) VALUES (11,'Suit',1,True,'Boş')"
    adding7= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (12,'Suit',2,True,'Boş')"
    adding8= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (13,'Normal',3,True,'Boş')"
    adding9= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (14,'Normal',3,False,'Boş')"
    adding10= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (15,'Normal',3,False,'Boş')"
    adding11= "INSERT INTO rooms  (Level,Style,Beds,Smoking,Counter) VALUES (21,'Suit',1,True,'Boş')"
    adding12= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (22,'Suit',2,True,'Boş')"
    adding13= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (23,'Normal',3,True,'Boş')"
    adding14= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (24,'Normal',3,False,'Boş')"
    adding15= "INSERT INTO rooms (Level,Style,Beds,Smoking,Counter) VALUES (25,'Normal',3,False,'Boş')"

    cursor = connection.cursor()
    cursor.execute(adding)
    cursor.execute(adding2)
    cursor.execute(adding3)
    cursor.execute(adding4)
    cursor.execute(adding5)
    cursor.execute(adding6)
    cursor.execute(adding7)
    cursor.execute(adding8)
    cursor.execute(adding9)
    cursor.execute(adding10)
    cursor.execute(adding11)
    cursor.execute(adding12)
    cursor.execute(adding13)
    cursor.execute(adding14)
    cursor.execute(adding15)
    

    connection.commit()

finally:
    connection.close()
    print("MySQL connection is closes")

