# Program Absensi Kelas 

from datetime import datetime
from collections import defaultdict
import os
import csv

print("=== PROGRAM ABSENSI KELAS ===")

# Input data kelas dan hari
kelas = input("Masukkan nama kelas: ")
hari = input("Masukkan hari: ")

# Tanggal otomatis
tanggal = datetime.now().strftime("%d-%m-%Y")
print(f"Tanggal absensi: {tanggal}")

# Jumlah siswa
jumlah = int(input("Masukkan jumlah siswa: "))

# List data absensi
absensi = []

print("\n=== INPUT DATA SISWA ===")
for i in range(jumlah):
    print(f"\nSiswa ke-{i+1}")
    NISN_siswa = input("NISN Siswa: ")
    nama = input("Nama Siswa: ")
    ket = input("Keterangan (H=Hadir, A=Alpha, I=Izin, S=Sakit): ").upper()

    if ket not in ["H", "A", "I", "S"]:
        print("Keterangan tidak valid, dianggap Alpha (A).")
        ket = "A"

    absensi.append([NISN_siswa, nama, ket, kelas, hari, tanggal])


# =============== SIMPAN OTOMATIS KE FOLDER ===============

# Nama folder
folder = "Absensi Kelas"

# Buat folder jika belum ada
if not os.path.exists(folder):
    os.makedirs(folder)

# Nama file memakai kelas + tanggal
nama_file = f"Absensi_{kelas}_{tanggal}.csv"

# Lokasi file
path_file = os.path.join(folder, nama_file)

# Simpan file
with open(path_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["NISN", "Nama", "Keterangan", "Kelas", "Hari", "Tanggal"])
    writer.writerows(absensi)

print("\n=== REKAP ABSENSI ===")
print(f"Kelas : {kelas}")
print(f"Hari  : {hari}")
print(f"Tanggal: {tanggal}")
print("---------------------------------------------")
print("NISN     | Nama Siswa           | Ket")
print("---------------------------------------------")

for data in absensi:
    print(f"{data[0]:6} | {data[1]:20} | {data[2]}")

print("\n✔ Data absensi berhasil disimpan!")
print(f"Lokasi: Folder '{folder}' → File '{nama_file}'")

print("=== PROGRAM REKAPAN ABSENSI")
folder = "Absensi Kelas"

# Pastikan folder ada
if not os.path.exists(folder):
    print(f"Folder '{folder}' tidak ditemukan!")
    exit()

# Data rekap
rekap = defaultdict(lambda: {"H": 0, "A": 0, "I": 0, "S": 0})

print("\nMembaca semua file absensi...")
print("--------------------------------\n")

# Baca semua file CSV dalam folder
for file_name in os.listdir(folder):
    if file_name.endswith(".csv"):
        print(f"Memproses: {file_name}")
        path_file = os.path.join(folder, file_name)

        with open(path_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # lewati header

            for row in reader:
                id_siswa, nama, ket, kelas, hari, tanggal = row
                rekap[nama][ket] += 1

# Tampilkan Rekap di Terminal
print("\n=== REKAP KEHADIRAN SISWA ===")
print("Nama Siswa           | H | A | I | S")
print("-------------------------------------")

for nama, data in rekap.items():
    print(f"{nama:20} | {data['H']} | {data['A']} | {data['I']} | {data['S']}")

# Simpan rekap ke file CSV
output_file = "Rekap_Absensi.csv"
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nama", "Hadir", "Alpha", "Izin", "Sakit"])

    for nama, data in rekap.items():
        writer.writerow([nama, data["H"], data["A"], data["I"], data["S"]])

print("\n✔ Rekap berhasil dibuat!")
print(f"Disimpan sebagai: {output_file}")
