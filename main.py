import discord, asyncio, datetime, pygq
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) 

Q = pygq.PyGQ()

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game("Aiming to Please Allah!"))
    print(f"We have logged in as Qur'an Bot!")

@bot.command()
async def sync(ctx):
    await ctx.send(f"Syncing...")
    await bot.tree.sync()
    await bot.tree.sync(guild = discord.Object(id=000000000000000000000000))
    await ctx.send(f"Syncing Complete!")

@bot.command()
async def ayah(ctx, ayah_identifier):
    surah, verse = ayah_identifier.split(":") 
    await ctx.send(Q.getAyah(int(surah), int(verse), "en.sahih")["verse"])
    if pygq.invalid_ayah == True:
        ctx.send("Invalid Ayah!")


bot.run("MTAzMTY3MjA3MzI5MjA5NTUyOQ.G4VClZ.FSCO1TbvhtO1BuEEnXo9wlSkOZUy2wjhsba938")