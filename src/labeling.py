import os
import pandas as pd

def label_entities(text):
  tokens = text.split()
  labeled_tokens = []
  
  for token in tokens:
    if "computer" in token:
      labeled_tokens.append((token, "B-Product"))
    elif token.lower() in ["addis", "abeba", "bole", "piassa", "arada", "kirkos", "yeka"]:
      labeled_tokens.append((token, "B-LOC"))
    elif "ዋጋ" in token:
      labeled_tokens.append((token, "B-PRICE"))
    else:
      labeled_tokens.append((token, "O"))
  return labeled_tokens

def save_labeled_data():
  os.makedirs('data/labeled_data', exist_ok=True)

  df = pd.read_csv('data/processed_data.csv')
  
  with open('data/labeled_data.conll', 'w', encoding='utf-8') as f:
    for index, row in df.iterrows():
      labeled_tokens = label_entities(row['Processed Message'])
      for token, label in labeled_tokens:
        f.write(f"{token} {label}\n")
      f.write("\n")  # Blank line to separate messages

if __name__ == "__main__":
  save_labeled_data()