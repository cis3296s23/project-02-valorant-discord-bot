import requests
import discord
from discord.ext import commands

class getRanksCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def ranks(self, ctx):
        print("ranks command called")
        e = discord.Embed(title = "Ranks", description="These are the ranks in Valorant, you have a singe rank type (bronze, silver, gold, etc...) and every rank type (except for radiant) has a number 1-3 to distinguish you from others in your rank type (example: platinum 1 is a lower rank than platinum 3)")
        e.set_image(url="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blte5a6438f76e89acf/5eec2c0f34f8f30c7cfb3025/VALORANT_ICONS_2.jpg")
        await ctx.send(embed=e)
        
async def setup(client):
    await client.add_cog(getRanksCommand(client))