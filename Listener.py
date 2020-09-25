from discord.ext import commands
import discord
import discordbot
from HTTPrequest import Request
import Loop
import datetime
import json

class ListenerCog(commands.Cog):
    def __init__(self,bot, communities):
        self.bot = bot
        self.communities = communities
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("ログインしました。プログラム起動します。")
        Loop.setup(self.bot,self.communities)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if(member.display_name != "NicoNicord"):
            return


def setup(bot,communities):
    bot.add_cog(ListenerCog(bot,communities))