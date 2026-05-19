from pathlib import Path
import shutil

from config import (
    INPUT_DIR,
    PROCESSED_DIR,
    BACKUP_DIR
)

from logger import logger

SORTING_RULES = {
    ".pdf": "pdf",
    ".docx": "documents",
    ".xlsx": "spreadsheets",
    ".png": "images",
    ".jpg": "images",
    ".dwg": "drawings"
}

INPUT_DIR.mkdir(exist_ok=True)
PROCESSED_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)

files = list(INPUT_DIR.iterdir())

if not files:
    print("Input folder is empty")
    logger.info("Input folder is empty")

else:
    print("Processing files...\n")

    for file in files:

        try:

            if file.is_file():

                extension = file.suffix.lower()

                folder_name = SORTING_RULES.get(extension, "other")

                target_folder = PROCESSED_DIR / folder_name

                target_folder.mkdir(parents=True, exist_ok=True)

                backup_destination = BACKUP_DIR / file.name

                shutil.copy2(str(file), str(backup_destination))

                logger.info(f"Backup created: {backup_destination}")

                destination = target_folder / file.name

                shutil.move(str(file), str(destination))

                logger.info(f"Moved: {file.name} -> {target_folder}")

                print(f"Processed: {file.name}")

        except Exception as error:

            logger.error(f"Error processing {file.name}: {error}")

            print(f"Error: {file.name}")