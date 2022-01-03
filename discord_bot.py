import discord
import os
# allows us to get quotes from website
import requests
import json
import math

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  # q represents quote a represents author
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  # all function names and command specific to discord
  # IF BOT SENSES A MESSAGE 
@client.event
async def on_message(message):
    if message.author == client.user:
      return 

    if message.content.startswith("$commands"):
      await message.channel.send('1.greet bot -- $hello, $hey, etc | 2. conversation -- $how are you, $I am good, etc | 3. $nspire -- for quotes -- not quite done yet | 4. gifs -- $mathgif, $my day was good, $are you ignoring me')


    if (message.content.startswith("$hello")) or (message.content.startswith("$HEYYYYYYYYYY")) or (message.content.startswith("$Hey")) or (message.content.startswith ("$Hello")) or (message.content.startswith ("$hey")):

      await message.channel.send('Hello!')

    if message.content.startswith("$how are you"):
      await message.channel.send('Im great, you?')

    if message.content.startswith("$I am good"):
      await message.channel.send('ah thats great, how was your day?')
    
    if message.content.startswith("$I need motivation"):
      await message.channel.send('“Inspiration does exist, but it must find you working.” ')

    if message.content.startswith("$math help"):
      await message.channel.send('https://www.mathway.com/ or ask abrar')

    if message.content.startswith("$inspire"):
      quote = get_quote
      await message.channel.send(quote)

    if message.content.startswith("$mathgif"):
      await message.channel.send("https://media.giphy.com/media/xT1Ra5h24Eliux3UVq/giphy.gif")

    if message.content.startswith("$my day was good"):
      await message.channel.send("https://media.giphy.com/media/fB1pQq6hlqnpyfETbk/giphy.gif")

    if message.content.startswith("$are you ignoring me?"):
      await message.channel.send("https://media.giphy.com/media/DKLkMrA40apwI/giphy.gif")
# calculations basic and celcius to fahrenheit converter
    n = 27
    if message.content.startswith('$Square root'):
      await message.channel.send(math.sqrt(int(n)))



client.run(os.getenv('TOKEN'))
