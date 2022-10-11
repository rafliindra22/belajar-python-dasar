## Operasi Aritmatika
a = 3
b = 2

# Pertambahan
hasil = a + b
print(a,'+',b,'=',hasil)

# Pengurangan
hasil = a - b
print(a,'-',b,'=',hasil)

# Perkalian
hasil = a * b
print(a,'*',b,'=',hasil)

# Pembagian
hasil = a / b
print(a,'/',b,'=',hasil)

# Eksponen (Pangkat)
hasil = a ** b
print(a,'**',b,'=',hasil)

# Modulus (Sisa hasil bagi)
hasil = a % b
print(a,'%',b,'=',hasil)

# Floor Division (Hasil Pembagian dibulatkan)
hasil = a // b
print(a,'//',b,'=',hasil)

## Prioritas Operasi (Ops Presedence)
'''
    1. Operasi dalam kurung -> (a+b)
    2. Eksponen/pangkat -> **
    3. Perkalian, Pembagian, Modulus, floor division -> *, /, %, //
    4. Penjumlahan dan pengurangan -> +, -
'''
x = 3
y = 2
z = 1
hasil = x + y ** x / z % x - y * (x - y)
print(x,'+',y,'**',x,'/',z,'%',x,'-',y,'(',x,'-',y,')=',hasil)