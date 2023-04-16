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

        rank.strip() #remove spaces
        rr.strip() #remove spaces

        rankDataList = rank.split() #split on a space character to get rank name and number
        rankName = rankDataList[0] 
        rankNumber = rankDataList[1]
        rankFile = "" #this variable will be used for a check 1-3 on what rank they are in the category (we will combine all neccessary information later into this string to be read for a scope check)

        #   RR is formatted by everything being together so we do not need to format 
        #   it we can just iterate through it till we hit the first 'R' in "RR" to get the number we want

        if (rankName == "Iron"):
            print("users rank = iron")
            rankFile = rankName + "_" + rankNumber + "_Rank.png" #formatting for the file search
            embed = discord.Embed(title="Iron")
            await ctx.send("You rank is: " + rankName + " " + rankNumber, file = discord.File(rankFile) , embed = embed)

        if (rankName == "Bronze"):
            print("users rank = iron")
            rankFile = rankName + "_" + rankNumber + "_Rank.png" #formatting for the file search
            embed = discord.Embed(title="Bronze")
            await ctx.send("You rank is: " + rankName + " " + rankNumber, file = discord.File(rankFile) , embed = embed)

        if (rankName == "Silver"):
            print("users rank = iron")
            rankFile = rankName + "_" + rankNumber + "_Rank.png" #formatting for the file search
            embed = discord.Embed(title="Silver")
            await ctx.send("You rank is: " + rankName + " " + rankNumber, file = discord.File(rankFile) , embed = embed)

        if (rankName == "Gold"):
            print("users rank = iron")
            rankFile = rankName + "_" + rankNumber + "_Rank.png" #formatting for the file search
            embed = discord.Embed(title="Gold")
            await ctx.send("You rank is: " + rankName + " " + rankNumber, file = discord.File(rankFile) , embed = embed)

        if (rankName == "Platinum"):
            print("users rank = iron")
            rankFile = rankName + "_" + rankNumber + "_Rank.png" #formatting for the file search
            embed = discord.Embed(title="Platinum")
            await ctx.send("You rank is: " + rankName + " " + rankNumber, file = discord.File(rankFile) , embed = embed)

        if (rankName == "Diamond"):
            print("users rank = iron")
            rankFile = rankName + "_" + rankNumber + "_Rank.png" #formatting for the file search
            embed = discord.Embed(title="Diamond")
            await ctx.send("You rank is: " + rankName + " " + rankNumber, file = discord.File(rankFile) , embed = embed)

        if (rankName == "Ascendant"):
            print("users rank = iron")   
            rankFile = rankName + "_" + rankNumber + "_Rank.png" #formatting for the file search
            embed = discord.Embed(title="Ascendant")
            await ctx.send("You rank is: " + rankName + " " + rankNumber, file = discord.File(rankFile) , embed = embed)

        if (rankName == "Immortal"):
            print("users rank = iron") 
            rankFile = rankName + "_" + rankNumber + "_Rank.png" #formatting for the file search
            embed = discord.Embed(title="Immortal")
            await ctx.send("You rank is: " + rankName + " " + rankNumber, file = discord.File(rankFile) , embed = embed)

        if (rankName == "Radiant"):
            print("users rank = iron") 
            rankFile = rankName + "_" + rankNumber + "_Rank.png" #formatting for the file search
            embed = discord.Embed(title="Radiant")
            await ctx.send("You rank is: " + rankName + " " + rankNumber, file = discord.File(rankFile) , embed = embed)


        #TODO
        #what ima do, I am going to seperate the data and have a rank string and a RR string
        # I am going to do one if to check for 1, 2, 3
        #then check for name iron, bronze, silver, etc..
        #then give them the logo of the rank and embed that
        #if non of those works, the only rank that has no number is Radiant, so display radiant icon
        #then display a bar with percentage of the RR 0-100


async def setup(client):
    await client.add_cog(rankCommand(client))