import os
import discord
from discord.ext import commands
from dotenv import load_dotenv 
# import main

# Difficulty modes
def_modes = [20, 10, 5, 1]

# Load env file
load_dotenv()

# Instantiating the bot with a prefix
client = commands.Bot(command_prefix='aq', help_command=None, case_insensitive=True, strip_after_prefix=True, intents=discord.Intents.all()) 
# Setting all intents true


# the on_ready function starts when the bot is ready to recieve commands 
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Guess the anime"))
    print("Bot is ready")

# Custom help command
@client.command()
async def help(ctx):
    embed = discord.Embed(title="aniQuiz Help", description="Commands and some stuff about the bot", color=0xFF5733)
    embed.add_field(name="Commands", value="""
    -> `aq start` : Starts the quiz

    -> `aq end` : Ends the quiz

    -> `aq board` : Shows the leaderboard

    -> `aq ping` : Shows latency of the bot

    -> aq help : displays available commands
    """, inline=False)
    embed.set_footer(text="If you enjoyed using this bot please give us a star and consider donating, makes our day tbh.")
    await ctx.send(embed=embed)

# Ping command
@client.command(aliases=['speed'])
async def ping(ctx):
    await ctx.send(f"your ping is: {round(client.latency * 1000)}ms")

# Error handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please choose a difficulty mode")

# Start quiz command
@client.command()
async def start(ctx, mode : int):
    await ctx.send("A quiz has been **started** !")
    await ctx.send(f"Type your guess within {mode} seconds")
    # await ctx.send(file = discord.File(f"{main.target_path}"))

# Reading a message
@client.event
async def on_message(message):
    channel = message.channel
    # if message.content == "smitesh":
    #     await channel.send("Correct! 5 points to griffindor")
    await client.process_commands(message) # This line is needed for commands to work in conjuction with on_message events

client.run(os.getenv('BOT_TOKEN'))