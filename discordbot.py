import discord
from discord.ext import commands
import loop
from HTTPrequest import Request
import re

TOKEN = "NzM2NTcwMzgzODM0MTUzMDAy.XxwuoA.uAvK2vbJuC64qtS0yFseTRbRrcQ"

bot = commands.Bot(command_prefix="-")

communities = {}

path = "communities.txt"


@bot.event
async def on_ready():
    print("ログインしました。プログラム起動します。")

    #コミュニティの読み込み
    with open(path) as f:
        l = [s.strip() for s in f.readlines()]

        for arg in l:
            _key = arg[:arg.find(":")]
            _value = arg[arg.find(":")+1:]

            communities[_key] = _value

    print(communities)

    loop.MyCog(communities)
        

@bot.command()
async def get(ctx):
    await ctx.send(Request().getResponse())

@bot.command()
async def info(ctx,id,name):
    with open(path,mode="a") as f:
        f.write("{0}:{1}\n".format(id,name))

    await ctx.send("コミュニティを追加しました")

@bot.command()
async def reload(ctx):
    with open(path) as f:
        l = str(f.read())
        key = l[:l.find(":")]
        value = l[l.find(":")+1:]

        communities.update(key=value)
    
    await ctx.send("リロード完了しました")



bot.run(TOKEN)