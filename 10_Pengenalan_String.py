# Pengenalan String

# Menggunakan single quote
data = 'Ini String Singgle Quote'
print(data)

# Menggungakan double quote
data = "Ini String Double Quote"
print(data)

# Penggunaan Quote dalam String
data = '"Hidup itu Indah" -Riyadi'
print(data)
data = "Riyadi pernah berkata pada hari jum'at"
print(data)

# Menggunakan tanda \
## membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, is\'t it?')

## backslash
print("C:\\user\\Ucup")

## tab
print("Ucup\tOtong")

##backspace
print("Ucup \bOtong")

## newline
print("Bari 1\nBaris 2\n") #LF -> line feed
print("Bari 1\rBaris 2\n") #CR -> carriage return
print("Bari 1\r\nBaris 2\n") #CRLF -> line feed carriage return

## String literal atau raw
#hati-hati
print('C:\new folder') #akan salah pathnya jadi garis baru

# menggunakan raw string
print(r'C:\new folder') #semua slash akan terbaca

# multiline literal string
print('''
Nama    : Ucup
Kelas   : 3 SD
''')

# multiline literal string dan raw
print(r'''
Nama    : Ucup
Kelas   : 3\SD
''')