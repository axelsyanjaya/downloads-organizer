from pathlib import Path

# Folder yang dipantau. Untuk uji coba, ganti dulu ke folder tes (lihat Tahap 8)
FOLDER_PANTAU = Path.home() / "Downloads"

# True = hanya mencetak rencana, tidak memindah/menghapus apa pun
DRY_RUN = False

# File di folder kategori yang lebih tua dari ini akan dihapus
HARI_SIMPAN = 30

KATEGORI = {
    "Gambar":  [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"],
    "Dokumen": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
    "Video":   [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio":   [".mp3", ".wav", ".m4a", ".flac"],
    "Arsip":   [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Program": [".exe", ".msi", ".apk"],
    "Kode":    [".py", ".js", ".html", ".css", ".json", ".ipynb"],
}

# Nama folder kategori (dipakai juga oleh pembersih)
SEMUA_KATEGORI = list(KATEGORI.keys()) + ["Lainnya"]

# File yang belum selesai diunduh, jangan disentuh
EKSTENSI_ABAIKAN = {".crdownload", ".part", ".tmp", ".download", ".opdownload"}