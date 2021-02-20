#continue --> mengabaikan atau melewati variabel yang ditentukan jika statement terpenuhi
for i in range(5):
    if i == 3:
        continue
    print(i)

print("===========")

nilai = [100,45,70,65,80]
for i in nilai:
    if i < 70:
        continue
    print("Nilai {} = lulus".format(i))

print("===========")

#break --> keluar dari perulangan ketika statement terpenuhi
for a in range(10):
    if a == 5:
        break
    print(a)

print("===========")    

#continue and break
for a in range(10):
    if a == 3:
        continue
    if a ==7:
        break
    print(a)