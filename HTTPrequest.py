import json
import urllib.request

class Request:
    def __init__(self,communityName=urllib.parse.quote("アルト狂想曲第零章"),communityId="2576338",fields=["contentId","title","startTime","memberOnly"]):
        self.communityName = communityName
        self.communityId = communityId
        self.fields = ",".join(fields)


    def getResponse(self):
        endpoint = "https://api.search.nicovideo.jp/api/v2/live/contents/search"

        parameters = ["q=" + self.communityName,
                "targets=" + "communityText",
                "filters[communityId][0]=" + self.communityId,
                "filters[liveStatus][1]=onair",
                "fields=" + self.fields,
                "_sort=-startTime",
                "_context=apiguide"]

        url = endpoint + "?" + "&".join(parameters)

        print(url + "にアクセスします")

        req = urllib.request.Request(url)

        with urllib.request.urlopen(req) as res:
            body = json.load(res)
            print(body)
            return body

