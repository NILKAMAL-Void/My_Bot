import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print("------")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    if not channel:
        channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}! 👋")

# --- ADD THIS EVENT TO FIX !PING ---
@bot.event
async def on_message(message):
    # This line forces the bot to check for commands like !ping
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

bot.run('MTUyMDgxMzUxOTAzMTc2Mjk2NA.G1_VN1.9iJzgkOwv2Ei6l5oS0uvF2XBBk2vbeiLYx_hbQ')
  
