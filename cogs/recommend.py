from discord.ext import commands

class recommend(commands.Cog):
    def __init__(self, client):
        self.client = client

    def ask_question(question):
        print(question)
        answer = input().lower()
        return answer
    
    def update_agent_scores(agents, affected_agents, points):
        for agent in affected_agents:
            agents[agent] += points

    
    @commands.command()
    async def recommend(self, ctx):
        await ctx.send("Welcome to the Valorant Agent Recommender!")
        await ctx.send("Please answer the following questions to find the best agent for you.\n")

        questions = [
            {
                "question": "Do you prefer playing aggressively or defensively? (Enter 'aggressive' or 'defensive'): ",
                "aggressive": ["Jett", "Raze", "Reyna", "Phoenix", "Yoru", "Breach", "KAY/O"],
                "defensive": ["Viper", "Omen", "Cypher", "Sova", "Brimstone", "Skye", "Sage", "Astra", "Killjoy"],
            },
            {
                "question": "Do you prefer close-range or long-range combat? (Enter 'close' or 'long'): ",
                "close": ["Jett", "Raze", "Reyna", "Phoenix", "Yoru", "Breach", "Killjoy"],
                "long": ["Viper", "Omen", "Cypher", "Sova", "Brimstone", "Skye", "KAY/O", "Sage", "Astra"],
            },
            {
                "question": "Do you enjoy supporting your teammates? (Enter 'yes' or 'no'): ",
                "yes": ["Omen", "Brimstone", "Viper", "Astra", "Sage", "Cypher", "Killjoy", "Sova", "Skye"],
                "no": ["Jett", "Raze", "Reyna", "Phoenix", "Yoru", "Breach", "KAY/O"],
            },
            {
                "question": "Do you prefer an agent with more self-sustain capabilities? (Enter 'yes' or 'no'): ",
                "yes": ["Phoenix", "Reyna", "Sage"],
                "no": [],
            },
            {
                "question": "Do you like using gadgets and traps? (Enter 'yes' or 'no'): ",
                "yes": ["Cypher", "Killjoy", "Viper", "Astra", "Brimstone", "KAY/O"],
                "no": [],
            },
        ]





async def setup(client):
    await client.add_cog(recommend(client))