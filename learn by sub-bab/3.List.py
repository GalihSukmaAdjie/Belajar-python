# data dalam list 1,2,3
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

# ==============================================================================================
print("=========================================================================================")
# mencetak data satu per satu
print("⬇⬇⬇ mencetak data satu dengan mengakses alamat ⬇⬇⬇")
print(mylist[0]) # cetak data pertama
print(mylist[1]) # cetak data kedua
print(mylist[2]) # cetak data ketiga

# ==============================================================================================
print("=========================================================================================")
# mencetak data semua sekaligus
print("⬇⬇⬇ mencetak semua isi data ⬇⬇⬇")
for x in mylist:
    print(x)

# # ==============================================================================================
# print("=========================================================================================")
# # mengakses indeks yang tidak ada akan menyebabkan error
# print("⬇⬇⬇ mengakses indeks tidak ada, akan error ⬇⬇⬇")
# listku2 = [4,5,6]
# print(listku2[8])

# ==============================================================================================
print("=========================================================================================")
# kesimpulan dan latihan
print("⬇⬇⬇ Kesimpulan dan Latihan ⬇⬇⬇")
# memasukkan data ke list menggunakan "append"
# dan mencetak list dan nama tengah
list_Angka = []
list_String = []
list_Name = ["Galih", "Sukma", "Adjie"]

list_Angka.append(1)
list_Angka.append(2)
list_Angka.append(3)

list_String.append("Halo")
list_String.append("Galih")

midle_Name = list_Name[1]

# mencetak isi variabel listAngka, listString, dan juga menuliskan nama tengah dari listNama
print(list_Angka)
print(list_String)
print("Nama tengahku adalah %s. " % midle_Name)