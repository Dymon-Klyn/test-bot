import os
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.command(name="hi")
async def hi(ctx):
    await ctx.send("hello")

bot.run(TOKEN)
