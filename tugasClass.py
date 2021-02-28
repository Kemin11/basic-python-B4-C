#Membuat class
class data:
    def __init__(self):
        nama = input("Masukkan nama : ")
        jurusan = input("Masukan jurusan : ")
        self.nama = nama
        self.jurusan = jurusan
    def tampil(self):
        print("{} jurusan {}".format(self.nama,self.jurusan))

#Input data
mahasiswa1 = data()
mahasiswa2 = data()
mahasiswa3 = data()
print()

#Menampilkan data
mahasiswa1.tampil()
mahasiswa2.tampil()
mahasiswa3.tampil()