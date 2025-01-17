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

async def scrape_channel(client, channel_username, writer, media_dir):
  entity = await client.get_entity(channel_username)
  channel_title = entity.title 
  async for message in client.iter_messages(entity, limit=500):
    media_path = None
    if message.media and hasattr(message.media, 'photo'):
      filename = f"{channel_username}_{message.id}.jpg"
      media_path = os.path.join(media_dir, filename)
      await client.download_media(message.media, media_path)
    
    writer.writerow([channel_title, channel_username, message.id, message.message, message.date, media_path])
    print(f"Scraped  from {channel_username}")

async def main():
  client = TelegramClient('user_session', api_id, api_hash)
  await client.start(phone=phone_number)
  async with client:
    media_dir = 'data/photos'
    os.makedirs(media_dir, exist_ok=True)
    os.makedirs('data/documents', exist_ok=True)

    with open('data/telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerow(['Sender', 'Timestamp', 'Content', 'Media Path'])

      channels = [
        '@nevacomputer',
      ]

      for channel in channels:
        await scrape_channel(client, channel, writer, media_dir)
        print(f"Scraping data from {channel}")

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())
