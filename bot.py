import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents().default()
intents.members = True

client = commands.Bot(command_prefix="-", intents=intents)


@client.event
async def on_ready():
    print("I'm in, bitch")


def role_check(user):
    for role in user.roles:
        if role.name == 'Officers':
            return True
    return False


@client.command()
# Mute everyone in same voice chat as command author
async def m(ctx):
    if role_check(ctx.author):
        vc = discord.utils.get(ctx.guild.voice_channels, id=ctx.author.voice.channel.id)
        for member in vc.members:
            if not role_check(member):
                await member.edit(mute=True)


@client.command()
# Unmute everyone on server
async def u(ctx):
    if role_check(ctx.author):
        for voice_channel in ctx.guild.voice_channels:
            vc = discord.utils.get(ctx.guild.voice_channels, id=voice_channel.id)
            for member in vc.members:
                await member.edit(mute=False)

client.run(TOKEN)

