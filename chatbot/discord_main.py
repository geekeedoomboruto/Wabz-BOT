from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from random import choice
import random
from time import sleep
import os
import sys
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import time
from time import ctime
import asyncio
from googletrans import Translator
from langdetect import detect
translator = Translator()
bot=ChatBot('Test')
random_bye=["You are a good, person, bye!","Really man, i want to talk with you","If you say it, i have to do it!","I'm a bot, and i approuve this message!","Ok","But... But... I am so sad...","Bye you are my best friend"]
Client=discord.Client()
client=commands.Bot(command_prefix="!")
bot=ChatBot('Test')
random_bye=["You are a good, person, bye!","Really man, i want to talk with you","If you say it, i have to do it!","I'm a bot, and i approuve this message!","Ok","But... But... I am so sad...","Bye you are my best friend"]
bot.set_trainer(ListTrainer)
for _file in os.listdir('files'):
    chats=open('files/'+_file,'r').readlines()
    bot.train(chats)
@client.event
async def on_ready():
    print("Wabz is connected to all servers!")
@client.event
async def on_message(message):
    translate=(message.content).split()
    if translate[0]=="!lang":
        try:
            sentence=""
            i=1
            while i<len(translate)-1:
                sentence=sentence+translate[i]+" "
                i+=1
            lang=detect(sentence)
            await client.send_message(message.channel,lang)
        except:
            await client.send_message(message.channel,"Je n'ai pas pu traduire")
    elif not message.author.bot and not translate[0]=="!translate" and translate[0]=="!parle":
            sentence=""
            i=1
            while i<len(translate)-1:
                sentence=sentence+translate[i]+" "
                i+=1
        response=bot.get_response(sentence)
        print(message," ",message.content)
        await client.send_message(message.channel,response)
while True:
    client.run(os.getenv('TOKEN'))
