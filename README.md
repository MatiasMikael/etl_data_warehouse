# ETL Pipeline: Technology News Analysis

This project is an ETL (Extract, Transform, Load) pipeline for fetching, processing, and storing recent technology news articles. It demonstrates the integration of Python scripting, data cleaning, and Prefect for orchestration.

## Project Overview

Goal: Automate the extraction of technology news from an API, clean and filter the data, and load it into Snowflake for analysis.

Tools Used:
* NewsAPI: For fetching the latest technology news.
* Python: Data processing and script automation.
* Pandas: Data cleaning and filtering.
* Snowflake: Data storage and querying.
* Prefect: Pipeline orchestration.

* Folder Structure

| Folder/File         | Description                                      |
|---------------------|--------------------------------------------------|
| 1_scripts/        | Contains all ETL scripts                        |
| ├── news_fetch.py | Fetches news data from NewsAPI                  |
| ├── transform.py  | Cleans and filters the fetched data             |
| ├── load.py       | Loads cleaned data into Snowflake               |
| ├── prefect_pipeline.py | Orchestrates the ETL process              |
| 2_data/           | Stores raw and cleaned data                     |
| ├── technology_news.csv | Raw fetched data                          |
| ├── cleaned_technology_news.csv | Cleaned and filtered data         |
| 3_sql_queries/    | Contains SQL outputs                            |
| 4_other/          | Miscellaneous files like dependencies and configs |
| ├── requirements.txt | Python dependencies                         |
| ├── .gitignore    | Excluded files and folders                      |


## Steps in the Pipeline

* Extract:
Fetch news articles containing the keyword technology using NewsAPI.
Save the data in CSV format (_technology_news.csv_).
* Transform:
Clean the data by removing duplicates and rows with missing values.
Filter articles published in the last 7 days.
Save the cleaned data as _cleaned_technology_news.csv_.
* Load:
Load the cleaned data into Snowflake's TECHNOLOGY_NEWS table in the ETL_DATA_WAREHOUSE database.
* Orchestration:
Use Prefect to automate and manage the ETL workflow.

## Licensing

This project is licensed under the MIT License.
Data is fetched from NewsAPI https://newsapi.org/. Please refer to their licensing terms for data usage policies.

