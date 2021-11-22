import os
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv 
import main

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

    -> `aq help` : displays available commands
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
    global fetched_anime
    await ctx.send("A quiz has been **started** !")

    # Generating random anime & link and then downloading it
    fetched_anime = main.anime_fetch(1)
    main.op_download(list(fetched_anime.values())[0])

    await ctx.send(file = discord.File(f"{main.target_path}")) # sending the video

    # Deleting residual files
    main.clean_folder()

    await ctx.send(f"You have {mode} seconds")
    await ctx.send("Type your guesses below")

# Reading a message
@client.event
async def on_message(message):
    global fetched_anime
    if message.author.bot and message.content == "Type your guesses below":
        bot_channel = message.channel
        # timeout variable can be omitted, if you use specific value in the while condition
        timeout = 600   # [seconds]

        timeout_start = time.time()

        while time.time() < timeout_start + timeout:
            if message.content in list(fetched_anime.keys())[0].split():
                print("correct")
    await client.process_commands(message) # This line is needed for commands to work in conjuction with on_message events
 
client.run(os.getenv('BOT_TOKEN'))