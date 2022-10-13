# Operator Bitwise, operasi biner, binary
a = 7
b = 2
# Bitwise OR (|)
c = a | b
print("\n====OR====")
print("nilai: ",a," , binary :",format(a,'08b'))
print("nilai: ",b," , binary :",format(b,'08b'))
print("------------------------------------------ |")
print("nilai: ",c," , binary :",format(c,'08b'))

# Bitwise AND (&)
c = a & b
print("\n====AND====")
print("nilai: ",a," , binary :",format(a,'08b'))
print("nilai: ",b," , binary :",format(b,'08b'))
print("------------------------------------------ &")
print("nilai: ",c," , binary :",format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b
print("\n====XOR====")
print("nilai: ",a," , binary :",format(a,'08b'))
print("nilai: ",b," , binary :",format(b,'08b'))
print("------------------------------------------ ^")
print("nilai: ",c," , binary :",format(c,'08b'))

# Bitwise OR (|)
c = ~a
print("\n====OR====")
print("nilai: ",a," , binary :",format(a,'08b'))
print("------------------------------------------ ~")
print("nilai: ",c," , binary :",format(c,'08b'))
