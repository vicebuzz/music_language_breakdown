import pandas as pd
from sqlalchemy import create_engine


db_connection_string = "postgresql://postgres:633804735@localhost:5432/Music_languages"


engine = create_engine(db_connection_string)


df = pd.read_csv('result/total.csv')

# Specify the table name
table_name = 'song_languages'

# Insert the DataFrame into the PostgreSQL table
df.to_sql(table_name, con=engine, if_exists='append', index=False)

# Replace 'append' with 'replace' if you want to replace the existing data in the table
