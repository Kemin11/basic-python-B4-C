a = "Hello, world!"

#Memanggil sesuai urutan Index
print(a[0])     
print(a[4])

#Memanggil dengan batasan
print(a[:3])
print(a[7:12])

#Mencari panjang String
print(len(a))

b = "Hello"
c = "World"

#Penggabungan String
d = b + c
print(d)

e = b + " " + c
print(e)

#Formating
umur = 23
tinggi = 170.32
txt = "Umur saya {} dan tinggi saya {:.2f}" .format(umur,tinggi)
print(txt)