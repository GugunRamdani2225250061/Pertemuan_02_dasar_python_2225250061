TAHUN_SEKARANG = 2026

print("PROGRAM BIODATA MAHASISWA")

Nama = input("Masukkan Nama: ")
NIM = input("Masukkan NIM: ")
Kelas = input("Masukkan Kelas: ")
Tahun_Lahir = int(input("Masukkan Tahun Lahir: "))
Umur = TAHUN_SEKARANG - Tahun_Lahir

print("\n===== BIODATA MAHASISWA =====")
print(f"Nama  : {Nama}")
print(f"NIM   : {NIM}")
print(f"Kelas : {Kelas}")
print(f"Umur  : sekitar {Umur} Tahun")