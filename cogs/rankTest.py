import discord
import os
from discord.ext import commands

class rankTestCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rankTest(self, ctx, rankName: str, rankNumber: str):

        radiantFlag = 0
        noRankBugFlag = 0 #no rank entered

        if (rankName == "Radiant" or rankName == "radiant"):
            radiantFlag = 1
        else:
            currentWorkingDirectory = os.getcwd() 
            rankFile = currentWorkingDirectory + "/images/ranks/" + rankName + "_" + rankNumber + "_Rank.png" #formatting for the file search
            disRankFile = discord.File(rankFile)

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

        if (rankName == "Iron" or rankName == "iron"):
            noRankBugFlag = 1
            print("users rank = Iron")
            embed = discord.Embed(title="Iron "+ rankNumber, color=discord.Color.dark_gray()) #setting title, and color banner for embedding
            embed.set_image(url ="attachment://" + disRankFile.filename) #setting local file to be present in embedding
            await ctx.send(file = disRankFile, embed = embed) #sending the message to the user

        if (rankName == "Bronze" or rankName == "bronze"):
            noRankBugFlag = 1
            print("users rank = Bronze")
            embed = discord.Embed(title="Bronze "+ rankNumber, color=discord.Color.dark_gold())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Silver" or rankName == "silver"):
            noRankBugFlag = 1
            print("users rank = Silver")
            embed = discord.Embed(title="Silver "+ rankNumber, color=discord.Color.light_gray())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Gold" or rankName == "gold"):
            noRankBugFlag = 1
            print("users rank = Gold")
            embed = discord.Embed(title="Gold "+ rankNumber, color=discord.Color.gold())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Platinum" or rankName == "platinum"):
            noRankBugFlag = 1
            print("users rank = Platinum")
            embed = discord.Embed(title="Platinum "+ rankNumber, color=discord.Color.teal())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Diamond" or rankName == "diamond"):
            noRankBugFlag = 1
            print("users rank = Diamond")
            embed = discord.Embed(title="Diamond "+ rankNumber, color=discord.Color.purple())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Ascendant" or rankName == "ascendant"):
            noRankBugFlag = 1
            print("users rank = Ascendant")   
            embed = discord.Embed(title="Ascendant "+ rankNumber, color=discord.Color.green())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

        if (rankName == "Immortal" or rankName == "immortal"):
            noRankBugFlag = 1
            print("users rank = Immortal") 
            embed = discord.Embed(title="Immortal "+ rankNumber, color=discord.Color.red())
            embed.set_image(url ="attachment://" + disRankFile.filename)
            await ctx.send(file = disRankFile, embed = embed)

async def setup(client):
    await client.add_cog(rankTestCommand(client))