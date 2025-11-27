import discord, random
from discord.ext import commands, tasks
from Angel.pan import analize_THIS
from ia_detect_animal.pan import Que_animal_seraaa
from codigoGPT import *
import game.game as game_module
from game.game import dou_exist
import io, asyncio
from detectar_voz import speech_from_audio_file
from voz_Ia import texto_ia
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
async def Voz_Ai(ctx, que_dijo="El chistosito que llamo este comando y me desperdicio un token de gemini no puso nada."):
    who_this = ctx.author
    try:
        await texto_ia(responde_gemini(str(que_dijo), str(who_this)))
        with open('audio/audio.mp3', 'rb') as f:
            audio = discord.File(f)
        await ctx.send(file=audio)
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
        if game_module.hunger>=0 and game_module.thirst>=0:
            await ctx.send(f"Hambre:{100-game_module.hunger} \n Sed:{100-game_module.thirst}, \n Diverticion:{game_module.fun}, \n Sueño:{100-game_module.not_tired}")
        else:
            await ctx.send("se te murio")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.attachments:
        archivo = message.attachments[0]
        es_audio = False
        if archivo.content_type and archivo.content_type.startswith("audio"):
            es_audio = True

        if es_audio:
            print(f"🎵 Audio detectado de {message.author}: {archivo.filename}")

            async with message.channel.typing():
                await archivo.save(archivo.filename)

                texto_transcrito = await bot.loop.run_in_executor(None, speech_from_audio_file, archivo.filename)
                if texto_transcrito:
                    await message.reply(f"👂 **Escuché:** \"{texto_transcrito}\"")

                    respuesta = responde_gemini(texto_transcrito, str(message.author))
                    await message.reply(respuesta)
                else:
                    await message.reply("No se te entiende nada. Habla bien 🔇")
    await bot.process_commands(message)

@bot.command()
async def revive_el_server(ctx, amount=100):
    await ctx.send("ok")
    for i in range(amount):
        await ctx.send("@everyone")
@bot.command()
async def necesitamos_tu_opinion(ctx, que=""):
    ctx.send(f"{random.choice(["si", "no", "talvez"])}, {que}")
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