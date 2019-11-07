import discord
import asyncio
import os
import json
import random

client = discord.Client()

try:  
   os.environ["discord_bot_token"]
except KeyError: 
   print ("Please set the environment variable discord_bot_token")
   sys.exit(1)

print(os.environ["discord_bot_token"])
secret_token = (os.environ["discord_bot_token"])


def get_random_quote():
   with open('quotes.json','r') as quotes:
      bobbyb_quotes = json.load(quotes)
   return random.choice(bobbyb_quotes)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
   channel = message.channel
   if message.content.startswith('!ping'):
      await channel.send( 'Pong!')
   if message.content.startswith('!ding'):
      await channel.send( 'Dong, motha fucka!')
   ### The magic
   if message.content.startswith('bobbyb'):
      msg = get_random_quote().format(message) 
#      msg = "THANK THE GODS FOR BESSIE AND HER TITS"
      await channel.send(msg)

client.run(secret_token)