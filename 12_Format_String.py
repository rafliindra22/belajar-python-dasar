## format string
# string
nama =  "kiplee"
format_str = f"Halooo {nama}"
print(format_str)

# boolean
boolean = False
format_str = f"kebenaran : {boolean}"
print(format_str)

# angka
angka = 20.5
format_str = f"angka anda : {angka}"
print(format_str)

# bilangan bulat
angka = 20
format_str = f"angka bulat : {angka:d}"
print(format_str)

# ribuan (koma dengan ordo ribuan : 3 digit 0 nol)
angka = 20000
format_str = f"angka bulat : {angka:,}"
print(format_str)

# desimal 
angka = 20000.55621
format_str = f"angka bulat : {angka:.2f}" # .2f artinya 2 angka dibelakang koma
print(format_str)

# leading zero
angka = 20000.55621
format_str = f"angka bulat : {angka:09.2f}" # menampilkan 9 total angka diawali 0
print(format_str)

# menampilkan tanda minus - dan plus +
plus = 10
minus = -10
pluskoma = 10.6747
format_plus = f"plus = {plus:+d}"
format_minus = f"minus = {minus:+d}"
format_koma = f"plus koma = {pluskoma:+.2f}"

print(format_plus)
print(format_minus)
print(format_koma)

# format persen
persen = 0.087
format_persen = f"persentase = {persen:.2%}" #persentasi 2 angka di belakang koma
print(format_persen)

# melakukan operasi aritmatika dalam placeholder
harga = 10000
jumlah = 3
total = f"Total Bayar : {harga*jumlah}"
print(total)
total = f"Total Bayar : Rp.  {harga*jumlah:,}"
print(total)

# format angka lain : binary, octal, hexadecimal
angka = 2
for_bin = f"Binary : {bin(angka)}"
for_oct = f"Octal : {oct(angka)}"
for_hex = f"Hex : {hex(angka)}"
print(for_bin)
print(for_oct)
print(for_hex)