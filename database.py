import pandas as pd
from sqlalchemy import create_engine


db_connection_string = "postgresql://postgres:633804735@localhost:5432/Music_languages"


engine = create_engine(db_connection_string)

def drop_model_outcomes_to_db():
    df = pd.read_csv('result/total.csv')

    # Specify the table name
    table_name = 'song_languages'

    # Insert the DataFrame into the PostgreSQL table
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

def provide_full_language_names():
    pass
