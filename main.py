import discord
from discord.ext import commands
import os
import asyncio


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('\n')
    print('BUTL-R is online and ready to use.')
    print('\n')

initial_extensions = []

async def load(bot):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load(bot)
    await bot.start("TOKEN")
   
asyncio.run(main())

