import discord
from requests import get
import asyncio
from os import environ
TOKEN = environ.get("benswoloToken")

s = """Soulja Boy off in this oh Watch me crank it,
watch me roll Watch me crank dat, Soulja Boy Then
Superman dat oh Now watch me you (Crank dat, Soulja
Boy) Now watch me you (Crank dat, Soulja Boy) """
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name='Team Fortress 3'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "soulja boy" in message.content.lower():
        await message.channel.send(s, tts=True)
    if message.content.lower() == ".sw":
        resp = get("http://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote").json()["starWarsQuote"]
        await message.channel.send(resp)
    if "can i take your order" in message.content.lower():
        await message.channel.send("I'll have two number 9's, a number 9 large, a number 6 with extra dip, a number 7, two number 45's, one with cheese, and a large soda.", tts=True)
    if "99792492710330368" in message.content.lower():
        await message.channel.send("🚨 <@99792492710330368> 🚨\nSomeone used your id!")
    if message.content.lower() == ".aaa":
        # grab the user who sent the command
        voice_channel=message.author.voice.channel
        # only play music if user is in a voice channel
        if voice_channel != None:
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio('aaa.mp3'), after=lambda e: print('done', e))
            while vc.is_playing():
                await asyncio.sleep(1)
            await vc.disconnect()

        else:
            await message.channel.send('Get in a voice channel, dumbass.')


client.run(TOKEN)
