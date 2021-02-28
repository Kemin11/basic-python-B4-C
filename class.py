#Membuat Class
class myClass:
    x = 10
    y = 5

p1 = myClass()          #membuat object
print(p1.x)
print(p1.y)

print("===============")

#Class dengan init
class person:
    #contruction
    def __init__ (self,nama,umur):      
        self.nama = nama
        self.umur = umur

p1 = person("Budi", 22)        
p2 = person("Ani", 23)

print(p1.nama)
print(p2.umur)

print("===============")

#Object method
class hewan:
    #contruction
    def __init__ (self,nama,jenis):
        self.nama = nama
        self.jenis = jenis
    
    #method
    def tampil(self):
        print("Nama hewan : ", self.nama)
        print("Jenis : " + self.jenis)

a = hewan("Kucing", "Herbivora")        
b = hewan("Macan", "Karnivora")

a.tampil()
print("-----------")
b.tampil()

print("===============")

#Inheritance (Penurunan class)
class special_id(person):
    def __init__ (self, nama, umur, alamat, status):
        self.alamat = alamat
        self.status = status
        person.__init__(self,nama,umur)
        #Penurunan sifat
    def cetak(self):
        print(self.nama)
        print(self.umur)
        print(self.alamat)
        print(self.status)

d1 = special_id("Wawan", 34, "Bandung", "Jomblo")
d1.cetak()
