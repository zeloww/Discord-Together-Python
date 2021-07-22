import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
intents.members = True

with open('config.json') as f:
    data = json.load(f)
    prefix = data["BOT_PREFIX"]
    activity = data["ACTIVITY"]

bot = commands.Bot(
    command_prefix=prefix,
    description="Bot by Zelow#9999",
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=activity)
    )
    print("Successful ! You are login with : {0.user}".format(bot))
    print(f"In {len(bot.guilds)} guilds")
    print(f"On {len(bot.users)} users")

@bot.command(aliases=['git'])
async def github(ctx):
    embed=discord.Embed(title='GitHub', description='[Click Here](https://github.com/zeloww)', color=discord.Color.purple())
    
    await ctx.send(embed=embed)

bot.load_extension("cogs.discordtogether")
bot.run(TOKEN)
