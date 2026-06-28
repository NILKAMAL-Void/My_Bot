import discord
from discord.ext import commands

# Set up the bot with a command prefix
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # CRITICAL: This allows the bot to detect when people join!
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("------")

# Welcome message event
@bot.event
async def on_member_join(member):
    # This searches for a text channel named 'welcome' or 'general' in your server
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    if not channel:
        channel = discord.utils.get(member.guild.text_channels, name="general")
    
    # If the bot finds a channel, it sends the message
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}! Glad to have you here. 👋")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Run the bot
bot.run('MTUyMDgxMzUxOTAzMTc2Mjk2NA.GFr1Rq.Hhasl6G9csQqeaahMtRMK2sY9Gxmx25HNE6iWw')
