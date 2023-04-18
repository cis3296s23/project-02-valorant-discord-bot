import discord
import random
from discord.ext import commands

class recommend(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    # #Function to check if each response the user types is a valid option and if not to re-ask the question
    # async def get_valid_response(self, ctx, question):
    #     while True:
    #         response = await self.client.wait_for("message", check=lambda message: message.author == ctx.author)
    #         if response.content.lower() in question:
    #             return response.content.lower()
    #         else:
    #             await ctx.send("Invalid input. Please provide a valid response.")
    #             response = await self.client.wait_for("message", check=lambda message: message.author == ctx.author)
    
    
    @commands.command()
    async def recommend(self, ctx):
        await ctx.send("Welcome to the Valorant Agent Recommender!")
        await ctx.send("Please answer the following questions to find the best agent for you.\n\n")
        await ctx.send(" ")

        #List of questions
        questions = [
            {
                "question": "Do you prefer playing aggressively or defensively? (Enter 'aggressive' or 'defensive'): ",
                "aggressive": ["Jett", "Raze", "Reyna", "Phoenix", "Yoru", "Breach", "KAY/O", "Breach", "Neon", "Fade", "Gekko"],
                "defensive": ["Viper", "Omen", "Cypher", "Sova", "Brimstone", "Skye", "Sage", "Astra", "Killjoy", "Chamber", "Harbor"],
            },
            {
                "question": "Do you prefer close-range or long-range combat? (Enter 'close' or 'long'): ",
                "close": ["Jett", "Raze", "Reyna", "Phoenix", "Yoru", "Breach", "Killjoy", "Fade"],
                "long": ["Viper", "Omen", "Cypher", "Sova", "Brimstone", "Skye", "KAY/O", "Sage", "Astra", "Harbor"],
            },
            {
                "question": "Do you enjoy supporting your teammates? (Enter 'yes' or 'no'): ",
                "yes": ["Omen", "Brimstone", "Viper", "Astra", "Sage", "Cypher", "Killjoy", "Sova", "Skye", "Harbor"],
                "no": ["Jett", "Raze", "Reyna", "Phoenix", "Yoru", "Breach", "KAY/O", "Neon"],
            },
            {
                "question": "Do you prefer an agent with more self-sustain capabilities? (Enter 'yes' or 'no'): ",
                "yes": ["Phoenix", "Reyna", "Sage", "Neon"],
                "no": [],
            },
            {
                "question": "Do you like using gadgets and traps? (Enter 'yes' or 'no'): ",
                "yes": ["Cypher", "Killjoy", "Viper", "Astra", "Brimstone", "KAY/O", "Fade"],
                "no": [],
            },
            {
                "question": "Do you enjoy controlling the battlefield with abilities? (Enter 'yes' or 'no'): ",
                "yes": ["Viper", "Astra", "Brimstone", "Omen", "Breach", "Harbor"],
                "no": [],
            },
            {
                "question": "Do you like playing stealthy or elusive agents? (Enter 'yes' or 'no'): ",
                "yes": ["Yoru", "Omen", "Cypher", "Fade"],
                "no": [],
            },
            {
                "question": "Do you prefer agents with area denial abilities? (Enter 'yes' or 'no'): ",
                "yes": ["Killjoy", "Viper", "Cypher", "Sova", "Neon", "Harbor"],
                "no": [],
            },
            {
                "question": "Do you enjoy entry fragging or getting the first kill? (Enter 'yes' or 'no'): ",
                "yes": ["Phoenix", "Jett", "Raze", "Reyna"],
                "no": [],
            },
        ]


        #List of agents
        agents = {
            agent: 0 for agent in [
                "Brimstone", "Phoenix", "Sage", "Sova", "Viper", "Cypher", "Reyna", "Killjoy", "Breach", "Omen", "Jett", "Raze", "Skye", "Yoru", "Astra", "KAY/O", "Chamber", "Neon", "Fade", "Harbor", "Gekko"
            ]
        }

        #Loop through each of the questions and based on each response, increment those agents' scores
        for question in questions:
            await ctx.send(question["question"])
            answer = await self.client.wait_for("message", check=lambda message: message.author == ctx.author)

            if answer.content.lower() in question:
                affected_agents = question[answer.content.lower()]
                for agent in affected_agents:
                    agents[agent] += 1
        
        
        #Collect the agent(s) who have the highest score and randomly select one to recommend to the user
        max_score = max(agents.values())
        top_agents = [agent for agent, score in agents.items() if score == max_score]

        recommended_agent = random.choice(top_agents)
        await ctx.send(f"Based on your answers, you should try playing as {recommended_agent}!")
        
async def setup(client):
    await client.add_cog(recommend(client))