#Import package
import getpass, smtplib, ssl, email

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

dataEmail = []  #data email dari file

#Menu
def menu():
    print()
    print("=== MENU ===")
    print("1. Daftar email")
    print("2. Kirim email")
    print("3. Keluar")
    pilihanMenu = input("Pilih menu : ")

    if pilihanMenu == "1":
        tampil()
    elif pilihanMenu == "2":
        kirim()
    elif pilihanMenu == "3":
        keluar()
    else:
        print("Pilihan menu tidak tersedia, silahkan pilih menu kembali")
        menu()

#Menampilkan daftar email
def tampil():
    print()
    print("=== Daftar Email Penerima ===")            
    data = open("receiver_list.txt", "r")
    bacaData = data.readlines()
    banyakData = len(bacaData)
    if banyakData != 0:
        for x in range(banyakData):
            print("Email {} :".format(x), bacaData[x][:-1])
            data.close()
    else:
        print("Daftar email kosong, silahkan tambah email terlebih dahulu")
        data.close()

    print()
    print("=== Opsi ====") 
    print("1. Tambah email")
    print("2. Ubah email")
    print("3. Hapus email")
    print("4. Menu sebelumnya")
    opsi = input("Pilih opsi : ")

    if opsi == "1":
        tambah()
    elif opsi == "2":
        ubah()    
    elif opsi == "3":
        hapus()
    elif opsi == "4":
        menu()
    else:
        print("Pilihan menu tidak tersedia, silahkan pilih menu kembali")
        tampil()        

#Menambahkan email
def tambah():
    print()
    print("=== Tambah Email Penerima ===")
    data = open("receiver_list.txt", "a")        
    emailBaru = input("Masukkan email : ")
    print("Email : ", emailBaru)
    pilihanTambah = input("Simpan email? Y/N : ")
    if pilihanTambah == "Y":
        data.write(emailBaru + "\n")
        data.close()
        print("Email berhasil ditambahkan")
        ekstrakData()  
        tampil()               
    elif pilihanTambah == "N":
        tampil()
    else:
        print("Pilihan tidak tersedia")
        tambah()

#Menghapus email
def hapus():
    print()
    print("=== Hapus Email Penerima ===")
    indexEmail = int(input("Nomor email yang ingin dihapus : "))
    print("Email yang akan dihapus : ", dataEmail[indexEmail])
    pilihanHapus = input("Hapus email? Y/N : ")
    if pilihanHapus == "Y":
        dataEmail.pop(indexEmail)
        data = open("receiver_list.txt", "w")        
        for x in range(len(dataEmail)):
            data.write(dataEmail[x] + "\n")
        data.close()
        print("Email berhasil dihapus")
        tampil()
    elif pilihanHapus == "N":
        tampil()
    else:
        print("Pilihan tidak tersedia")
        hapus()

#Mengubah email
def ubah():
    print()
    print("=== Ubah Email Penerima ===")
    indexEmail = int(input("Nomor email yang ingin diubah : "))
    dataEmail[indexEmail] = input("Email yang baru : ")
    pilihanUbah = input("Ubah email? Y/N : ")
    if pilihanUbah == "Y":
        data = open("receiver_list.txt", "w")        
        for x in range(len(dataEmail)):
            data.write(dataEmail[x] + "\n")
        data.close()
        print("Email berhasil diubah")
        tampil()
    elif pilihanUbah == "N":
        tampil()
    else:
        print("Pilihan tidak tersedia")
        ubah() 

#Keluar program
def keluar():
    print("Terimakasih")

#Kirim email
def kirim():
    print()
    print("=== Kirim email ===")
    print("Pilih mode pengiriman")
    print("1. Personal")
    print("2. Broadcast")
    print("3. Menu sebelumnya")
    mode = input("Pilih Mode : ")

    if mode == "1":
        print()
        print("Mode kirim personal")
        personal()
    elif mode == "2":
        print()
        print("Mode kirim broadcast")
        broadcast()
    elif mode == "3":
        menu()
    else:
        print("Plihan mode tidak tersedia, silahkan pilih mode")
        kirim()

