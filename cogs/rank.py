import requests
import discord
from discord.ext import commands

class ranks(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rank(self, ctx, region: str, riotName: str, riotId: str):
        url = ("https://api.kyroskoh.xyz/valorant/v1/mmr/" + region + "/" + riotName + "/" + riotId) #url for the API im using
        r = requests.get(url) #get the result of the API request
        await ctx.send(f'Your rank and current RR is: {r}') #send the user their rank info

async def setup(client):
    await client.add_cog(ranks(client))