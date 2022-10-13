# Operasi Logika not, or, and, xor
## Not
print("=====NOT=====")
a = True
b = not a
print("a :", a)
print("b :", b)

## OR
print("=====OR=====")
a = True
b = True
c = a or b
print(a, "OR", b, " = ", c )

a = True
b = False
c = a or b
print(a, "OR", b, " = ", c )

a = False
b = True
c = a or b
print(a, "OR", b, " = ", c )

a = False
b = False
c = a or b
print(a, "OR", b, " = ", c )

print("=====AND=====")
a = True
b = True
c = a and b
print(a, "AND", b, " = ", c )

a = True
b = False
c = a and b
print(a, "AND", b, " = ", c )

a = False
b = True
c = a and b
print(a, "AND", b, " = ", c )

a = False
b = False
c = a and b
print(a, "AND", b, " = ", c )

## XOR
print("=====XOR=====")
a = True
b = True
c = a ^ b
print(a, "XOR", b, " = ", c )

a = True
b = False
c = a ^ b
print(a, "XOR", b, " = ", c )

a = False
b = True
c = a ^ b
print(a, "XOR", b, " = ", c )

a = False
b = False
c = a ^ b
print(a, "XOR", b, " = ", c )
