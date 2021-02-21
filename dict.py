pelanggan = {
#   "keys" : "value"    
    "nama" : "budi",
    "umur" : "23",
}

#Mengakses value berdasarkan keys
print(pelanggan)
print("Nama : {}".format(pelanggan["nama"]))
print("Umur : {}".format(pelanggan["umur"]))

print("================")

#Ganti nilai dalam dict
pelanggan["nama"] = "Bambang"
print("Nama : {}".format(pelanggan["nama"]))
print("Umur : {}".format(pelanggan["umur"]))

print("================")

#For loop dalam dict
for x in pelanggan:
    print(x)                #print keys
    print(pelanggan[x])     #print value

print("================")

#Menampilkan value
for x in pelanggan.values():
    print(x)

print("================")

#Menampilkan keys
for x in pelanggan.keys():
    print(x)

print("================")    

#Memasukkan Dict dalam list
pelanggan2 = {
    "nama" : "Eko",
    "umur" : "32"
}
daftar_pelanggan = []               #dict
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan2)

print(daftar_pelanggan)