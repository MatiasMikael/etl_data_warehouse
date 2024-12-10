import os
import pandas as pd

def clean_and_filter_data(input_file, output_file):
    print("Step 1: Reading the CSV file...")
    df = pd.read_csv(input_file)

    print("Step 2: Dropping rows with missing values...")
    df.dropna(inplace=True)

    print("Step 3: Removing duplicate rows...")
    df.drop_duplicates(inplace=True)

    print("Step 4: Filtering articles published in the last 7 days...")
    df["Published At"] = pd.to_datetime(df["Published At"])
    current_time = pd.Timestamp.now(tz="UTC")
    filtered_df = df[df["Published At"] >= current_time - pd.Timedelta(days=7)]

    print("Step 5: Saving cleaned and filtered data...")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure directory exists
    filtered_df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    input_file = "../2_data/technology_news.csv"
    output_file = "../2_data/cleaned_technology_news.csv"
    print("Starting data cleaning process...")
    clean_and_filter_data(input_file, output_file)
    print("Data cleaning process completed!")