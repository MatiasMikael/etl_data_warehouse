from prefect import flow, task
import subprocess
import time

@task
def fetch_data():
    print("Starting: Fetching data...")
    subprocess.run(["python", "1_scripts/news_fetch.py"], check=True)
    print("Completed: Fetching data.")
    time.sleep(2)

@task
def transform_data():
    print("Starting: Transforming data...")
    subprocess.run(["python", "1_scripts/transform.py"], check=True)
    print("Completed: Transforming data.")
    time.sleep(2)

@task
def load_data():
    print("Starting: Loading data to Snowflake...")
    subprocess.run(["python", "1_scripts/load.py"], check=True)
    print("Completed: Loading data to Snowflake.")
    time.sleep(2)

@flow
def etl_pipeline():
    print("Initiating ETL Pipeline...")
    fetch_data()
    transform_data()
    load_data()
    print("ETL Pipeline completed successfully!")

if __name__ == "__main__":
    etl_pipeline()