from discord.ext import tasks,commands
from HTTPrequest import Request
import asyncio
import json
import urllib.request

class MyCog(commands.Cog):
    def __init__(self,communities,bot):
        self.communities = communities
        self.bot = bot

        args = []
        
        for key in self.communities.keys():
            args.append(urllib.parse.quote(key))

        self.keys = ",".join(args)
        self.values = ",".join(self.communities.values())
        self.fields = ["contentId","title","startTime","memberOnly"]

        self.index = 0

        self.looper.start()

    def cog_unload(self):
        self.looper.cancel()

    @tasks.loop(seconds=5.0)
    async def looper(self):
        nowContent = ""

        responses = {}

        print(self.index)
        self.index += 1

        responses = Request(self.keys,self.values,self.fields).getResponse()
        #responseは辞書型{data:[{}],meta:{}}


        data_list = responses["data"] #List
        meta_dict = responses["meta"] #Dict

        if meta_dict["totalCount"] <= 0:
            print("passed")
            return

        for data in data_list:      
            #if data_dict["contentId"] == nowContent:
            #    return
                                        
            link = "https://live2.nicovideo.jp/watch/"
    
            if data["memberOnly"] == True:
                await self.bot.send("生放送が" + link + data["contentId"] + "でコミュニティ限定で行われています")
            else:
                await self.bot.send("生放送が" + link + data["contentId"] + "で行われています")
            #nowContent = data_dict["contentId"]

            
            
