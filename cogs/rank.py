import requests
import discord
from discord.ext import commands

class rankCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rank(self, ctx, region: str, riotName: str, riotId: str):
        url = ("https://api.kyroskoh.xyz/valorant/v1/mmr/" + region + "/" + riotName + "/" + riotId) #url for the API im using
        r = requests.get(url) #get the result of the API request

        if r.status_code == 200: #if the request from API was successful
            data = r.text #parse the text
            print(data)
            await ctx.send(f'Your rank and current RR is: {data}') #send the user their rank info
        else:
            print(f"Request failed with status code: {r.status_code}")
            await ctx.send("Your entered region, name, or ID is incorrect, please try again!") #ask the user to try again

        '''
            TODO:
                Make it so the user is presented with a better output and not just text
                    - meaning give icons per rank
                    - maybe implement a bar to show the percentage of RR from 0-100%
                    - add fields to make it more clear how the user should type in the arguments for the command to work
                    - update help command to explain how to do this properly
        '''

async def setup(client):
    await client.add_cog(rankCommand(client))