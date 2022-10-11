# Operasi komparasi
# > , < ,  >= , <= ,  == ,  != , is , is not
# Hasil dari komparasi adalah boolean
a = 4
b = 8
# lebih besar
c = a > b
print("Lebih dari :")
print(a,">",b,"=", c) # typedata tidak dicasting
print(str(a) + " > " + str(b) + " = " + str(c)) # dicasting ke string

#lebih kecil
print("Kurang dari :")
c = a < b
print(str(a) + " < " + str(b) + " = " + str(c)) # dicasting ke string, tidak pun bisa

# lebih dari sama dengan
print("Lebih dari sama dengan :")
a = 8
b = 8
c = a >= b
print(str(a) + " >= " + str(b) + " = " + str(c)) # dicasting ke string, tidak pun bisa

# kurang dari sama dengan
print("kurang dari sama dengan :")
a = 4
b = 8
c = a <= b
print(str(a) + " <= " + str(b) + " = " + str(c)) # dicasting ke string, tidak pun bisa

# sama dengan
print("sama dengan :")
a = 4
b = 8
c = a == b
print(str(a) + " == " + str(b) + " = " + str(c)) # dicasting ke string, tidak pun bisa

# tidak sama dengan
print("tidak sama dengan :")
a = 4
b = 8
c = a != b
print(str(a) + " != " + str(b) + " = " + str(c)) # dicasting ke string, tidak pun bisa

# is adalah object identity
print("========Object Identity========")
x = 5
y = 5
print("nilai x = ",x,", id = ",hex(id(x)))
print("nilai x = ",y,", id = ",hex(id(y)))
z = x is y
print("x is y = ",z)

x = 5
y = 6
print("nilai x = ",x,", id = ",hex(id(x)))
print("nilai x = ",y,", id = ",hex(id(y)))
z = x is y
print("x is y = ",z)

# is not adalah object identity kebalikan dari is
x = 5
y = 5
print("nilai x = ",x,", id = ",hex(id(x)))
print("nilai x = ",y,", id = ",hex(id(y)))
z = x is not y
print("x is y = ",z)

x = 5
y = 6
print("nilai x = ",x,", id = ",hex(id(x)))
print("nilai x = ",y,", id = ",hex(id(y)))
z = x is not y
print("x is y = ",z)