import discord
import asyncio

client = discord.Client()
secret_token = 'NDIwNzYyMzgwMjY0NTM4MTEy.DYDZbQ.eGECuc2x2Qv2uFDTgHE04J7yLfE'

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

client.run(secret_token)