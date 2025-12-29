import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "mobile_usage.db"

def run_sql(sql: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description] if cur.description else []
    conn.close()
    return cols, rows
