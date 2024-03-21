import pandas as pd
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float, BigInteger
import config

def create_table():
    try:
        engine = create_engine(config.db_url)
        df = pd.read_csv('../subject/item/item.csv')
        data_types= {
            "product_id": Integer(),
            "category_id": BigInteger(),
            "category_code": String(length=255),
            "brand": String(length=255)
        }
        with engine.connect() as connection:
            df.to_sql('items', connection, if_exists='replace', index=False, dtype=data_types)
    except Exception as error:
        print(f'An error has occured :\n{error}')
    


def main():
    create_table()



if __name__ == '__main__':
    main()