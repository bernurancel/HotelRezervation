import pymysql.cursors
from datetime import datetime
import time

print("""
----- Welcome to Hotel Reservation System! ----- 
----- Rezervasyon işlemi için giriş yapınız -----
      1-KAYIT OL
      2-GİRİŞ YAP
      3-ADMİN GİRİŞİ YAP
""") 

def kayit():
    connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject",port = 3306, cursorclass = pymysql.cursors.DictCursor)
    
    try:
      with connection.cursor() as cursor:
         
        Fname = input("Ad: ")
        Lname = input("Soyad: ")
        Email = input("Email: ")
        Password = input("Parola: ")
        Phone = input("Telefon: ")
        Address = input("Adres: ") 
        print("Başarıyla kayıt oldunuz.")
        print("Kullanıcı Adı: " +Email, "Parola: " +Password)
        sorgu = "INSERT INTO guests (Fname,Lname,Email,Password,Phone,Address) VALUES (%s,%s,%s,%s,%s,%s)"
     
        cursor.execute(sorgu,(Fname,Lname,Email,Password,Phone,Address))

        connection.commit()
            
    finally:
 
      connection.close()

def giris():
    Email = input("Email: ")
    Password = input("Parola: ")
    connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject",port = 3306, cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            findemail = "SELECT * FROM guests WHERE Email = %s"
            findpassword = "Select * from guests where Password = %s"
           

            cursor.execute(findemail,(Email,))
            cursor.execute(findpassword,(Password,))

            result = cursor.fetchall()
            if result:
                print("Hoşgeldiniz.")

            else:
                print("Kullanıcı adı veya şifre yanlış.")

        connection.commit()

        
    finally:
        connection.close()
    

def odagoster():
    connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject",port = 3306, cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM rooms WHERE Counter = 'Boş'")
            rooms = cursor.fetchall()
            for i in rooms:
                print("ODA NO: " + str(i['Number']) + " DÜZEY: " +str(i['Level']) + " STİL: " + i['Style'] + " YATAK SAYISI: " + str(i['Beds']) + " SİGARA: " + str(i['Smoking']) + " DURUM: " + i['Counter'])
                print("----------------------------------------------------------------------------")
        connection.commit()
    finally:
        connection.close()


def rezervasyonsil():
    connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject",port = 3306, cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            room = input("Çıkış yapmak için oda numaranızı giriniz: ")  
            findemail = "SELECT * FROM reservations WHERE RoomID = %s" 
            cursor.execute(findemail,(room,))
            result = cursor.fetchall()
            if result:
                sql = "DELETE FROM reservations WHERE RoomID = %s "
                cursor.execute(sql,(room,))
                
                time.sleep(2)
                print("Çıkış işlemi tamamlandı. ")
                update = "UPDATE rooms SET Counter = 'Boş' WHERE Number = %s"
                cursor.execute(update,(room,))
                
        connection.commit()
    finally:
        connection.close()
    
def rezervasyonyap():
    connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject",port = 3306, cursorclass = pymysql.cursors.DictCursor)
  
    try:
        with connection.cursor() as cursor:             
            Number = input("Rezervasyon için oda numarası giriniz: ")
            findroom = "Select * from rooms where Number = %s"
            cursor.execute(findroom,(Number,))
            result = cursor.fetchall()
            
            sorgu2 = "SELECT RoomID FROM reservations WHERE RoomID = %s"
            cursor.execute(sorgu2,(Number,))
            result2 = cursor.fetchall()
            if result2:
                print("BU ODA ALINAMAZ")
                print("Boş odalara dönüş yapılıyor")
                print("\n")
                time.sleep(2)
                odagoster()
            else:
                if result:

                    Kullanici = input("Onaylamak için emailinizi  giriniz: ")
                    sorgu = "SELECT * FROM guests WHERE Email = %s"
                    cursor.execute(sorgu,(Kullanici,))
                    result = cursor.fetchall()
                    if result:
                    
                        sorgu = "INSERT INTO reservations (GuestID,RoomID) SELECT LoginID,Number FROM guests,rooms WHERE Email = %s and Number = %s "
                        cursor.execute(sorgu,(Kullanici,Number))
                        update = "UPDATE rooms SET Counter = 'Dolu' WHERE Number = %s"
                        cursor.execute(update,(Number,))

                   
                    time.sleep(2)
                    print("Rezervasyon tamamlanmıştır")
                    
                else:
                    print("Emailiniz yanlış")
                    print("Boş olan odalarımıza dönüyorsunuz")
                    time.sleep(2)
                    odagoster()
                    rezervasyonyap()

            
        connection.commit()
    finally:
        connection.close()

def kullanicisil():
    KullaniciSil = input("Silmek istediğiniz kullanıcının mail adresini giriniz: ")
    connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject",port = 3306, cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            Sorgu = "SELECT * FROM Guests Where Email = %s "
            cursor.execute(Sorgu,(KullaniciSil,))
            result = cursor.fetchall()

            if result:
                Sorgu = "DELETE FROM Guests WHERE Email = %s "
                cursor.execute(Sorgu,(KullaniciSil,))
                time.sleep(2)
                print("Başarıyla silindi...")
            else:
                print("Böyle bir kullanıcı bulunmamaktadır...")
           

        connection.commit()
    finally:
        connection.close()   

def odasil():
    OdaSil = input("Silmek istediğiniz odanın numarasını giriniz: ")
    connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject",port = 3306, cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sorgu = "SELECT * FROM Rooms Where Number = %s"
            cursor.execute(sorgu,(OdaSil,))
            result = cursor.fetchall()

            if result:
                Sorgu = "DELETE FROM Rooms WHERE Number = %s "
                cursor.execute(Sorgu,(OdaSil,))
                time.sleep(2)
                print("Başarıyla silindi...")
            else:
                print("Böyle bir oda bulunmamaktadır...")    

        
        connection.commit()
    finally:
        connection.close()     






def admingirisi():
    AdminGirisi = input("Admin kullanıcı adını giriniz: ")
    AdminPassword = input("Admin şifresini giriniz: ")
    connection = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "hotelproject",port = 3306, cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            Sorgu = "SELECT * FROM Guests Where Email = %s and Password = %s" 
            cursor.execute(Sorgu,(AdminGirisi,AdminPassword))
            result = cursor.fetchall()

            if result:
                print("""
                
                1-Kullanıcı Sil
                2-Oda Sil
            
                 """)
                 
                islem = int(input("Yapmak istediğiniz işlemi seçin: "))

                if islem == 1:
                    kullanicisil()

                elif islem == 2:
                    odasil()

                else:
                    print("Geçersiz işlem...")
                    time.sleep(2)


        connection.commit()
    finally:
        connection.close()      


process = input("İşlem Seçiniz. ")
if process == "1":
    kayit()
    if kayit:
        print(""" 
            GİRİŞ BİLGİLERİNİ GİRİNİZ. 
            """)
        giris()
elif process == "2":
    giris()
    if giris:         
        print("""
        3- ODA ARA VE REZERVASYON YAP
        4- ODADAN AYRIL
        5- KULLANICI SİL
        """)
        islem = input("İseçiniz: ")
        if islem == "3":
            print("""
               BOŞ OLAN ODALARIMIZ   
            """)
            odagoster()
            print("\n")
            
            rezervasyonyap()
        elif islem == "4":
            rezervasyonsil()
        elif islem == "5":
            kullanicisil()  

        else:
            print("Sistemden çıkış yapılıyor... Hoşçakalın.")
            
            time.sleep(2)

elif process == "3":
    admingirisi()            
