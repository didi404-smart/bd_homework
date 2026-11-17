import psycopg2
import csv

def fill_table_from_csv(tablename: str, filepath: str):
    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="di291009"
    )
    cur = conn.cursor()

    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            query = f"INSERT INTO {tablename} VALUES ({', '.join(['%s'] * len(row))})"
            cur.execute(query, row)
    conn.commit()
    cur.close()
    conn.close()


def main():
    fill_table_from_csv("employees", "data/employees_data.csv")
    fill_table_from_csv("customers", "data/customers_data.csv")
    fill_table_from_csv("orders", "data/orders_data.csv")

if __name__ == "__main__":
    main()