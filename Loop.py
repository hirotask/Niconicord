from discord.ext import tasks,commands
import discord
from discord import Guild
from HTTPrequest import Request
import asyncio
import json
import urllib.request
import logging

class LoopCog(commands.Cog):
    def __init__(self,bot,communities):
        self.bot = bot
        self.communities = communities

        logging.basicConfig(level=logging.INFO)

        args = []
        
        #TODO: keysとvaluesの値がnullなのをなおす
        for key in self.communities.keys():
            args.append(urllib.parse.quote(key))

        self.keys = ",".join(args)
        self.values = ",".join(self.communities.values())
        self.fields = ["contentId","title","startTime","memberOnly"]

        self.isLive = False

        self.index = 0

        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):

        print("live=" + str(self.isLive))

        responses = {}

        print(self.index)
        self.index += 1

        print("keys:" + self.keys)
        print("values:" + self.values)
        print("fields:" + ",".join(self.fields))


        responses = Request(self.keys,self.values,self.fields).getResponse()
        #responseは辞書型{data:[{}],meta:{}}


        data_list = responses["data"] #List
        meta_dict = responses["meta"] #Dict


        #放送が行われていなかった場合
        if meta_dict["totalCount"] <= 0:
            print("passed")
            self.isLive = False
            return

        #行われていた場合
        for data in data_list:      
            #if data_dict["contentId"] == nowContent:
            #    return
                                        
            link = "https://live2.nicovideo.jp/watch/"


            if self.bot.is_ready():

                channel = self.bot.get_channel(736844332233130010)

                if self.isLive == True:
                    return

                if data["memberOnly"] == True :
                    await channel.send("生放送が " + link + data["contentId"] + " でコミュニティ限定で行われています")
                else:
                    await channel.send("生放送が " + link + data["contentId"] + " で行われています")

                self.isLive = True

            else:
                print("not ready")
    
    @printer.before_loop
    async def before_printer(self):
        print("wainting...")
        await self.bot.wait_until_ready()

def setup(bot ,communities):
    bot.add_cog(LoopCog(bot,communities))