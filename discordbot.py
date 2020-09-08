import discord
from discord.ext import commands
import re
import traceback
import Listener
import Command
from HelpCommand import SimpleHelpCommand

TOKEN = "NzM2NTcwMzgzODM0MTUzMDAy.XxwuoA.uAvK2vbJuC64qtS0yFseTRbRrcQ"

communities = {}

path ="communities.txt"

class MainBot(commands.Bot):
    def __init__(self,command_prefix,help_command):
        super().__init__(command_prefix,help_command)

        #コミュニティの読み込み
        with open(path) as f:
            l = [s.strip() for s in f.readlines()]

            for arg in l:
                _key = arg[:arg.find(":")]
                _value = arg[arg.find(":")+1:]

                communities[_key] = _value

        print(communities)

    def get_channel(self,channel):
        return super().get_channel(channel)

if __name__ == "__main__":
    bot = MainBot(command_prefix="-", help_command=SimpleHelpCommand())
    Listener.setup(bot,communities)
    Command.setup(bot)
    bot.run(TOKEN)
