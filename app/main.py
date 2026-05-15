from pathlib import Path
import shutil

INPUT_DIR = Path("input")
PROCESSED_DIR = Path("processed")

SORTING_RULES = {
    ".pdf": "pdf",
    ".docx": "documents",
    ".xlsx": "spreadsheets",
    ".png": "images",
    ".jpg": "images",
    ".dwg": "drawings"
}

files = list(INPUT_DIR.iterdir())

if not files:
    print("Input folder is empty")

else:
    print("Processing files...\n")

    for file in files:

        if file.is_file():

            extension = file.suffix.lower()

            folder_name = SORTING_RULES.get(extension, "other")

            target_folder = PROCESSED_DIR / folder_name

            target_folder.mkdir(parents=True, exist_ok=True)

            destination = target_folder / file.name

            shutil.move(str(file), str(destination))

            print(f"Moved: {file.name} -> {target_folder}")