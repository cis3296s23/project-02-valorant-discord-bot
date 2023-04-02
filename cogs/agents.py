import requests
import discord
from discord.ext import commands

class agents(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def agent(self, ctx, arg):
        r = requests.get("https://valorant-api.com/v1/agents")
        print(r.status_code)
        print(r.text)
        for entry in r.json()['data']:
            if entry['displayName'] == arg:
                await ctx.send(entry['uuid'])

async def setup(client):
    await client.add_cog(agents(client))