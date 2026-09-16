import psycopg2
import pandas as pd

df = pd.read_csv("new_data.csv")

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Intention2025%",
    database="sql_practice")

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO public.sales
    (date, region, beverages_units, food_units, electronics_units, clothes_units, tools_units)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """,(
        row["date"],
        row["region"],
        row["beverages_units"],
        row["food_units"],
        row["electronics_units"],
        row["clothes_units"],
        row["tools_units"],
    ))

conn.commit()
cursor.close()

conn.close()
print("CSV imported")