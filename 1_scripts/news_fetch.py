import os
import requests
import csv

def fetch_technology_news(api_key, language="en"):
    print("Step 1: Fetching technology news from NewsAPI...")
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "technology",
        "language": language,
        "apiKey": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Step 1 Completed: News data fetched successfully!")
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def save_news_to_csv(news_data, filename):
    print("Step 2: Saving news data to CSV file...")
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Ensure directory exists
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Source", "Published At", "URL"])
        for article in news_data.get("articles", []):
            writer.writerow([
                article["title"],
                article["source"]["name"],
                article["publishedAt"],
                article["url"]
            ])
    print(f"Step 2 Completed: News data saved to {filename}")

if __name__ == "__main__":
    API_KEY = "f9621aed6c0d43218a6e79df90815080"  # Replace with your actual API key
    filename = "../2_data/technology_news.csv"

    print("Starting the news fetching process...")
    news_data = fetch_technology_news(API_KEY)

    if news_data:
        save_news_to_csv(news_data, filename)
        print("News fetching and saving process completed successfully!")