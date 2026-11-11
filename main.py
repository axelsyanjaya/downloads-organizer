import logging
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import config
from cleaner import hapus_file_lama
from organizer import rapikan_file, rapikan_semua

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)


class PemantauDownloads(FileSystemEventHandler):
    def _proses(self, path_str: str):
        path = Path(path_str)
        # Hanya proses file yang langsung berada di folder pantau
        if path.parent == config.FOLDER_PANTAU:
            rapikan_file(path)

    def on_created(self, event):
        if not event.is_directory:
            self._proses(event.src_path)

    def on_moved(self, event):
        # Browser biasanya mengganti nama .crdownload -> nama asli
        if not event.is_directory:
            self._proses(event.dest_path)


def main():
    print(f"Memantau: {config.FOLDER_PANTAU}")
    print(f"Mode simulasi: {config.DRY_RUN}")
    print("Tekan Ctrl+C untuk berhenti.\n")

    # Rapikan yang sudah ada + bersihkan file lama saat program mulai
    rapikan_semua()
    hapus_file_lama()

    observer = Observer()
    observer.schedule(PemantauDownloads(), str(config.FOLDER_PANTAU), recursive=False)
    observer.start()

    terakhir_bersih = time.time()
    try:
        while True:
            time.sleep(1)
            # Bersihkan file lama tiap 24 jam
            if time.time() - terakhir_bersih > 24 * 3600:
                hapus_file_lama()
                terakhir_bersih = time.time()
    except KeyboardInterrupt:
        observer.stop()
        print("\nBerhenti.")
    observer.join()


if __name__ == "__main__":
    main()