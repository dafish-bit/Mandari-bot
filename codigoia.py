import discord
from discord.ext import commands, tasks
from Angel.pan import analize_THIS
from ia_detect_animal.pan import Que_animal_seraaa
from codigoGPT import *
from game.game import *
import io, asyncio
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

true, false = True, False
"👍👍👍👍👍👍"

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def analiza_algo(ctx):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        
        await attachment.save(attachment.filename)
        
        await ctx.send(analize_THIS(attachment.filename))
    else:
        await ctx.send("pon una imagen D:<")

@bot.command()
async def Que_animal_sera(ctx):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        
        await attachment.save(attachment.filename)
        
        await ctx.send(Que_animal_seraaa(attachment.filename))
    else:
        await ctx.send("pon una imagen D:<")

@bot.command()
async def Pipu_ai(ctx, que_dijo="El chistosito que llamo este comando y me desperdicio un token de gemini no puso nada."):
    who_this = ctx.author
    try:
        await ctx.send(responde_gemini(str(que_dijo), str(who_this)))
    except Exception as e:
        await ctx.send(f'Ni idea. \n Solo entiendo cosas entre comillas \n Como esto: ($Pipu_ai "Hola como estas") \n a y tambien {e}')
@bot.command()
async def dou(ctx, act="nothing"):
    with io.BytesIO() as ib:
        sendable = dou_exist(act)
        sendable.save(ib, "PNG")
        ib.seek(0)
        
        discord_file = discord.File(fp=ib, filename='douuu.png')
        

        await ctx.send(file=discord_file)
        if 
        await ctx.send(f"Hambre:{100-hunger} \n Sed:{100-thirst}, \n Diverticion:{fun}, \n Sueño:{100-not_tired}")
@tasks.loop(seconds=1)
async def dou_loop():
    dou_exist()
    await asyncio.sleep(1)
#####################################
hyper_secret_token = open("../cloro.txt", 'r')
bot.run(hyper_secret_token.read())
#####################################
#hola
#chao :p