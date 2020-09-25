import discord
from discord.ext import commands
from DBmanager import DBManager
import re
import traceback
import Listener
import Command
import datetime
import json
import psycopg2
import os

#config.jsonの読み込み
with open("config.json") as conf:
    config = json.load(conf)

DATABASE_URL = config["url"]
db = DBManager(DATABASE_URL)

path ="communities.txt"
communities = {}

class MainBot(commands.Bot):
    def __init__(self,command_prefix,help_command):
        super().__init__(command_prefix,help_command)
    
    def set_db(self):
        server_names = []

        async for guild in self.fetch_guilds(limit=100):
            server_names.append(guild.name)


        for server_name in server_names :
            datetime_format = datetime.datetime().today()
            date = datetime_format.strftime("%Y-%m-%d %H:%M:%S")

            db.execute("INSERT INTO servers (created_at,updated_at,server_name) values ({0},{1},{2});".format(date,date,server_name))
        

if __name__ == "__main__":
    bot = MainBot(command_prefix=config["prefix"], help_command=Command.SimpleHelpCommand())
    Listener.setup(bot,communities)
    Command.setup(bot)
    bot.run(config["token"])
