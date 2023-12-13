import discord
from discord.ext import commands
import os 
import sys
from discord.ext.commands import has_permissions


class Roles(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command() # detector
    @commands.has_role("TCS")
    async def Roles_test(self, ctx):
        await ctx.send('Role_test command works!')
        print('Role tester command triggered.')

    @commands.Cog.listener() # on member join
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, id=1174397521536229467)
        print(f"{member} has joined the server.")
        await channel.send(f"{member} has joined the server.")


#setup du cog
async def setup(bot):
    await bot.add_cog(Roles(bot))
    print("Roles cog loaded successfully")