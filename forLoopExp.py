data_nama = []
data_umur = []

banyak_data = int(input("Masukkan banyak data yang ingin di input : "))

for x in range(banyak_data):
    nama = input("Masukkan nama anda : ")
    umur = int(input("Masukkan umur anda : "))
    data_nama.append(nama)
    data_umur.append(umur)

for x in range(len(data_nama)):
    print("Nama {} berumur {}".format(data_nama[x], data_umur[x]))