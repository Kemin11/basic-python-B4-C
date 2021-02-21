#Membuat fungsi (tanpa parameter)
def fungsi_1():
    print("data dalam fungsi_1")

#Memanggil fungsi tanpa parameter
fungsi_1()

print("===============")

#Membuat Fungsi dengan parameter wajib
def fungsi_2(nama):
    print("Data fungsi_2 : " + nama)

#Memanggil fungsi dengan parameter
fungsi_2("Bambang")

print("===============")

#Membuat Fungsi dengan parameter opsional
def fungsi_3(nama=""):
    print("Data fungsi_3 : " + nama)

#Memanggil fungsi dengan parameter 
fungsi_3("Budi")
#Memanggil fungsi dengan tanpa parameter 
fungsi_3()

print("===============")

#Membuat Fungsi dengan parameter default
def fungsi_4(nama="Harun"):
    print("Data fungsi_4 : " + nama)

#Memanggil fungsi dengan parameter 
fungsi_4("Budi")
#Memanggil fungsi dengan parameter default
fungsi_4()

print("===============")

#Membuat Fungsi dengan keyword parameter
def fungsi_5(nama_depan, nama_belakang):
    print("Hallo {} {}".format(nama_depan,nama_belakang))

#Memanggil fungsi dengan tanpa keyword parameter 
fungsi_5("Budi", "Suseno")

#Memanggil fungsi dengan keyword parameter 
fungsi_5(nama_belakang= "Budi", nama_depan= "Suseno")

print("===============")
#return function
def fungsi_6(x):
    return 5 * x

print(fungsi_6(4))

print("===============")

#Function and list
buah = []                       #buat list

def tampil():                   #fungsi untuk menampilkan data
    for nama_buah in buah:
        print(nama_buah)
    print("---------")

def tambah(nama):               #fungsi untuk menambahkan data
    buah.append(nama)
    tampil()

tambah("Jeruk")
tambah("Apel")
tambah("Semongko")    
