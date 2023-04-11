import requests
import discord
from discord.ext import commands

class skinSearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def skin(self, ctx, arg1, arg2):
            r = requests.get("https://valorant-api.com/v1/weapons/skins")
            print(r.status_code)
            print(arg1)
            print(arg2)
            arg1 += " "
            arg1 += arg2
            print(arg1)
            for entry in r.json()['data']:
                if entry['displayName'] == arg1:
                    #await ctx.send("The skin has been found")
                    displayIcon = entry['displayIcon']
                    break
            embed = discord.Embed(title=arg1, colour = discord.Colour.random())
            embed.set_image(url=displayIcon)
            await ctx.send(embed=embed)
            #await ctx.send(displayIcon)

async def setup(client):
    await client.add_cog(skinSearch(client))