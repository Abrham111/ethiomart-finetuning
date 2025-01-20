import os
import csv
import re
from telethon import TelegramClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone_number = os.getenv('PHONE_NUMBER')

async def scrape_channel(client, channel_username, writer):
  entity = await client.get_entity(channel_username)
  async for message in client.iter_messages(entity):    
    writer.writerow([channel_username, message.id, message.message, message.date])
    print(f"Scraping {message} from {channel_username}")

async def main():
  client = TelegramClient('user_session', api_id, api_hash)
  await client.start(phone=phone_number)
  async with client:

    with open('data/telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerow(['Sender', 'id', 'Content', 'Timestamp',])

      channels = [
        '@nevacomputer',
      ]

      for channel in channels:
        await scrape_channel(client, channel, writer)
        print(f"Scraped data  from {channel}")

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())
