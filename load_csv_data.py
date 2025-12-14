import sqlite3
import pandas as pd
import os

DB_PATH = "Assignment-9/my_app/data/Intelligence_platform.db"
CSV_DIR = "Week 8/DATA"

def load_csv_files():
    """Load all CSV files from Week 8 into the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    files = {
        "cyber_incidents.csv": "cyber_incidents",
        "it_tickets.csv": "it_tickets",
        "datasets_metadata.csv": "datasets_metadata"
    }
    
    for csv_file, table_name in files.items():
        csv_path = os.path.join(CSV_DIR, csv_file)
        if os.path.exists(csv_path):
            print(f"Loading {csv_file}...")
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f"✅ Loaded {len(df)} rows into {table_name}")
        else:
            print(f"❌ File not found: {csv_path}")
    
    conn.close()
    print("\n✅ All CSV files loaded successfully!")

if __name__ == "__main__":
    load_csv_files()
