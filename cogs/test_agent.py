import asyncio
import discord.ext.commands as commands
from discord.ext.commands import Cog, command
import discord.ext.test as dpytest
import discord
import pytest
import pytest_asyncio
import requests

class agents(Cog):


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


@pytest_asyncio.fixture
async def bot():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents = intents)
    await bot._async_setup_hook()
    await bot.add_cog(agents())
    dpytest.configure(bot)
    return bot

@pytest.mark.asyncio
async def test_agent_list(bot):
    await dpytest.message("!agent list")
    assert dpytest.verify().message().contains("list")
