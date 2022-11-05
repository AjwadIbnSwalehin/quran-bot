import discord, os, requests, quranInfo
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) 

def configure():
    load_dotenv()

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game("Aiming to Please Allah!"))
    await bot.tree.sync(guild=None) # Change the "None" to a specific guild ID as global syncing takes long, if the bot is in multiple servers
    print(f"We have logged in as Qur'an Bot!")

# TO DO: 
# 1) Add Buttons to the Bots

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

    ayahembed = discord.Embed(
        colour = discord.Colour.blue()
    )

    ayahembed.set_author(name = f"{quranInfo.quranInfoList['surah'][int(surah)][1]}, {quranInfo.quranInfoList['surah'][int(surah)][2]}", icon_url = "https://images.unsplash.com/photo-1609599006353-e629aaabfeae?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aG9seSUyMHF1cmFufGVufDB8fDB8fA%3D%3D&w=1000&q=80")
    ayahembed.add_field(name = f"{ayah_identifier}", value = f"{quran_dict['verse']}")

    if int(quran_dict["surah"]) == int(surah):
        await ctx.send(embed=ayahembed)
    else:
        await ctx.send(f"Invalid Ayah number for this Surah.")

@bot.command()
async def arabic(ctx, arabicayah):
    configure()

    asurah, aayah = arabicayah.split(":")
    url = f"http://api.globalquran.com/ayah/{asurah}:{aayah}/quran-simple?key={os.getenv('api_key')}"
    r = requests.get(url)
    arabic_quran_dict = r.json()

    while len(arabic_quran_dict) == 1:
        arabic_quran_dict = arabic_quran_dict[next(iter(arabic_quran_dict))]

    if int(asurah) < 1 or int(asurah) > 114:
        await ctx.send("Invalid Surah Number")

    arabicembed = discord.Embed(
        colour = discord.Colour.blue()
    )

    arabicembed.set_author(name = f"{quranInfo.quranInfoList['surah'][int(asurah)][0]}", icon_url = "https://images.unsplash.com/photo-1609599006353-e629aaabfeae?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aG9seSUyMHF1cmFufGVufDB8fDB8fA%3D%3D&w=1000&q=80")
    arabicembed.add_field(name = f"{arabicayah}", value = f"{arabic_quran_dict['verse']}")

    if int(arabic_quran_dict["surah"]) == int(asurah):
        await ctx.send(embed=arabicembed)
    else:
        await ctx.send(f"Invalid Ayah number for this Surah.")

bot.run("Bot Token")