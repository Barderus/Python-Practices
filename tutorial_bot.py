'''
    Follow along discord bot tutorial from RealPython: https://realpython.com/how-to-make-a-discord-bot-python/
'''

# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

''' 
    A Client is an object that represents a connection to Discord. 
    A Client handles events, tracks state, and generally interacts with Discord APIs.
'''
client = discord.Client()

@client.event
async def on_ready():
    '''
        handles the event when the Client has established a connection to Discord and it has finished preparing the data that Discord
        has sent, such as login state, guild and channel data, and more.
    '''
    print(f'{client.user} has connected to Discord!')
    
client.run(TOKEN)
