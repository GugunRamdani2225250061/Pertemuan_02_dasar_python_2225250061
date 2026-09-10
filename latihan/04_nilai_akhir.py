BOBOT_TUGAS = 0.20
BOBOT_UTS = 0.30
BOBOT_UAS = 0.50

print("PROGRAM MENGHITUNG NILAI AKHIR")

nama = input("Masukkan nama: ")

nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = (
nilai_tugas * BOBOT_TUGAS
+ nilai_uts * BOBOT_UTS
+ nilai_uas * BOBOT_UAS
)
print("\n===== HASIL NILAI MAHASISWA =====")
print(f"Nama        : {nama}")
print(f"Nilai Tugas : {nilai_tugas:.2f}")
print(f"Nilai UTS   : {nilai_uts:.2f}")
print(f"Nilai UAS   : {nilai_uas:.2f}")
print(f"Nilai Akhir : {nilai_akhir:.2f}")