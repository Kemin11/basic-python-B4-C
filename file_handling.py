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
    
    for x in range(len(bacaData)):
        print(bacaData[x][:-1])
    
    for y in range(0,len(bacaData),2):
        print("Nama {}, nomor {}".format(bacaData[y][:-1], bacaData[y+1]))
    data.close()

inputData()
tampil()