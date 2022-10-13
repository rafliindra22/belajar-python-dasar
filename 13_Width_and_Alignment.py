# Width and Multiline

# Data
data_nama = "Kiplee"
data_umur = "23"
data_tinggi = 163.5

# String
print('\n'+5*'='+"Data"+5*'=')
print(f"Nama : {data_nama}, Umur : {data_umur}, Tinggi : {data_tinggi}")

# String Multiline
print('\n'+5*'='+"Data"+5*'=')
print(f"Nama : {data_nama} \nUmur : {data_umur} \nTinggi : {data_tinggi}")

# Multiline Triplequotes
print('\n'+5*'='+"Data"+5*'=')
print(f'''
Nama    : {data_nama}
Umur    : {data_umur}
Tinggi  : {data_tinggi}
''')

# Mengubah menjadi rata kanan
print('\n'+5*'='+"Data"+5*'=')
print(f'''
Nama    : {data_nama:>6}
Umur    : {data_umur:>6}
Tinggi  : {data_tinggi:>6}
''')

