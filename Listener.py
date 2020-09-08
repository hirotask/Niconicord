from discord.ext import commands
import discord
from HTTPrequest import Request
import loop

class ListenerCog(commands.Cog):
    def __init__(self,bot, communities):
        self.bot = bot
        self.communities = communities
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("ログインしました。プログラム起動します。")
        loop.setup(self.bot,self.communities)


def setup(bot,communities):
    bot.add_cog(ListenerCog(bot,communities))