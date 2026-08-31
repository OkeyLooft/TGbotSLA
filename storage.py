import json
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent
DB_PATH: Path = BASE_DIR / "database.json"

class TicketStorage:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path

    def read_json(self) -> dict:
        with open(self.db_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def write_json(self, data):
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
