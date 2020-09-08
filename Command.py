from discord.ext import commands
import discord
from HTTPrequest import Request
import discordbot

class CommandCog(commands.Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
    
    @commands.command()
    async def get(self,ctx):
        """ APIを叩いた結果をJSON形式で表示する。デフォルトは＠Ltoさんのコミュニティ """
        await ctx.send(Request())

    @commands.command()
    async def info(self,ctx,id,name):
        """ コミュニティの追加をする。使い方は -info コミュID コミュ名 """

        with open(discordbot.path,mode="a") as f:
            f.write("{0}:{1}\n".format(id,name))

        await ctx.send("コミュニティを追加しました")

    @commands.command()
    async def reload(self,ctx):
        """ 情報をリロードする。 """
        with open(discordbot.path) as f:
            l = str(f.read())
            key = l[:l.find(":")]
            value = l[l.find(":")+1:]

            discordbot.communities.update(key=value)
    
        await ctx.send("リロード完了しました")


def setup(bot):
    bot.add_cog(CommandCog(bot))