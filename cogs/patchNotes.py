import requests
import discord
from discord.ext import commands

class patchNotes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def patchnotes(self, ctx):
        url = ("https://playvalorant.com/page-data/en-us/news/game-updates/page-data.json")
        data = requests.get(url).json()

        for a in reversed(data["result"]["pageContext"]["data"]["articles"]):
            if "Patch Notes" in a["title"]:
                patch_notes_url = "https://playvalorant.com" + a["url"]["url"]
        await ctx.send(patch_notes_url)
    
async def setup(client):
    await client.add_cog(patchNotes(client))