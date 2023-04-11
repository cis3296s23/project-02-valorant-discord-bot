from discord.ext import commands

class recommend(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    
    @commands.command()
    async def recommend(self, ctx):
        await ctx.send("Welcome to the Valorant Agent Recommender!")
        await ctx.send("Please answer the following questions to find the best agent for you.\n")



async def setup(client):
    await client.add_cog(recommend(client))