import logging
import shutil
import time
from datetime import datetime
from pathlib import Path

import config


def cari_kategori(ekstensi: str) -> str:
    ekstensi = ekstensi.lower()
    for nama, daftar in config.KATEGORI.items():
        if ekstensi in daftar:
            return nama
    return "Lainnya"


def nama_unik(path: Path) -> Path:
    """Kalau nama sudah ada, tambahkan _1, _2, dst. agar tidak menimpa."""
    if not path.exists():
        return path
    counter = 1
    while True:
        baru = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if not baru.exists():
            return baru
        counter += 1


def tunggu_file_siap(path: Path, timeout: int = 60) -> bool:
    """Tunggu sampai ukuran file stabil (artinya unduhan sudah selesai)."""
    ukuran_lama = -1
    mulai = time.time()
    while time.time() - mulai < timeout:
        try:
            ukuran = path.stat().st_size
        except FileNotFoundError:
            return False
        if ukuran == ukuran_lama:
            return True
        ukuran_lama = ukuran
        time.sleep(1)
    return False


def rapikan_file(path: Path) -> None:
    if not path.is_file():
        return
    if path.suffix.lower() in config.EKSTENSI_ABAIKAN:
        return
    if not tunggu_file_siap(path):
        logging.warning(f"Dilewati (belum siap): {path.name}")
        return

    kategori = cari_kategori(path.suffix)
    bulan = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m")
    folder_tujuan = config.FOLDER_PANTAU / kategori / bulan
    tujuan = nama_unik(folder_tujuan / path.name)

    if config.DRY_RUN:
        print(f"[SIMULASI] {path.name} -> {kategori}/{bulan}/")
        return

    try:
        folder_tujuan.mkdir(parents=True, exist_ok=True)
        shutil.move(str(path), str(tujuan))
        logging.info(f"Dipindah: {path.name} -> {kategori}/{bulan}/")
        print(f"Dipindah: {path.name} -> {kategori}/{bulan}/")
    except PermissionError:
        logging.error(f"File sedang dipakai: {path.name}")
    except Exception as e:
        logging.error(f"Gagal memindah {path.name}: {e}")


def rapikan_semua() -> None:
    """Rapikan file yang sudah ada di folder (hanya level atas, subfolder diabaikan)."""
    for item in config.FOLDER_PANTAU.iterdir():
        rapikan_file(item)