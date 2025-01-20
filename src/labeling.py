import re
import pandas as pd

# Load dataset
data = pd.read_csv("data/preprocessed_data.csv")

# Define entity labeling function
def label_text_conll(message):
  labels = []
  tokens = str(message).split()  # Convert to string and tokenize
  for token in tokens:
    if "ELITEBOOK" in token or "LENOVO" in token or "DELL" in token:
      labels.append(f"{token}\tB-Product")
    elif "Price" in token or re.search(r"\d+ብር", token):
      labels.append(f"{token}\tB-PRICE" if token == "Price" else f"{token}\tI-PRICE")
    elif "መገናኛ" in token:
      labels.append(f"{token}\tB-LOC")
    else:
      labels.append(f"{token}\tO")
  labels.append("")  # Add blank line after each sentence
  return "\n".join(labels)

def save_labeled_data():
  # Label a subset of the data
  subset = data["Cleaned_Content"].head(30)  # Use first 30 rows for labeling
  labeled_data = "\n".join([label_text_conll(msg) for msg in subset])

  # Save labeled data in CoNLL format
  with open("data/labeled_data.conll", "w", encoding="utf-8") as file:
    file.write(labeled_data)
