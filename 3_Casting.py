# Casting adalah Mengubah Tipe Data
# tipe data = int, float, str, bool
print("======INTEGER======")
data_int = 1
print("data :", data_int, "type :", type(data_int))

data_float  = float(data_int)
data_string = str(data_int)
data_bool   = bool(data_int) # akan false jika nilai = 0
print("data :", data_float, "type :", type(data_float))
print("data :", data_string, "type :", type(data_string))
print("data :", data_bool, "type :", type(data_bool)) # akan false jika nilai = 0

print("======FLOAT======")
data_float = 5.6
print("data :", data_float, "type :", type(data_float))

data_int  = int(data_float) # dibulatkan ke bawah
data_string = str(data_float) # nilai sama tapi jadi teks
data_bool   = bool(data_float) # akan false jika nilai = 0
print("data :", data_int, "type :", type(data_int)) # dibulatkan ke bawah
print("data :", data_string, "type :", type(data_string)) # nilai sama tapi jadi teks
print("data :", data_bool, "type :", type(data_bool)) # akan false jika nilai = 0

print("======BOOLEAN======")
data_bool = False
print("data :", data_bool, "type :", type(data_bool))

data_int  = int(data_bool) # True jadi 1, False jadi 0
data_string = str(data_bool) # nilai sama tapi jadi teks
data_float  = float(data_bool) 
print("data :", data_int, "type :", type(data_int))
print("data :", data_string, "type :", type(data_string)) # nilai sama tapi jadi teks
print("data :", data_float, "type :", type(data_float)) 

print("======STRING======")
data_string = "51"
print("data :", data_string, "type :", type(data_string))

data_int  = int(data_string) # string harus angka
data_float  = float(data_string) # string harus angka
data_bool = bool(data_string) # akan false jika string kosong, bukan 0
print("data :", data_int, "type :", type(data_int)) # string harus angka
print("data :", data_float, "type :", type(data_float)) # string harus angka
print("data :", data_bool, "type :", type(data_bool)) # akan false jika string kosong, bukan 0