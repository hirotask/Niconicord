from discord.ext import tasks,commands
from HTTPrequest import Request
import asyncio
import json
import urllib.request

class MyCog(commands.Cog):
    def __init__(self,communities):
        self.communities = communities
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

    def sendAlert(self,data_dict):
        link = "https://live2.nicovideo.jp/watch/"
        
        if data_dict["memberOnly"] == True:
            print("生放送が" + link + data_dict["contentId"] + "でコミュニティ限定で行われています")
        else:
            print("生放送が" + link + data_dict["contentId"] + "で行われています")

    @tasks.loop(seconds=5.0)
    async def looper(self):
        nowContent = ""

        responses = {}

        print(self.index)
        self.index += 1

        print("{0}:{1}".format(self.keys,self.values))
        responses = Request(self.keys,self.values,self.fields).getResponse()
        #responseは辞書型{data:[{}],meta:{}}


        data_list = responses["data"] #List
        meta_dict = responses["meta"] #Dict

        for data in data_list:
            for data_dict in data:
                if meta_dict["totalCount"] <= 0:
                    return
                    
                if data_dict["contentId"] == nowContent:
                    return
                                        
                self.sendAlert(data_dict)
                nowContent = data_dict["contentId"]

            
            
