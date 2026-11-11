import logging
import time

from send2trash import send2trash

import config


def hapus_file_lama() -> None:
    batas = time.time() - config.HARI_SIMPAN * 24 * 3600

    for kategori in config.SEMUA_KATEGORI:
        folder = config.FOLDER_PANTAU / kategori
        if not folder.exists():
            continue

        for file in folder.rglob("*"):
            if not file.is_file() or file.stat().st_mtime >= batas:
                continue

            if config.DRY_RUN:
                print(f"[SIMULASI] Akan dihapus: {file.name}")
                continue

            try:
                send2trash(str(file))
                logging.info(f"Dihapus (ke Recycle Bin): {file.name}")
                print(f"Dihapus: {file.name}")
            except Exception as e:
                logging.error(f"Gagal menghapus {file.name}: {e}")