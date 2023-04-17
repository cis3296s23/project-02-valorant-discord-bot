import discord
import asyncio
import keepToken
import os
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await client.start(keepToken.token) #for this to work for you please see intructions below
    '''
        please make a keepToken.py file, and just put in 'token = "enter the discord token here"'
        put in your .gitignore file
            "keepToken.py"
        now you can commit your main everytime without having the token reset and you'll be able to start the bot normally
    '''

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

asyncio.run(main())