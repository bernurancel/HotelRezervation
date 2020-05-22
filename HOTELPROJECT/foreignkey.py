import pymysql.cursors
connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject",port = 3306, cursorclass = pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:

        sorgu1="ALTER TABLE reservations ADD COLUMN RoomID INT"
        sorgu = "ALTER TABLE reservations ADD FOREIGN KEY (RoomID) REFERENCES rooms(Number)"
        sorgu2 = "ALTER TABLE reservations ADD FOREIGN KEY (GuestID) REFERENCES guests(LoginID)"
        cursor.execute(sorgu1)
        cursor.execute(sorgu)
        cursor.execute(sorgu2)

       
        connection.commit()
finally:
     connection.close()