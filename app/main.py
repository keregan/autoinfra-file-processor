from pathlib import Path

INPUT_DIR = Path("input")

files = list(INPUT_DIR.iterdir())

if not files:
    print("Input folder is empty")
else:
    print("Found files:")

    for file in files:
        if file.is_file():
            print(f"File: {file.name}")

            extension = file.suffix

            print(f"Extension: {extension}")
            print("------")