## variabel pada bahasa python tidak harus didefinisikan

# Tipe Data integer
data_integer = 1
print("Contoh :", data_integer)
print("Tipe Data : ", type(data_integer))

# Tipe Data Float
data_float = 7.5
print("Contoh :", data_float)
print("Tipe Data : ", type(data_float))

# Tipe Data String
data_string = "kiplee 599"
print("Contoh :", data_string)
print("Tipe Data : ", type(data_string))

# Tipe Data Boolean (Biner True or False)
data_bool = True
print("Contoh :", data_bool)
print("Tipe Data : ", type(data_bool))

## Tipe Data Khusus
# Bilangan Kompleks
data_complex = complex(5,6)
print("Contoh :", data_complex)
print("Tipe Data : ", type(data_complex))

# Tipe Data bahasa C
# dengan mengimport tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.9)
print("Contoh :", data_c_double)
print("Tipe Data : ", type(data_c_double))