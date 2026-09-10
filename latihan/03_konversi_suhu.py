KELVIN_OFFSET = 273.15

print("PROGRAM KONVERSI SUHU")

Celsius = float(input("Masukkan suhu dalam Celsius: "))

Fahrenheit = (9 / 5) * Celsius + 32
Kelvin = Celsius + KELVIN_OFFSET

print("\n===== HASIL KONVERSI SUHU =====")
print(f"Celsius    : {Celsius:.2f} °C")
print(f"Fahrenheit : {Fahrenheit:.2f} °F")
print(f"Kelvin     : {Kelvin:.2f} K")