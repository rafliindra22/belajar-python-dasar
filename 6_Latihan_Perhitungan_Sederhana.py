## PR Latihan Perhitungan Sederhana
'''
    1. Konversi Fahrenheit ke Kelvin
    2. Konversi Kelvin ke Fahrenheit
'''
# Fahrenheit to Kelvin
menu = input("Masukan Menu yang akan dipilih (fk / kf): ")
if menu == 'fk':
    nilai = float(input("Masukan Nilai Suhu Fahrenheit : "))
    print("Nilai Suhu Fahrenheit = ", nilai, "F")
    f_c = (5/9) * (nilai - 32)
    print("Nilai Suhu dalam Celcius = ", f_c, "C")
    kelvin = f_c + 273
    print("Hasil Konversi Fahrenheit ke Kelvin = ",kelvin, "K")
# Kelvin to Fahrenheit
elif menu == "kf":
    nilai = float(input("Masukan Nilai Suhu Kelvin : "))
    print("Nilai Suhu Kelvin = ", nilai, "K")
    k_c = nilai - 273
    print("Nilai Suhu dalam Celcius = ", k_c, "C")
    fahrenheit = (9/5) * k_c + 32
    print("Hasil Konversi Kelvin ke Kelvin = ",fahrenheit, "F")
else:
    print("\nRequest Can't Run\n")

print("TQ")