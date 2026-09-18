import psycopg2
import pandas as pd

df = pd.read_csv("warehouse.csv")

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Intention2025%",
    database="sql_practice")

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO public.warehouse
    (warehouse_id, region, capacity, warehouse_status)
    VALUES (%s, %s, %s, %s)
    """,(
        row['warehouse_id'],
        row["region"],
        row["capacity"],
        row["warehouse_status"]
    ))

conn.commit()
cursor.close()

conn.close()
print("CSV imported")