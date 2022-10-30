import discord, os, requests 
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) 

def configure():
    load_dotenv()

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
    configure()
    surah, ayah = ayah_identifier.split(":")
    url = f"http://api.globalquran.com/ayah/{surah}:{ayah}/en.sahih?key={os.getenv('api_key')}"
    r = requests.get(url)
    quran_dict = r.json()
    while len(quran_dict) == 1:
            quran_dict = quran_dict[next(iter(quran_dict))]
    if int(quran_dict["surah"]) == int(surah):
        await ctx.send(f"{quran_dict['verse']}")
    else:
        await ctx.send(f"Invalid Ayah number for this Surah.")

bot.run("Bot Token")