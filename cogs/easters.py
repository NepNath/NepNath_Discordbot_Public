import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import os 
import sys

__all__ = ["has_permissions", "MissingPermissions", "os", "sys"]


class easters(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def easter_test(self, ctx):
        await ctx.send("Easter_Test command works!")

    @commands.Cog.listener() # message  de motivation #buggé
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        role = discord.utils.get(message.author.roles, name="TCS")
        emote = discord.utils.get(message.guild.emojis, name="LTG")
        if 'kys' in message.content or "Kys" in message.content or "Kill yourself" in message.content or "kill yourself" in message.content and role.name == "TCS":
            print('ltg easter triggered')
            motivational_speech = ("You are a worthless, bitch ass nigga. Your life literally is as valuable as a summer ant. I'm just gonna stomp you and you're gonna keep coming back, imma seal up all my cracks, you're gonna keep coming back. Why? Cause you smellin the syrup. You worthless bitch ass nigga.\nYou gonna stay on my dick until you die. You serve no purpose in life. Your purpose in life is to be on my stream sucking on my dick daily. Your purpose in life is to be in that chat blowing the dick daily.\nYour life is nothing, you serve zero purpose.\nYou should kill yourself, **NOW**.")
            await message.channel.send(f"{motivational_speech} {emote}")
            print("someone needs to be motivated : ", message)
        elif "femme" in message.content and message.author.id == 311872623896166400: 
            await message.channel.send(f"Alfred on sait que t'aime les hommes ça sert a rien de mytho")
        

    @commands.command() #alfred meme tg
    async def alfdtg(self, ctx):
        print("Alfred Tg message triggered")
        emote = discord.utils.get(ctx.guild.emojis, name="LTG")
        message = "Alfted ta avec ton meme de qui a aucun sens avec la discution"
        if ctx.author.id == 311872623896166400 or ctx.author.id == 240797449529196545: 
            await ctx.send(f"{message} {emote} ")
    
    @commands.command()
    async def fard(self, ctx, member : discord.Member, *, reason=None):
        if ctx.author.id == 954286734416429126:
            emote = discord.utils.get(ctx.guild.emojis, name="LTG")
            try:
                await member.kick(reason=reason)
                await ctx.send(f'{member} has been kicked. {emote}')
            except discord.Forbidden:
                await ctx.send("Je n'ai pas la permission de Kick ce membre.")
                print("Kick commmand triggered, however, the bot does not have the permission to kick the member.")
            except discord.HTTPException:
                await ctx.send("Une erreure s'est produite lors de l'exclusion du membre.")
                print("Kick command triggered, however, an error occured while kicking the member.")
        elif ctx.author.id == 311872623896166400:
            await ctx.send("trigger")
        

#setup du cog
async def setup(bot):
    await bot.add_cog(easters(bot))
    print("Easters cog loaded successfully")  # add this line to check if the cog is being loaded correctly
