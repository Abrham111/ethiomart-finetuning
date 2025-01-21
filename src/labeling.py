import re
import pandas as pd

# Load dataset
data = pd.read_csv("data/preprocessed_data.csv")

# Define entity labeling function
def label_text_conll(message):
  labels = []
  tokens = str(message).split()  # Convert to string and tokenize
  for token in tokens:
    if re.search(r"\b(ELITEBOOK|LENOVO|HP|ኮምፒውተር|NEVA|COMPUTER|NOTEBOOK)\b", token, re.IGNORECASE):
      labels.append(f"{token}\tB-Product")
    elif re.search(r"\bPrice\b", token, re.IGNORECASE) or re.search(r"\d+ብር", token):
      labels.append(f"{token}\tB-PRICE" if re.search(r"\bPrice\b", token, re.IGNORECASE) else f"{token}\tI-PRICE")
    elif re.search(r"\bመገናኛ\b", token):
      labels.append(f"{token}\tB-LOC")
    else:
      labels.append(f"{token}\tO")
  labels.append("")  # Add blank line after each sentence
  return "\n".join(labels)

def save_labeled_data():
  # Label a subset of the data
  subset = data["Cleaned_Content"].head(100)  # Use first 100 rows for labeling
  labeled_data = "\n".join([label_text_conll(msg) for msg in subset])

  # Save labeled data in CoNLL format
  with open("data/labeled_data.conll", "w", encoding="utf-8") as file:
    file.write(labeled_data)
