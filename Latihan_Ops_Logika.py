# Latihan Operasi Komparasi Logika
'''
    1. -------0+++++++5-------8+++++++11-------
    2. +++++++0-------5+++++++8-------11+++++++
'''
print("1. -------0+++++++5-------8+++++++11-------")
inputUser = float(input("Masukan angka > 0 dan < 5\natau\nangka > 8 dan < 11\n: "))
# -------0+++++++5-------
isnollima = inputUser > 0 and inputUser < 5
print("angka > 0 & < 5 : ", isnollima)
# -------8+++++++11-------
isdelas = inputUser > 8 and inputUser < 11
print("angka > 8 & < 11 : ", isdelas)
hasil = isnollima or isdelas
print("Maka Hasilnya : ",hasil)

print("2. +++++++0-------5+++++++8-------11+++++++")
inputUser = float(input("Masukan angka < 0 atau > 5 dan < 8 atau > 11\n: "))
# +++++++0-------
iskurang = inputUser < 0 
print("angka < 0 = ", iskurang)
# -------5+++++++8-------
isdan = inputUser > 5 and inputUser < 8
print("angka > 5 dan < 8 = ", isdan) 
# -------11+++++++
islebih = inputUser > 11
print("angka > 11 = ", islebih) 
hasil = iskurang or isdan or islebih
print("Maka Hasilnya : ",hasil)