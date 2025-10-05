import discord
from discord.ext import tasks, commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN') 

client = commands.Bot(command_prefix='idfk know bro go wild',intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('Bot is ready to send messages!')
    channel_id = int(input("what channel (copy channel)?: "))
    while 7==7:
        channel = client.get_channel(channel_id)
        message = input("message or say 'change' to switch channel, or reply to reply: ")
        if message == "change":
            channel_id = int(input("what channel?: "))
        if message == "reply":
            reply_id = int(input("reply to what id?:"))
            message_to_reply = await channel.fetch_message(reply_id)
            message = input("give the message: ")
            await message_to_reply.reply(message)
        else:
            await channel.send(message)


client.run(TOKEN)