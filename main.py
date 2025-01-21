from src.data_ingestion import main as data_ingestion
from src.data_preprocessing import process_raw_data
from src.labeling import save_labeled_data

if __name__ == "__main__":
  # import asyncio
  # asyncio.run(data_ingestion())
  process_raw_data()
  save_labeled_data()