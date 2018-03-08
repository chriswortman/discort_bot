import discord
import asyncio
import os

client = discord.Client()

try:  
   os.environ["discord_bot_token"]
except KeyError: 
   print ("Please set the environment variable discord_bot_token")
   sys.exit(1)

print(os.environ["discord_bot_token"])
secret_token = (os.environ["discord_bot_token"])

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(client.servers)


@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
       await client.send_message(message.channel, 'Pong!')
    if message.content.startswith('!ding'):
    	await client.send_message(message.channel, 'Dong, motha fucka!')

client.run(secret_token)