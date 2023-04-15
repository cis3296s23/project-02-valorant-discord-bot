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
            nameList = []
            for entry in r.json()['data']:
                print(entry['displayName'])
                nameList.append(entry['displayName'])
            nameList = '\n'.join(nameList)
            embed = discord.Embed(title='Agents', description = 'List of playable agents', colour = discord.Colour.brand_red())
            embed.add_field(name="List of agents", value=nameList)
            await ctx.send(embed = embed)
        else:
            for entry in r.json()['data']:
                if entry['displayName'] == arg:
                    embed = discord.Embed(title=arg, description = entry['description'], colour = discord.Colour.random())
                    embed.set_thumbnail(url=entry['displayIconSmall'])
                    for ability in entry['abilities']:
                        print(ability['displayName'])
                        embed.add_field(name= ability['displayName'], value = ability['description'], inline = False)
                    break
                    
            await ctx.send(embed=embed)
        

async def setup(client):
    await client.add_cog(agents(client))