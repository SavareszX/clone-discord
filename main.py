
from os import system
import psutil
from pypresence import Presence
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone
from colorama import Fore, Back, Style, init
init()
def colorprint(str1, str2):
    print(getattr(Fore, str2) + str1 + Fore.WHITE)
colorprint("words", "GREEN")

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.GREEN}

                           ╔╗
╔══╦══╦╗╔╦══╦═╦══╦══╦═══╦══╣║╔══╦═╗╔══╗
║══╣╔╗║╚╝║╔╗║╔╣║═╣══╬══║║╔═╣║║╔╗║╔╗╣║═╣
╠══║╔╗╠╗╔╣╔╗║║║║═╬══║║══╣╚═╣╚╣╚╝║║║║║═╣
╚══╩╝╚╝╚╝╚╝╚╩╝╚══╩══╩═══╩══╩═╩══╩╝╚╩══╝

                                                            {Fore.MAGENTA}{Style.RESET_ALL}
        """)
token = input('Please enter your token >> ')
guild_s = input('Please enter guild id you want to copy >> ')
guild = input('Please enter guild id you want to place >> ')
input_guild_id = guild_s  # <-- ใส่ guild id ที่จะก็อป        #ใส่ในconsoleได้
output_guild_id = guild  # <-- ใส่ guild id ที่จะวาง          #ใส่ในconsoleได้
token = token  # <-- ใส่ Token                              #ใส่ในconsoleได้


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}
                                            ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                            ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                            ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                            ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                            ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                            ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░
    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)