def inputData():
    data = open("kontak.txt", "a")
    nama = input("Masukkan nama : ")
    nomor = input("Masukkan nomor : ")

    data.write(nama + "\n")
    data.write(nomor + "\n")
    data.close()

def tampil():
    data = open("kontak.txt", "r")
    bacaData = data.readlines()
    for x in range(0,len(bacaData),2):
        print("Nama ", bacaData[x])
        print("Nomor ", bacaData[x+1])
    data.close()

inputData()
tampil()