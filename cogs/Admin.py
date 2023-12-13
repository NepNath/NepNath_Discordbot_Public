import discord
from discord.ext import commands
import os 
import sys
from discord.ext.commands import has_permissions


class Admin(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command() #active detector
    @commands.has_role(1174018403539886191)
    async def detect(self, ctx):
        await ctx.send('BUTL-R is currently active.')
        print('Detector command triggered.')


    @commands.command() #restart 
    @commands.has_role(1174018403539886191)
    async def rst(self, ctx):
        await ctx.send("Restarting...")
        os.execv(sys.executable, ['python'] + sys.argv)
        await ctx.send("Restarted.") #unreachable 
    
    @commands.command() #kick
    @commands.has_role(1174018403539886191)
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
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


    

#setup du cog
async def setup(bot):
    await bot.add_cog(Admin(bot))
    print("Admin cog loaded successfully")