import pandas as pd
import re

# Define patterns for entities
patterns = {
  'B-PRICE': r'\bPrice\b',
  'I-PRICE': r'\b\d+\b|ብር',
  'B-LOC': r'\bአዲስ\b',
  'I-LOC': r'\bአበባ\b',
  'B-Product': r'\bLaptop\b'
}

def label_entities(text):
  tokens = text.split()
  labeled_tokens = []
  for token in tokens:
    label = 'O'  # Default label
    for entity, pattern in patterns.items():
      if re.match(pattern, token):
        label = entity
        break
    labeled_tokens.append((token, label))
  return labeled_tokens

def save_labeled_data():
  # Load dataset
  df = pd.read_csv('data/processed_data.csv')
  if 'Processed Message' not in df.columns:
    raise ValueError("Column 'Processed Message' not found in the dataset.")
  
  # Save labeled data in CoNLL format
  with open('data/labeled_data.conll', 'w', encoding='utf-8') as f:
    for _, row in df.iterrows():
      labeled_tokens = label_entities(row['Processed Message'])
      for token, label in labeled_tokens:
        f.write(f"{token}\t{label}\n")
      f.write("\n")  # Blank line to separate messages
    print("Labeled data saved to 'data/labeled_data.conll'")

if __name__ == "__main__":
  save_labeled_data()
