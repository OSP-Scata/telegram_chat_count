from telethon.sync import TelegramClient, types
from asyncio import run

comments = []
name = 'parsecomments'
api_id = 24716440
api_hash = "179bce2ba1a80be579160b84b7c355a7"

chat = input("Enter chat name: ")
post = int(input("Enter post ID: "))


async def messages_func(name, api_id, api_hash):
    async with TelegramClient(name, api_id, api_hash) as client:
        print("Extracting messages")
        async for message in client.iter_messages(chat, reply_to=post, reverse=True):
            if isinstance(message.sender, types.User):
                comments.append(message.date, ',', message.sender.first_name, ',', message.text)
            else:
                comments.append(message.date, ',', message.sender.title, ',', message.text)


run(messages_func(name, api_id, api_hash))
outfile = 'result.csv'
with open(outfile, 'w', encoding='utf8') as file:
    for comment in comments:
        file.write(f'{comment},\n')
