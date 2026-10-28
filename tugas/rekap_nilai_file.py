def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8-sig") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data.append((nim, nilai))
                except ValueError:
                    print(f"Baris {nomor_baris} tidak valid: {baris}")

    except FileNotFoundError:
        print("File tidak ditemukan.")

    return data

def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    jumlah_data = len(data)
    total_nilai = sum(nilai for nim, nilai in data)
    rata_rata = total_nilai / jumlah_data
    nilai_minimum = min(nilai for nim, nilai in data)
    nilai_maksimum = max(nilai for nim, nilai in data)
    jumlah_lulus = sum(1 for nim, nilai in data if nilai >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("REKAP NILAI MAHASISWA\n")
        file.write("====================\n")
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {nilai_minimum:g}\n")
        file.write(f"Nilai maksimum: {nilai_maksimum:g}\n")
        file.write(f"Jumlah mahasiswa lulus: {jumlah_lulus}\n")

    print(f"Rekap berhasil disimpan ke {nama_file}.")

if __name__ == "__main__":
    data_nilai = baca_data("data/nilai.txt")
    tulis_rekap("data/hasil_rekap.txt", data_nilai)