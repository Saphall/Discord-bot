import discord
import os
import requests
import json
import random
from keep_alive import keep_alive


client = discord.Client()

sad_words = ["sad", 'depressed', 'unhappy', 'exhausted',
             'bored', 'miserable', 'depressing', 'depress',
             'exhausted', 'tired', 'terrible', 'losing'
             ]

starter_motivator = [
    'Cheer Up!',
    "Hey I am here for you!",
    "You are a great person. Remember this!",
    'Think positive man! There is always a bright side!',
    'What about you watching a funny video to swing the mood?'
]


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q']+"  -"+json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower()
    if ((msg.startswith('$hello')) or (msg.startswith('$hi')) or (msg.startswith('$hey'))):
        await message.channel.send('Hello there! Nice to see you !!\nHow are you feeling?')

    if msg.startswith('$motivate'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_motivator))

    if msg.startswith('$help'):
        await message.channel.send("This is bot help.\nCommands:\n* hey, hello, hi :- Bot responds.\n* $motivate :- Generates motivating quotes.\n* $help :- Bot help.")

keep_alive()
client.run(os.environ['TOKEN'])
