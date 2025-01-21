import pandas as pd
import re

# Load dataset
data = pd.read_csv("data/telegram_data.csv")

# Remove rows with NaN values in the "Content" column
data = data.dropna(subset=["Content"])

# Define stopwords
stopwords = ["እና", "ለ", "በ", "ነበር", "እየ", "የተ", "እየነበር"]

def preprocess_text(text):
  # Normalize text: Remove unnecessary characters, links, and mentions
  text = str(text)  # Convert to string
  text = re.sub(r"http\S+|@\S+|#[^\s]+", "", text)  # Remove links, mentions, hashtags
  text = re.sub(r"[^\w\s።፣፤፥፦፧፨፡]", "", text)  # Remove non-Amharic punctuation
  text = re.sub(r"\s+", " ", text.strip())  # Remove extra spaces

  # Tokenize
  tokens = text.split()
  
  # Remove stopwords
  tokens = [token for token in tokens if token not in stopwords]

  return " ".join(tokens)

def process_raw_data():
  # Preprocess each message in the dataset
  data["Cleaned_Content"] = data["Content"].apply(preprocess_text)

  # Save structured data
  data[["Sender", "Timestamp", "Cleaned_Content"]].to_csv("data/preprocessed_data.csv", index=False)
