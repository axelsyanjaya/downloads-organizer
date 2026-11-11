# 📁 Downloads Organizer

🌐 [English](README.md) | **Bahasa Indonesia**

Program Python yang memantau folder Downloads secara **real-time** dan otomatis
merapikan file baru berdasarkan **jenis file** dan **bulan**, serta membersihkan
file lama secara berkala.

## ❓ Masalah yang Diselesaikan

Folder Downloads cepat berantakan: ratusan file campur aduk (foto, PDF, installer,
zip) sehingga sulit mencari file. Merapikannya manual membosankan dan sering
terlupakan. Program ini melakukannya otomatis di latar belakang.

## ✨ Fitur Unggulan

- **Real-time monitoring**: file baru langsung dirapikan begitu selesai diunduh, memakai library `watchdog`.
- **Pengelompokan ganda**: file dikelompokkan per jenis dan per bulan, contoh `Gambar/2026-11/foto.jpg`.
- **Deteksi unduhan belum selesai**: file sementara (`.crdownload`, `.part`, `.tmp`) diabaikan, dan program menunggu ukuran file stabil sebelum memindahnya.
- **Anti-timpa nama file**: jika nama file sudah ada, otomatis diberi akhiran `_1`, `_2`, dan seterusnya sehingga tidak ada file yang tertimpa.
- **Mode simulasi (Dry Run)**: lihat rencana pemindahan dan penghapusan tanpa mengubah file apa pun.
- **Penghapusan aman**: file lama dikirim ke **Recycle Bin**, bukan dihapus permanen.
- **Pembersihan terjadwal**: file yang lebih tua dari batas hari yang ditentukan dibersihkan otomatis setiap 24 jam.
- **Aman untuk folder pribadi**: pembersih hanya menyentuh folder kategori buatan program, bukan folder lain di Downloads.
- **Logging lengkap**: semua aktivitas (dipindah, dihapus, error) tercatat di `log.txt`.
- **Jalan otomatis saat Windows menyala** lewat Task Scheduler.

## 🗂️ Contoh Hasil

Sebelum:
```
Downloads/
├── foto1.jpg
├── laporan.pdf
├── setup.exe
└── tugas.zip
```

Sesudah:
```
Downloads/
├── Gambar/2026-11/foto1.jpg
├── Dokumen/2026-11/laporan.pdf
├── Program/2026-11/setup.exe
└── Arsip/2026-11/tugas.zip
```

## 🛠️ Teknologi

- Python 3.9+
- `watchdog` (pemantauan folder)
- `send2trash` (hapus ke Recycle Bin)
- `pathlib`, `shutil`, `logging` (bawaan Python)

## 🚀 Cara Instal

```bash
# 1. Clone repository
git clone https://github.com/axelsyanjaya/downloads-organizer.git
cd downloads-organizer

# 2. Buat virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Instal library
pip install -r requirements.txt
```

## ▶️ Cara Pakai

1. Buka `config.py` lalu atur sesuai kebutuhan:
   ```python
   FOLDER_PANTAU = Path.home() / "Downloads"   # folder yang dipantau
   DRY_RUN = True      # ubah ke False jika sudah yakin
   HARI_SIMPAN = 30    # file lebih tua dari ini (hari) dihapus
   ```
2. Jalankan:
   ```bash
   python main.py
   ```
3. Disarankan mencoba dulu dengan `DRY_RUN = True` atau di folder tes.

### Jalan otomatis saat Windows menyala

Gunakan Task Scheduler dengan trigger **When I log on**, lalu atur action untuk
menjalankan `venv\Scripts\pythonw.exe` dengan argumen `main.py` dan folder proyek
pada kolom **Start in**.

## ⚙️ Struktur Proyek

```
downloads-organizer/
├── config.py       # pengaturan (folder, kategori, batas hari)
├── organizer.py    # logika memindahkan file
├── cleaner.py      # logika menghapus file lama
├── main.py         # program utama (pemantau real-time)
└── requirements.txt
```

## 🔄 Alur Kerja

```
File baru muncul → cek ekstensi → tunggu unduhan selesai →
tentukan kategori + bulan → pindahkan → catat ke log
```

## 🔮 Rencana Pengembangan

- [ ] Konfigurasi lewat `config.json`
- [ ] Argumen command line (`--folder`, `--dry-run`)
- [ ] Antarmuka GUI sederhana
- [ ] Distribusi sebagai file `.exe`

## 👤 Pembuat

[Axel Syanjaya] - [https://github.com/axelsyanjaya]