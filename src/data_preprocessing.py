import os
import re
import pandas as pd

def preprocess_text(text):
  # Normalize text: lowercasing and removing special characters
  text = text.lower()
  text = re.sub(r'[^\w\s]', '', text)
  return text.strip()

def process_raw_data():
  os.makedirs('data/processed_data', exist_ok=True)

  # Read from the CSV file generated in data ingestion
  df = pd.read_csv('data/telegram_data.csv')
  
  # Preprocess the message column
  df['Processed Message'] = df['Message'].apply(preprocess_text)

  # Save the processed data
  df.to_csv('data/processed_data.csv', index=False)

if __name__ == "__main__":
  process_raw_data()