#Kirim email mode personal
def personal():
    pengirim = input("Pengirim : ")
    password = getpass.getpass(prompt="Password : ", stream=None)        
    print("=== Pilih Penerima ===")            
    data = open("receiver_list.txt", "r")
    bacaData = data.readlines()
    banyakData = len(bacaData)
    if banyakData != 0:
        for x in range(banyakData):
            print("Email {} :".format(x), bacaData[x][:-1])
            data.close()
    else:
        print("Daftar email kosong, silahkan tambah email terlebih dahulu")
        data.close()
    indexEmail = int(input("Pilih penerima : "))

    penerima = dataEmail[indexEmail]
    subject = input("Subject : ")
    body = input("Body : ")

    pesan = MIMEMultipart()
    pesan["From"] = pengirim
    pesan["To"] = penerima
    pesan["Subject"] = subject
    pesan["Bcc"] = penerima

    pesan.attach(MIMEText(body, "plain"))

    print("Ingin lampirkan file? Y untuk lampirkan, N untuk tidak")
    lampiran = input("Lampirkan file? Y/N : ")
    if lampiran == "Y":
        namaLampiran = input("Nama file (exp : laporan.pdf): ")
        with open(namaLampiran, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename = {namaLampiran}",)
        pesan.attach(part)
        text =  pesan.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(pengirim, password)
            server.sendmail(pengirim, penerima, text)
        menu()
    elif lampiran == "N":
        text =  pesan.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(pengirim, password)
            server.sendmail(pengirim, penerima, text)
        menu()
    else:
        print("Pilihan tidak tersedia")
        kirim()

#Kirim email mode broadcast
def broadcast():
    pengirim = input("Pengirim : ")
    password = getpass.getpass(prompt="Password : ", stream=None)        
    print("=== Daftar Penerima ===")            
    data = open("receiver_list.txt", "r")
    bacaData = data.readlines()
    banyakData = len(bacaData)
    if banyakData != 0:
        for x in range(banyakData):
            print("Email {} :".format(x), bacaData[x][:-1])
            data.close()
    else:
        print("Daftar email kosong, silahkan tambah email terlebih dahulu")
        data.close()

    subject = input("Subject : ")
    body = input("Body : ")

    print("Ingin lampirkan file? Y untuk lampirkan, N untuk tidak")
    lampiran = input("Lampirkan file? Y/N : ")
    if lampiran == "Y":
        namaLampiran = input("Nama file (exp : laporan.pdf): ")
        for x in dataEmail:
            penerima = x
        
            pesan = MIMEMultipart()
            pesan["From"] = pengirim
            pesan["To"] = penerima
            pesan["Subject"] = subject
            pesan["Bcc"] = penerima

            pesan.attach(MIMEText(body, "plain"))

            with open(namaLampiran, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename = {namaLampiran}",)
            pesan.attach(part)
            text =  pesan.as_string()
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(pengirim, password)
                server.sendmail(pengirim, penerima, text)
        menu()
    elif lampiran == "N":
        for x in dataEmail:
            penerima = x

            pesan = MIMEMultipart()
            pesan["From"] = pengirim
            pesan["To"] = penerima
            pesan["Subject"] = subject
            pesan["Bcc"] = penerima

            pesan.attach(MIMEText(body, "plain"))
            text =  pesan.as_string()
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(pengirim, password)
                server.sendmail(pengirim, penerima, text)
        menu()
    else:
        print("Pilihan tidak tersedia")
        kirim()

#Mengambil email dari file dimasukkan ke dalam list
def ekstrakData():
    dataEmail.clear()
    data = open("receiver_list.txt", "r")
    bacaData = data.readlines()
    banyakData = len(bacaData)
    for x in range(banyakData):
        dataEmail.append(bacaData[x][:-1])
    data.close()
    #print(dataEmail)

print("Selamat Datang")
ekstrakData()
menu()

#Referensi
#https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development
#https://www.w3schools.com/python/default.asp
#https://docs.python.org/3/library/getpass.html
#https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/