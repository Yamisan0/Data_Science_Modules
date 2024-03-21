from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

csv_dir = '../subject/customer'
csv_files = os.listdir(csv_dir)
DB = os.getenv('DATABASE_DB')
USERNAME = os.getenv('DATABASE_USER')
PASSWORD = os.getenv('DATABASE_PASSWORD')
PORT = os.getenv('DATABASE_PORT')
db_url = f'postgresql://{USERNAME}:{PASSWORD}@localhost:{PORT}/{DB}'
engine = create_engine(db_url)

def create_tables():
    try:
        for f in csv_files:
            if f.endswith('.csv'):
                table_name = os.path.splitext(f)[0]
                csv_path = os.path.join(csv_dir, f)
                df = pd.read_csv(csv_path)
                df.columns = [c.lower().replace(' ', '_') for c in df.columns]
                df.to_sql(table_name, engine, if_exists='replace', index=False)
    except error:
        print(f"An error has occured:{error}")

def main():
    create_tables()

if __name__ == "__main__":
    main()


        


    


