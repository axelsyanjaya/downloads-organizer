# 📁 Downloads Organizer

🌐 **English** | [Bahasa Indonesia](README.id.md)

A Python program that monitors your Downloads folder in **real time** and
automatically organizes new files by **file type** and **month**, while
periodically cleaning up old files.

## ❓ Problem

The Downloads folder gets messy fast: hundreds of mixed files (photos, PDFs,
installers, archives) make it hard to find anything. Organizing it by hand is
tedious and easy to forget. This program does it automatically in the background.

## ✨ Key Features

- **Real-time monitoring**: new files are organized as soon as they finish downloading, using the `watchdog` library.
- **Two-level grouping**: files are sorted by type and by month, e.g. `Images/2026-11/photo.jpg`.
- **Incomplete download detection**: temporary files (`.crdownload`, `.part`, `.tmp`) are ignored, and the program waits until the file size is stable before moving it.
- **Overwrite protection**: if a file name already exists, a suffix (`_1`, `_2`, ...) is added so nothing gets overwritten.
- **Dry run mode**: preview planned moves and deletions without changing any file.
- **Safe deletion**: old files are sent to the **Recycle Bin**, not permanently deleted.
- **Scheduled cleanup**: files older than the configured number of days are cleaned up every 24 hours.
- **Respects your own folders**: the cleaner only touches category folders created by the program, never other folders in Downloads.
- **Full logging**: every action (moved, deleted, error) is recorded in `log.txt`.
- **Runs at Windows startup** via Task Scheduler.

## 🗂️ Example Result

Before:
```
Downloads/
├── photo1.jpg
├── report.pdf
├── setup.exe
└── homework.zip
```

After:
```
Downloads/
├── Gambar/2026-11/photo1.jpg
├── Dokumen/2026-11/report.pdf
├── Program/2026-11/setup.exe
└── Arsip/2026-11/homework.zip
```

> Category folder names (`Gambar`, `Dokumen`, `Program`, `Arsip`) are in Indonesian
> by default and can be changed in `config.py`.

## 🛠️ Tech Stack

- Python 3.9+
- `watchdog` (folder monitoring)
- `send2trash` (move to Recycle Bin)
- `pathlib`, `shutil`, `logging` (Python standard library)

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/axelsyanjaya/downloads-organizer.git
cd downloads-organizer

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

## ▶️ Usage

1. Open `config.py` and adjust the settings:
   ```python
   FOLDER_PANTAU = Path.home() / "Downloads"   # folder to monitor
   DRY_RUN = True      # set to False when you are ready
   HARI_SIMPAN = 30    # files older than this (days) are deleted
   ```
2. Run:
   ```bash
   python main.py
   ```
3. Try it first with `DRY_RUN = True` or on a test folder.

### Run automatically at startup (Windows)

Use Task Scheduler with the trigger **When I log on**, and set the action to run
`venv\Scripts\pythonw.exe` with the argument `main.py` and the project folder as
the **Start in** directory.

## ⚙️ Project Structure

```
downloads-organizer/
├── config.py       # settings (folder, categories, retention days)
├── organizer.py    # file moving logic
├── cleaner.py      # old file cleanup logic
├── main.py         # main program (real-time monitor)
└── requirements.txt
```

## 🔄 How It Works

```
New file appears → check extension → wait for download to finish →
determine category + month → move file → write to log
```

## 🔮 Roadmap

- [ ] Configuration via `config.json`
- [ ] Command line arguments (`--folder`, `--dry-run`)
- [ ] Simple GUI
- [ ] Standalone `.exe` distribution

## 👤 Author

[Axel Syanjaya] - [https://github.com/axelsyanjaya]