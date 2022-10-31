import discord, os, requests 
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) 

def configure():
    load_dotenv()

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game("Aiming to Please Allah!"))
    await bot.tree.sync(guild=None) # Change the "None" to a specific guild ID as global syncing takes long
    print(f"We have logged in as Qur'an Bot!")

# TO DO: 
# 1) Use decomposition on code, split up incorrect Ayah and incorrect Surah into different functions
# 2) Make bot look more "fancy"

@bot.command()
async def ayah(ctx, ayah_identifier):
    configure()
    surah, ayah = ayah_identifier.split(":")
    url = f"http://api.globalquran.com/ayah/{surah}:{ayah}/en.sahih?key={os.getenv('api_key')}"
    r = requests.get(url)
    quran_dict = r.json()
    while len(quran_dict) == 1:
            quran_dict = quran_dict[next(iter(quran_dict))]
    if int(surah) < 1 or int(surah) > 114:
        await ctx.send("Invalid Surah Number")
    else:
        if int(quran_dict["surah"]) == int(surah):
            await ctx.send(f"{quran_dict['verse']}")
        else:
            await ctx.send(f"Invalid Ayah number for this Surah.")

bot.run("Bot Token")