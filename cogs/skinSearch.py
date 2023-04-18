import requests
import discord
from discord.ext import commands

class skinSearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def skin(self, ctx, *arg):
            r = requests.get("https://valorant-api.com/v1/weapons/skins")
            print(r.status_code)
            print(arg)
            str = ' '.join(arg)
            print(str)
            for entry in r.json()['data']:
                if entry['displayName'] == str:
                    #await ctx.send("The skin has been found")
                    displayIcon = entry['displayIcon']
                    break
            embed = discord.Embed(title=str, colour = discord.Colour.random())
            embed.set_image(url=displayIcon)
            await ctx.send(embed=embed)
            #await ctx.send(displayIcon)

    @commands.command()
    async def bundle(self, ctx, *arg):
            r = requests.get("https://valorant-api.com/v1/bundles")
            print(r.status_code)
            print(arg)
            str = ' '.join(arg)
            print(str)
            if str == 'list':
                nameList = []
                for entry in r.json()['data']:
                    print(entry['displayName'])
                    nameList.append(entry['displayName'])
                nameList = '\n'.join(nameList)
                embed = discord.Embed(title='Bundles', description = 'List of valid bundles', colour = discord.Colour.brand_red())
                embed.add_field(name="You can use these names with the skins command as well:", value=nameList)
                await ctx.send(embed = embed)
            else:
                for entry in r.json()['data']:
                    if entry['displayName'] == str:
                        #await ctx.send("The skin has been found")
                        displayIcon = entry['displayIcon']
                        break
                embed = discord.Embed(title=str, colour = discord.Colour.random())
                embed.set_image(url=displayIcon)
                await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(skinSearch(client))