import requests
import discord
from discord.ext import commands

class getRanks(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def rank(ctx):
        file = discord.File("valorant_rank_icons.jpg")
        e = discord.Embed()
        e.set_image(url="attachment://valorant_rank_icons.jpg")
        await ctx.send(file=file, embed=e)
        
async def setup(client):
    await client.add_cog(getRanks(client))