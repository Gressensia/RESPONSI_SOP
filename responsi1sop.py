import helper

#5200411122
#Gressensia Olivia Neno Aumenu
helper.header("Responsi NO.1")

Ram = int(input("Kapasitas RAM : " ))
totalBlok = int(input("Blok/unit : "))
petabit = helper.hitungPetaBit(helper.ubahRamKeMbps(Ram), totalBlok)
kapasitas = petabit - Ram

print("Total peta bit : ", petabit , "KB " )
print("Kapasitas per Petabit : " , kapasitas)
print("\nProgram tereksekusi")

print("-"*40)
ramUntukSOP = int(input("Kapasitas Sistem Operasi  : "))
program1 = int(input("RAM yang digunakan Program 1 : "))
program2 = int(input("RAM yang digunakan Program 2 : "))

totalRam = program1 + program2
totalRAMygtidakterpakai = Ram - totalRam

print("Total RAM yang Terpakai = ", totalRam)
print("Total RAM yang tidak Terpakai = ", totalRAMygtidakterpakai)

print("\njumlah blok bernilai 1 = ", totalRam)
print("jumlah blok bernilai 0 = ", totalBlok - totalRam)

