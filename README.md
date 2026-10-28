# Pertemuan 12 — File I/O dan Error Handling

## Identitas Mahasiswa

- **Nama:** Mutiara Sari
- **NIM:** 2225250071
- **Kelas:** 3A
- **Program Studi:** Pendidikan Matematika
- **Mata Kuliah:** Algoritma dan Pemrograman

## Tujuan

Praktikum ini bertujuan untuk memahami operasi file menggunakan Python, meliputi menulis, membaca, dan menambahkan isi file. Selain itu, praktikum ini mempelajari pemrosesan data per baris serta penanganan kesalahan menggunakan `FileNotFoundError` dan `ValueError`.

Pada bagian tugas, program digunakan untuk membaca data nilai mahasiswa, memvalidasi masukan, menghitung statistik nilai, dan menyimpan hasil rekap ke dalam file teks.

## Struktur Proyek

```text
pertemuan-12-file-io-2225250071/
├── data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
├── tugas/
│   └── rekap_nilai_file.py
├── .gitignore
└── README.md
```

File pengujian tambahan dapat dibuat di dalam folder `data/` selama proses pengujian program.

## Deskripsi Latihan

1. `01_tulis_file.py`: menulis teks ke dalam file menggunakan mode `w`.
2. `02_baca_file.py`: membaca isi file menggunakan mode `r`.
3. `03_append_file.py`: menambahkan teks ke dalam file menggunakan mode `a`.
4. `04_proses_baris.py`: membaca dan memproses data nilai per baris.
5. `05_file_not_found.py`: menangani kondisi ketika file tidak ditemukan.
6. `06_value_error.py`: menangani masukan yang tidak dapat dikonversi menjadi angka.

## Deskripsi Tugas

Program `rekap_nilai_file.py` membaca data nilai mahasiswa dari `data/nilai.txt` dan menyimpan hasil rekap ke `data/hasil_rekap.txt`.

Program memiliki dua fungsi utama:

- `baca_data(nama_file)`: membaca data, melewati baris kosong, memvalidasi nilai, dan menangani kesalahan ketika file tidak ditemukan atau format data tidak valid.
- `tulis_rekap(nama_file, data)`: menghitung jumlah data valid, rata-rata, nilai minimum, nilai maksimum, dan jumlah mahasiswa yang lulus.

Mahasiswa dinyatakan lulus apabila memperoleh nilai lebih besar atau sama dengan 60.

## Format Data Masukan

Data masukan disimpan dalam file teks dengan format:

```text
NIM,nilai
```

Contoh isi `data/nilai.txt`:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Setiap baris berisi identitas mahasiswa dan nilai yang dipisahkan oleh tanda koma. Nilai harus dapat dikonversi menjadi angka. Baris kosong dilewati, sedangkan baris dengan format atau nilai yang tidak valid dilaporkan oleh program.

## Cara Menjalankan Program

Jalankan perintah berikut melalui terminal pada direktori utama proyek:

```powershell
python tugas/rekap_nilai_file.py
```

Jika perintah `python` belum tersedia pada terminal, gunakan lokasi Python yang sudah terpasang pada komputer:

```powershell
& "$HOME\.local\bin\python3.14.exe" tugas/rekap_nilai_file.py
```

Hasil rekap akan disimpan secara otomatis ke dalam `data/hasil_rekap.txt`.

## Penanganan Kesalahan

Program menangani beberapa kondisi berikut:

1. **File tidak ditemukan:** program menampilkan pesan kesalahan dan mengembalikan daftar kosong.
2. **Nilai tidak valid:** program melaporkan baris yang bermasalah dan melanjutkan pembacaan data.
3. **Baris kosong:** program melewati baris kosong tanpa menghentikan proses.
4. **Tidak ada data valid:** program tidak melakukan perhitungan rekap.
5. **Nilai batas kelulusan:** program menggunakan kondisi `nilai >= 60` untuk menentukan kelulusan.

## Test Case

Pengujian dilakukan untuk memeriksa pemrosesan data normal dan penanganan berbagai kondisi kesalahan.

| No. | Kondisi pengujian | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|---|
| 1 | Data nilai normal dengan satu nilai tidak valid | Data valid diproses dan nilai tidak valid dilewati | 5 data valid diproses; rata-rata 83,40; nilai minimum 74; nilai maksimum 92; 5 mahasiswa lulus | Berhasil |
| 2 | File masukan tidak ditemukan | Program menampilkan pesan kesalahan dan mengembalikan daftar kosong | Pesan `File tidak ditemukan.` ditampilkan dan hasil pembacaan berupa `[]` | Berhasil |
| 3 | File berisi baris kosong dan nilai tidak valid | Baris kosong dilewati, nilai tidak valid dilaporkan, dan data valid tetap dibaca | Baris ke-4 dilaporkan tidak valid; tiga data valid berhasil dibaca | Berhasil |
| 4 | File masukan kosong | Program tidak melakukan perhitungan rekap | Program menghasilkan `Data: []` dan menampilkan `Tidak ada data valid untuk direkap.` | Berhasil |
| 5 | Nilai berada pada batas kelulusan | Nilai 60 dinyatakan lulus dan nilai di bawah 60 dinyatakan tidak lulus | Dari nilai 60, 59, dan 75, terdapat 2 mahasiswa lulus | Berhasil |

## Refleksi

Melalui praktikum ini, saya mempelajari penggunaan operasi file dalam Python serta pentingnya validasi data sebelum melakukan perhitungan. Saya juga memahami bahwa penanganan kesalahan dapat membantu program tetap berjalan ketika menemukan data yang tidak valid atau file yang tidak tersedia.

Pengujian dengan beberapa kondisi masukan membantu memastikan bahwa program menghasilkan keluaran yang sesuai dengan kebutuhan. Selain itu, praktikum ini melatih saya untuk mendokumentasikan hasil pengujian secara sistematis.