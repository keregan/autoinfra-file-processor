from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

INPUT_DIR = Path(os.getenv("INPUT_DIR", "input"))
PROCESSED_DIR = Path(os.getenv("PROCESSED_DIR", "processed"))
BACKUP_DIR = Path(os.getenv("BACKUP_DIR", "backup"))
LOG_DIR = Path(os.getenv("LOG_DIR", "logs"))