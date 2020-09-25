from discord.ext import commands
import discord
import json
from HTTPrequest import Request
import discordbot
from DBmanager import DBManager

class CommandCog(commands.Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
    
    @commands.command()
    async def get(self,ctx):
        """ APIを叩いた結果をJSON形式で表示する。デフォルトは＠Ltoさんのコミュニティ """
        await ctx.send(Request())
    
    @commands.command()
    async def add(self,id,name,ctx):
        #サーバー名からserversテーブルのIDを取得する

        self.bot.get_id(ctx.guild.name)

        discordbot.db.execute("INSERT INTO communities (server_id, communitiy_id,community_name) VALUES ({0},{1},{2});".format(1,id,name))
        await ctx.send("ID:" + id + ", NAME:" + name + "で登録しました")

    @commands.command()
    async def reload(self,ctx):
        """ 情報をリロードする。 """
        with open(discordbot.path) as f:
            l = str(f.read())
            key = l[:l.find(":")]
            value = l[l.find(":")+1:]

            discordbot.communities.update(key=value)
    
        await ctx.send("リロード完了しました")

class SimpleHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = "コマンド："
        self.no_category = "その他"
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

    def get_ending_note(self):
        return (f"各コマンドの説明: -help <コマンド名> \n"
                f"各カテゴリの説明: -help <カテゴリ名> \n")


def setup(bot):
    bot.add_cog(CommandCog(bot))