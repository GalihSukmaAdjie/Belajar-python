# bilangan bulat
print("⬇⬇⬇ bilangan bulat ⬇⬇⬇")
bilangan_Bulat = 7
print(bilangan_Bulat)

#==============================================================================================
("=========================================================================================")
# bilangan pecahan
print("⬇⬇⬇ bilangan pecahan ⬇⬇⬇")
bilangan_Pecahan = 7.4
print(bilangan_Pecahan)
bilangan_Pecahan_2 = float(5.7)
print(bilangan_Pecahan_2)

#==============================================================================================
("=========================================================================================")
# string
print("⬇⬇⬇ type data string ⬇⬇⬇")
string_1 = "Don't worry"
print(string_1)
string_2 = 'Jangan cemas'
print(string_2)

#==============================================================================================
("=========================================================================================")
# penjumlahan
print("⬇⬇⬇ penjumlahan data ⬇⬇⬇")
satu = 1
dua = 2
jumlah_Angka = satu + dua
print(jumlah_Angka)

kata_1 = "Halo"
kata_2 = "Teman-teman"
kalimat = kata_1 + " " + kata_2
print(kalimat)

# ==============================================================================================
print("=========================================================================================")
# dapat menuliskan lebih dari satu variabel dalam satu line
print("⬇⬇⬇ mencetak 2 data dalam 1 line ⬇⬇⬇")
var_1, var_2 = 1, 2
print(var_1, var_2)

# # ==============================================================================================
# print("=========================================================================================")
# # tidak dapat menjumlahkan antara string dan angka
# print("⬇⬇⬇ tidak dapat menjumlahkan string dan angka ⬇⬇⬇")
# angka1 = 1
# angka2 = 2
# iniString = "ini adalah string"
# print(angka1 + angka2 + iniString)

# ==============================================================================================
print("=========================================================================================")
# kesimpulan dan latihan
print("⬇⬇⬇ Kesimpulan dan Latihan ⬇⬇⬇")
# string harus berisi kata "halo", angka pecahan harus 70.0, bilangan bulat harus 20
dataString = "halo"
dataFloat = 70.0
dataInteger = 20
if dataString == "halo":
    print("String : %s" % dataString)
if isinstance(dataFloat, float) or dataFloat == 10.0:
    print("Float : %f" % dataFloat)
if isinstance(dataInteger, int) or dataInteger == 20:
    print("Integer : %d" % dataInteger)
