# Operasi dan Manipulasi String

# 1. Menyambung String (concatenate)
nama_awal = 'Rafli'
nama_tengah = 'Indra'
nama_akhir = 'Gunawan'
nama_lengkap = nama_awal +" "+ nama_tengah +" "+ nama_akhir
print(nama_lengkap, type(nama_lengkap))
'''
nama_lengkap = nama_awal , nama_tengah , nama_akhir #jika pakai koma hasil dari
print(nama_lengkap, type(nama_lengkap)) # pemanggilan akan jadi type: tuple
'''

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print('Panjang dari '+ nama_lengkap + ': '+ str(panjang))

# 3. Operatur untuk String
#mengecek apakah ada komponen char atau string di String
d = "dr"
status = d in nama_lengkap
print("'dr' dalam "+ nama_lengkap + ": "+ str(status))

d = "drs"
status = d in nama_lengkap
print("'drs' dalam "+ nama_lengkap + ": "+ str(status))

d = "drs"
status = d not in nama_lengkap
print("'drs' tidak dalam "+ nama_lengkap + ": "+ str(status))

#mengulang string
print("wk"*5)
print(5*"wok")

#indexing
print("index ke-0 :" + nama_lengkap[0])
print("index ke-1 :" + nama_lengkap[1])
print("index ke-(-1) :" + nama_lengkap[-1]) #-1 berarti paling belakang
print("index ke-[0-3] :" + nama_lengkap[0:4]) #[0:4] berarti yang diambil 0-3, 4 tdk diambil
print("index ke-[0,2,4,6,8,10] :" + nama_lengkap[0:11:2]) 

# item paling keciil dalam string
print("paling kecil : " + min(nama_lengkap))

# item paling keciil dalam string
print("paling kecil : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code dari spasi adalah " + str(ascii_code))
data = 117
print("char dari ASCII Code 117 adalah " + chr(data))

# Operator dalam bentuk method
## count
data = "reza sulanjana purnama"
jumlah = data.count("a")
print("jumlah a pada "+ data + ": " + str(jumlah))

## Merubah case dari string
### uppercase
data = "rafli"
print("normal : "+ data)
data = data.upper()
print("Uppercase : " + data)

### lowercase
data = "RAFLI"
print("normal : "+ data)
data = data.lower()
print("Lower : " + data)

### Capital each fisrt letter
data = "rafli indra gunawan"
print("normal : "+ data)
data = data.title()
print("Capital each first letter : " + data)

## Mengecek case dari string
### cek lower
data = "rafliindragunawan"
data_lower = data.islower() #hasilnya bool
print("Hasil cek lower : " + str(data_lower)) #casting ke str
### cek upper
data_upper = data.isupper()
print("Hasil cek upper : " + str(data_upper))
### cek capital each first letter
data_tittle = data.istitle()
print("Hasil cek tittle : " + str(data_tittle))
### cek apakah semua huruf
data_alpha = data.isalpha() #spasi tidak termasuk
print("Hasil cek alpha : " + str(data_alpha))
### cek apakah huruf dan angka
data_alnum = data.isalnum()
print("Hasil cek alnum : " + str(data_alnum))
### cek apakah  angka saja
data_decimal = data.isdecimal()
print("Hasil cek angka : " + str(data_decimal))
### cek apakah  angka saja
data_space = data.isspace()
print("Hasil cek spasi : " + str(data_space))

## mengecek komponen
### startwith() dan endwith()\
cek_start = "Rafli Indra Gunawan".startswith("Rafli")
print("start = " + str(cek_start))
cek_end = "Rafli Indra Gunawan".endswith("Indra")
print("start = " + str(cek_end))

## Penggabungan komponen join() split()
data = ['rafli','kipli','kiplee']
join = ' & '.join(data)
print(data)
print(join)

join = 'rafli&kipli&kiplee'
print(join.split('&'))

## alokasi karakter = rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'" + kanan + "'")
kiri = "kiri".ljust(10)
print("'" + kiri + "'")
tengah = "tengah".center(10,"~")
print("'" + tengah + "'")

# kebalikannya -> strip
tengah = tengah.strip(("~")) #menghilangkan tanda ~
print("'"+tengah+"'")