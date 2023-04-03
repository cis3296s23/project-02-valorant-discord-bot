import discord
import asyncio
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
    await client.start('MTA4NDc3NzAyMjY5OTYwNjA3OA.GKqz0c.3AMh905UuqN5VhqGynEpybQocRUQGcnHdePgdI')

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

asyncio.run(main())