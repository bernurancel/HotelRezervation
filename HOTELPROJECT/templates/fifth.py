import pymysql.cursors


connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject", cursorclass = pymysql.cursors.DictCursor)

try:
   with connection.cursor() as cursor:
    
   
    adding=  "INSERT INTO reservations (GuestID,RoomID,CheckIn,Checkout) SELECT LoginID, Number,  '2020-05-17',  '2020-05-17' From guests, rooms Where Email='berfin@gmail.com' and Number=1"
    adding2= "INSERT INTO reservations (GuestID,RoomID,CheckIn,Checkout) SELECT LoginID, Number,  '2020-06-17',  '2020-06-23' From guests, rooms Where Email='bernur@gmail.com' and Number=2"
    adding3= "INSERT INTO reservations (GuestID,RoomID,CheckIn,Checkout) SELECT LoginID, Number,  '2020-07-17',  '2020-07-20' From guests, rooms Where Email='busra@gmail.com' and Number=3"
    adding4= "INSERT INTO reservations (GuestID,RoomID,CheckIn,Checkout) SELECT LoginID, Number,  '2020-08-17',  '2020-08-21' From guests, rooms Where Email='yagmur@gmail.com' and Number=4"
    adding5= "INSERT INTO reservations (GuestID,RoomID,CheckIn,Checkout) SELECT LoginID, Number,  '2020-09-17',  '2020-09-18' From guests, rooms Where Email='asile@gmail.com' and Number=7"
    adding6= "INSERT INTO reservations (GuestID,RoomID,CheckIn,Checkout) SELECT LoginID, Number,  '2020-10-17',  '2020-10-19' From guests, rooms Where Email='merve@gmail.com' and Number=6"

    sorgu= "UPDATE rooms SET Counter = 'Dolu' Where Number = 1" 
    sorgu1="UPDATE rooms SET Counter = 'Dolu' Where Number = 2"
    sorgu2="UPDATE rooms SET Counter = 'Dolu' Where Number = 3"
    sorgu3="UPDATE rooms SET Counter = 'Dolu' Where Number = 4"
    sorgu4="UPDATE rooms SET Counter = 'Dolu' Where Number = 6"
    sorgu5="UPDATE rooms SET Counter = 'Dolu' Where Number = 7"  

    cursor = connection.cursor()

    cursor.execute(adding)
    cursor.execute(adding2)
    cursor.execute(adding3)
    cursor.execute(adding4)
    cursor.execute(adding5)
    cursor.execute(adding6)
    
    cursor.execute(sorgu)
    cursor.execute(sorgu1)
    cursor.execute(sorgu2)
    cursor.execute(sorgu3)
    cursor.execute(sorgu4)
    cursor.execute(sorgu5)


    connection.commit()

finally:
    connection.close()
    print("MySQL connection is closes")

