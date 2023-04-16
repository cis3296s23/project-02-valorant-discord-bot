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

        #working code for now
        if r.status_code == 200: #if the request from API was successful
            data = r.text #parse the text
            print(data)
            await ctx.send(f'Your rank and current RR is: {data}') #send the user their rank info
        else:
            print(f"Request failed with status code: {r.status_code}")
            await ctx.send("Your entered region, name, or ID is incorrect, please try again!") #ask the user to try again

        dataList = data.split('-') #split into a list with list[0] = rank , and list[1] = RR
        rank = dataList[0]
        rr = dataList[1]
        
        #TODO
        #what ima do, I am going to seperate the data and have a rank string and a RR string
        # I am going to do one if to check for 1, 2, 3
        #then check for name iron, bronze, silver, etc..
        #then give them the logo of the rank and embed that
        #if non of those works, the only rank that has no number is Radiant, so display radiant icon
        #then display a bar with percentage of the RR 0-100


async def setup(client):
    await client.add_cog(rankCommand(client))