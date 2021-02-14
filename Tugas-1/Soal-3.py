teori = int(input("Masukan nilai teori : "))
praktek = int(input("Masukan nilai praktek : "))
batas = 70

if teori >= batas and praktek >= batas:
    print("Selamat, anda lulus!")
elif teori >= batas and praktek < batas:
    print("Anda harus mengulang ujian praktek")
elif teori < batas and praktek >= batas:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")
