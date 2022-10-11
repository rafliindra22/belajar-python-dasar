# Menginput Data User

# data yang di-input pasti string
data = input("Masukan data : ")
print("Data :", data, ", type : ", type(data))

# jika ingin mengambil data int, float maka
angka = float(input("Masukan angka : "))
print("Data :", angka, ", type : ", type(angka))

angka = int(input("Masukan angka : "))
print("Data :", angka, ", type : ", type(angka))

# bagaimana dengan boolean
# dicasting dari integer untuk menginputkan bilangan biner
#sehingga terbaca 1=True, 0=False
biner = bool(int(input("Masukan biner : ")))
print("Data :", biner, ", type : ", type(biner))