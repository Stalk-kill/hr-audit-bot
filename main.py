import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

with open('config.json') as f:
    config = json.load(f)

GUILD_ID = 1393233487850373334  # ID твоего сервера

@bot.event
async def on_ready():
    print("Bot ready!")
    bot.audit_channel = bot.get_channel(int(config['audit_channel_id']))

@bot.event
async def on_member_join(member):
    # HR AUDIT — только наш сервер
    if member.guild.id != GUILD_ID:
        return

    if bot.audit_channel is None:
        return

    e = discord.Embed(
        title="👤 Присоединился",
        color=0x00ff00
    )
    e.add_field(name="User", value=member.mention, inline=False)
    e.add_field(name="ID", value=member.id, inline=False)

    await bot.audit_channel.send(embed=e)

@bot.event
async def on_member_remove(member):
    # HR AUDIT — только наш сервер
    if member.guild.id != GUILD_ID:
        return

    if bot.audit_channel is None:
        return

    e = discord.Embed(
        title="👤 Ушёл",
        color=0xff0000
    )
    e.add_field(name="User", value=member.name, inline=False)
    e.add_field(name="ID", value=member.id, inline=False)

    await bot.audit_channel.send(embed=e)

bot.run(config['token'])
