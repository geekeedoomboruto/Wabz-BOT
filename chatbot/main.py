from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from random import choice
import random
from time import sleep
import os
import sys
import asyncio
import time
bot=ChatBot('Test')
random_bye=["You are a good, person, bye!","Really man, i want to talk with you","If you say it, i have to do it!","I'm a bot, and i approuve this message!","Ok","But... But... I am so sad...","Bye you are my best friend"]
def unclone(list):
    return list
def chat_begin(botname):
    for _file in os.listdir('files'):
        chats=open('files/'+_file,'r').readlines()
        chats=unclone(chats)
        bot.set_trainer(ListTrainer)
        bot.train(chats)
    if "harry potter and the goblet of fire\n" in chats:
        chats.remove("harry potter and the goblet of fire\n")
    if "which movie do you like\n" in chats:
        chats.remove("which movie do you like\n")
    if "etes vous stupide\n" in chats:
        chats.remove("etes vous stupide\n")
    if "Are you crazy?\n" in chats:
        chats.remove("Are you crazy?\n")
    if "yes you are\n" in chats:
        chats.remove("yes you are\n")
    if "bye\n" in chats:
        chats.remove("bye\n")
    if "elle etait cool\n" in chats:
        chats.remove("elle etait cool\n")
    if "Vous savez tout\n" in chats:
        chats.remove("Vous savez tout\n")
    for i in range(0,len(chats)-1):
        if chats[i]=="which movie do you like\n":
            chats[i]="because it is like that!!!!"
        if chats[i]=="what the f\n":
            chats[i]="........................ftrfgferhgvfdcvfgrthygtfvrvgthy6!!!!"
    chats.append("You are so good\n")
    for _file in os.listdir('files'):
        bot.train(chats)
    while True:
        print("Dis un truc")
        request = input("You: ")
        if request=='bye':
            print(botname,": ",choice(random_bye))
            break
        response=te=bot.get_response(request)
        if te=="Vous savez tout":
            response="Ma limite est tendue"
        if te=="yes you are":
            response="dsl, je ne comprend pas tres bien"
        if te=="harry potter and the goblet of fire":
            response="I don't understand, sorry"
        if te=="elle etait cool":
            response="comment ca va"
        if te=="because you say you are stupid":
            response="A euh, je voulais ecrire quoi!"
        if te=="good!":
            response="Bien!"
        if te=="how are you?":
            response="comment vas tu"
        if te=="you are stupid" or te=="you are crazy" or te=="you know nothing" or te=="Are you crazy?":
            response="Oh, merci"
        if te=="no":
            response="oui"
        print(botname,": ",response)
def play():
    def simulator(name,simulation_username):
        print(name,simulation_username)
        connect_choice=["connected","unconnected"]
        connect=random.choice(connect_choice)
        if connect=="connected":
            name="@"+name
            print(name,",",simulation_username," is connected")
            return chat_begin(simulation_username)
        else:
            sleep(0.8)
            n=name
            print("@",name," We will try to find another person because ",simulation_username,"is not connected!")
            return interface(n)
    def interface(n):
        if not n==1:
            letters=["a","b","c","d","e","f","g","h","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            numbers=["0","1","2","3","4","5","6","7","8","9"]
            #ok so i put it from another program i made, now we have to randomize the position of these values
            random.shuffle(letters)
            random.shuffle(numbers)
            #ok, now we have shuffle all that, we have to add all that to a sting who will be the random username
            #it has to be like its real
            random_letters=random.randint(3,8)
            #3 to 8 letters, it is ok
            random_numbers=random.randint(0,4)
            #i think the most of username have between 0 to 4 numbers
            random_user=""
            #now i will add all of these things
            i=0
            while i<random_letters:
                random_user+=letters[i]
                i+=1
            i=0
            while i<random_numbers:
                random_user+=numbers[i]
                i+=1
            print(random_user)
            return simulator(n,random_user)
        else:
            letters=["a","b","c","d","e","f","g","h","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            numbers=["0","1","2","3","4","5","6","7","8","9"]
            #ok so i put it from another program i made, now we have to randomize the position of these values
            random.shuffle(letters)
            random.shuffle(numbers)
            #ok, now we have shuffle all that, we have to add all that to a sting who will be the random username
            #it has to be like its real
            random_letters=random.randint(3,8)
            #3 to 8 letters, it is ok
            random_numbers=random.randint(0,4)
            #i think the most of username have between 0 to 4 numbers
            random_user=""
            #now i will add all of these things
            i=0
            while i<random_letters:
                random_user+=letters[i]
                i+=1
            i=0
            while i<random_numbers:
                random_user+=numbers[i]
                i+=1
            user_ask="The username is: "+input("Write your username: ")
            user_ask=user_ask.split()
            user_ask.append("anonyme")
            user=user_ask[3]
            print(random_user)
            return simulator(user,random_user)
    return interface(1)
#so #if the user is not connected, it will regenerate another username but it will not ask your username
    #else, it will do all the stuff and ask your username
