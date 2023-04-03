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
        print(arg)
        if arg == 'list':
            await ctx.send("List not yet implemented")
        else:
            for entry in r.json()['data']:
                if entry['displayName'] == arg:
                    uuid = entry['uuid']
                    displayIcon = entry['displayIconSmall']
                    description = entry['description']

                    break
            embed = discord.Embed(title=arg, description = description, colour = discord.Colour.random())
            embed.set_thumbnail(url=displayIcon)
            await ctx.send(embed=embed)
                #await ctx.send(entry['uuid'])
        

async def setup(client):
    await client.add_cog(agents(client))