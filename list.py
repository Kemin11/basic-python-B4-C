myList = [4, 5.8, "Ayam"]

#Menambahkan data
myList.append(1)
myList.append(2)
myList.append(3)

print(myList)       #Memanggil data list keseluruhan
print(myList[0])    #Memanggil data list sesuai urutan
print(myList[:3])   #Memanggil data list sesuai range

#Memanggil data satu per satu
for x in myList:
    print(x)