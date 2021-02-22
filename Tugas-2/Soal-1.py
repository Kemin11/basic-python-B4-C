daftar_nama = []        #Inisialisasi list untuk menyimpan data nama
daftar_nomor = []       #Inisialisasi list untuk menyimpan data nomor

#membuat fungsi daftar
def daftar():
    panjang_data = len(daftar_nama)                 #menghitung jumlah data
    if panjang_data == 0:
        print("Data kosong, silahkan masukkan kontak")
        print("================")
        menu()                                      #kembali ke menu
    else:
        for x in range(panjang_data):               #membuka data sebanyak panjang data
            print("Data Kontak")
            print("Nama : ", daftar_nama[x])
            print("Nomor telepon : ", daftar_nomor[x])
            print("---------------")
        print("================")
        menu()                                      #kembali ke menu
        
#membuat fungsi tambah        
def tambah():
    nama = input("Masukkan nama kontak : ")         #Input data nama
    nomor = input("Masukkan nomor telepon : ")      #Input data nomor
    daftar_nama.append(nama)                        #menambahkan data ke dalam list nama
    daftar_nomor.append(nomor)                      #menambahkan data ke dalam list nomor
    print("Kontak berhasil ditambahkan")
    print("================")
    menu()                                          #kembali ke menu

#membuat fungsi keluar
def keluar():
    print("Program selesai, Terimakasih")

#membuat fungsi menu
def menu():
    print("-- Menu --")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    pilihan = input("Pilih Menu : ")                #Input pilihan (data berupa string)

    if pilihan == '1':                              #'1' karena tipe data string (bisa pakai "1")
        daftar()
    elif pilihan == '2':
        tambah()
    elif pilihan == '3':
        keluar()
    else:                                           #Jika input tidak sesuai menu
        print("Menu tidak tersedia, silahkan pilih menu")
        menu()                                      #kembali ke menu

print("Selamat Datang, silahkan pilih menu")
menu()                                              #memanggil fungsi menu