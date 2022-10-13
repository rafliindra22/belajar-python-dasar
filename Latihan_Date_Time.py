# import library datetime untuk menanampilkan tanggal dan waktu
import datetime as dt
print("Silahkan masukan tengga, bulan, tahun lahir anda!!!")
tanggal = int(input("Tanggal\t: "))
bulan = int(input("Bulan\t: "))
tahun = int(input("Tahun\t: "))
tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda\t: {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini Tanggal\t: {hari_ini}")

umur_hari = hari_ini - tanggal_lahir
print(f"umur hari anda : {umur_hari.days}")
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
#umur_hari_sisa = (umur_hari.days / 365) // 30 
print(f"Umur anda\t: {umur_tahun} Tahun, {umur_bulan_sisa} Bulan")
#print(f"Umur anda\t: {umur_tahun} Tahun, {umur_bulan_sisa} Bulan, {umur_hari_sisa:.0f} Hari")