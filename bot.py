from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.command(name="hi")
async def hi(ctx):
    await ctx.send("hello")

bot.run("Njc5ODYwNzgxOTUyNzk0NjQ2.XoZSUg.pb_WsuYSS810czto-9oMlPohvWw")
