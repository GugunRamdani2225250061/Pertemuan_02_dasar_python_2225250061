print("KALKULATOR PERSEGI PANJANG")

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print("\n===== HASIL PERHITUNGAN =====")
print(f"Panjang  : {panjang:.2f}")
print(f"Lebar    : {lebar:.2f}")
print(f"Luas     : {luas:.2f} satuan persegi")
print(f"Keliling : {keliling:.2f} satuan")