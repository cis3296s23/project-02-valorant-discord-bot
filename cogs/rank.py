import requests
import discord
import os
from discord.ext import commands

class rankCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rank(self, ctx, region: str, riotName: str, riotId: str):
        url = ("https://api.kyroskoh.xyz/valorant/v1/mmr/" + region + "/" + riotName + "/" + riotId) #url for the API im using
        r = requests.get(url) #get the result of the API request

        #get the users data
        if r.status_code == 200: #if the request from API was successful
            data = r.text #parse the text
            print("Got the users data for their rank: " + data)
        else:
            print(f"Request failed with status code: {r.status_code}")
            await ctx.send("Your entered region, name, or ID is incorrect, please try again!") #ask the user to try again

        #split into a list with list[0] = rank , and list[1] = RR
        dataList = data.split('-')
        rank = dataList[0]
        rr = dataList[1]

        #remove spaces
        rank.strip() 
        rr.strip()

        #flag variable to catch radiants in future edge case checking
        radiantFlag = 0

        #edge case buisiness to catch radiants
        if ("Radiant" in rank): #scope check so that radiants can make it through
            print("Radiant detected! changing flag!")
            radiantFlag = 1
        else:
            #split on a space character to get rank name and number
            rankDataList = rank.split() 
            rankName = rankDataList[0] 
            rankNumber = rankDataList[1]

            #get the current working directory
            currentWorkingDirectory = os.getcwd() 
            rankFile = currentWorkingDirectory + "/images/ranks/" + rankName + "_" + rankNumber + "_Rank.png" #formatting for the file search
            noRankBugFlag = 0 #if this is zero it means we never hit a rank meaning a bug is present

            #set the file for discord
            disRankFile = discord.File(rankFile)
        

        #rank data scope searching
        if (radiantFlag == 1):
            #get current working directory
            currentWorkingDirectory = os.getcwd() 
            #reset the file path
            rankFile = currentWorkingDirectory + "/images/ranks/Radiant_Rank.png"
            #set the file for discord for just Radiant ranks
            #this is because radiant ranks do not have numbers
            disRankFileRadiant = discord.File(rankFile)
            noRankBugFlag = 1
            print("users rank = Radiant") 
            embed = discord.Embed(title="Radiant", color=discord.Color.from_rgb(255, 255, 255))
            embed.set_image(url ="attachment://" + disRankFileRadiant.filename)
            await ctx.send(file = disRankFileRadiant, embed = embed)

        if (rankName == "Iron"):
            noRankBugFlag = 1
            print("users rank = Iron")
            embed = discord.Embed(title="Iron "+ rankNumber, color=discord.Color.dark_gray()) #setting title, and color banner for embedding
            embed.set_image(url ="attachment://" + disRankFile.filename) #setting local file to be present in embedding
            await ctx.send(file = disRankFile, embed = embed) #sending the message to the user

        if (rankName == "Bronze"):
            noRankBugFlag = 1
            print("users rank = Bronze")
            embed = discord.Embed(title="Bronze "+ rankNumber, color=discord.Color.dark_gold())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Silver"):
            noRankBugFlag = 1
            print("users rank = Silver")
            embed = discord.Embed(title="Silver "+ rankNumber, color=discord.Color.light_gray())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Gold"):
            noRankBugFlag = 1
            print("users rank = Gold")
            embed = discord.Embed(title="Gold "+ rankNumber, color=discord.Color.gold())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Platinum"):
            noRankBugFlag = 1
            print("users rank = Platinum")
            embed = discord.Embed(title="Platinum "+ rankNumber, color=discord.Color.teal())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Diamond"):
            noRankBugFlag = 1
            print("users rank = Diamond")
            embed = discord.Embed(title="Diamond "+ rankNumber, color=discord.Color.purple())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Ascendant"):
            noRankBugFlag = 1
            print("users rank = Ascendant")   
            embed = discord.Embed(title="Ascendant "+ rankNumber, color=discord.Color.green())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Immortal"):
            noRankBugFlag = 1
            print("users rank = Immortal") 
            embed = discord.Embed(title="Immortal "+ rankNumber, color=discord.Color.red())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        #scope check for if we do not execute any of the above if statements regarding the users rank and the image displayed
        if (noRankBugFlag == 0):
            print("ISSUE!!: No rank found for user")
            await ctx.send("We could not find a rank to display based on your rank")

        #RR percentage printing and formatting

        #TODO
        #then display a bar with percentage of the RR 0-100
        #make a way to test every rank output without the need of someones account info?


async def setup(client):
    await client.add_cog(rankCommand(client))