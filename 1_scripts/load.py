import os
import snowflake.connector
import csv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_data_to_snowflake(file_path, table_name, connection_params):
    print("Step 1: Connecting to Snowflake...")
    conn = snowflake.connector.connect(**connection_params)
    cursor = conn.cursor()

    try:
        print("Step 2: Creating or using target table...")
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            Title STRING,
            Source STRING,
            Published_At TIMESTAMP_TZ,
            URL STRING
        )
        """)

        print("Step 3: Inserting data into Snowflake...")
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) == 4:  # Ensure the row has all 4 fields
                    cursor.execute("""
                    INSERT INTO {0} (Title, Source, Published_At, URL)
                    VALUES (%s, %s, %s, %s)
                    """.format(table_name), row)
                else:
                    print(f"Skipping invalid row: {row}")

        print(f"Data from {file_path} has been loaded into table {table_name}.")
    finally:
        print("Closing connection to Snowflake...")
        conn.close()

if __name__ == "__main__":
    connection_params = {
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "warehouse": "COMPUTE_WH",
        "database": "ETL_DATA_WAREHOUSE",
        "schema": "PUBLIC",
        "role": os.getenv("SNOWFLAKE_ROLE"),
    }

    file_path = "../2_data/cleaned_technology_news.csv"
    table_name = "TECHNOLOGY_NEWS"

    print("Starting data load process...")
    load_data_to_snowflake(file_path, table_name, connection_params)
    print("Data load process completed successfully!")