import requests
import discord
from discord.ext import commands
from bs4 import BeautifulSoup

class stats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def aim(self, ctx, riotName:str,riotTag:str):
        #Formats input from user and creates url with info
        url = ("https://blitz.gg/valorant/profile/"+riotName+"-"+riotTag)
        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'lxml')
        print("Here")
        #The following will scrape the shot percentages from the user profile
        headShots = soup.find(attrs = {'class':'type-body2-form--active stat-value body-head'}).getText()
        bodyShots = soup.find(attrs ={'class':'type-body2-form--active stat-value body-chest'}).getText()
        legShots = soup.find(attrs ={'class':'type-body2-form--active stat-value body-legs'}).getText()

        #Formats the above into an embed to be printed on Discord
        embed = discord.Embed(title=riotName+"'s Aim Stats", description="Over the last 20 Matches...", colour = discord.Colour.blue())
        embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/1692/1692908.png')
        embed.add_field(name= "Head Shots:", value = headShots, inline = False)
        embed.add_field(name= "Body Shots:", value = bodyShots, inline = False)
        embed.add_field(name= "Leg Shots:", value = legShots, inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    async def stats(self, ctx,riotName:str,riotTag:str):
        URL = "https://tracker.gg/valorant/profile/riot/"+ riotName + "%23"+ riotTag
        #Connects to webpage
        r = requests.get(URL)
        #Get content of webpage 
        soup = BeautifulSoup(r.content, 'lxml')
        #Filter HTML Tree to find for stats
        table = soup.find('div', attrs = {'class':'giant-stats'}) 
        value = table.findAll('span', attrs = {'class':'value'})
        #Get users image
        table2 = soup.find('div', attrs = {'class':'ph__container'}) 
        image = table2.find('img', attrs = {'class':'user-avatar__image'})

        #Create array for values
        arr = []
        #loop to find all values in value header
        for values in value:
            #.string extension will get the value in the tree and not the other stuff in the HTML Tree
            arr.append(values.string)
        embed = discord.Embed(title='Current Competitive Season Stats', description = 'Stats of player: '+riotName, colour = discord.Colour.random())
        embed.set_thumbnail(url='https://img.icons8.com/color/512/valorant.png')
        embed.add_field(name= "Damage/Round: ", value = arr[0], inline = False)
        embed.add_field(name= "K/D Ratio: ", value = arr[1], inline = False)
        embed.add_field(name= "Headshot%: ", value = arr[2], inline = False)
        embed.add_field(name= "WinRate: ", value = arr[3], inline = False)
        await ctx.send(embed=embed)

    #This command does not work
    @commands.command()
    async def matches(self, ctx, riotName:str, riotTag:str):
        URL = "https://tracker.gg/valorant/profile/riot/"+ riotName + "%23"+ riotTag
        #Connects to webpage
        r = requests.get(URL)
        #Get content of webpage 
        soup = BeautifulSoup(r.content, 'lxml')
        #Filter HTML Tree to find
        table = soup.find('div', attrs = {'class':'trn-gamereport-list__group-entries'}) 
        value = table.find('div', attrs = {'vmr-stats trn-match-row__section trn-match-row__section--right gap-4'})
async def setup(client):
    await client.add_cog(stats(client))