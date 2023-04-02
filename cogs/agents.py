import discord
from discord.ext import commands

class agents(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def agent(self, ctx, arg):
        if arg == '':
            await ctx.send("No argument supplied")
        if arg == 'sova':
            await ctx.send("Sova")

async def setup(client):
    await client.add_cog(agents(client))