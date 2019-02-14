import discord, sys, requests, os
from random import randint

client = discord.Client()

token = os.environ.get("DISCORD_TOKEN")
my_key = os.environ.get("GIPHY_KEY")

# token = open("token.txt", "r").read()

# my_key = open("key.txt", "r").read()

def community_report(guild):
    online = 0
    offline = 0
    idle = 0

    for m in guild.members:
        if str(m.status) == "online":
            online+=1
        if str(m.status) == "offline":
            offline+=1
        else:
            idle+=1
    return online, offline, idle

# def pubg(ign):
#     ign = message.content[6:]
#     await message.channel.send("https://pubg.op.gg/user/"+ign+"?server=na")

@client.event # event decorator/wrapper 
async def on_ready():
    print(f"We have logged in as {client.user}")
    print("Discord Version: {}".format(discord.__version__))

@client.event
async def on_message(message):

    print(f"{message.channel}: {message.author}: {message.author.name}: \n{message.content}")

    # access discord server/guild information
    
    guild = client.get_guild(323164582422249473)

    if message.content.startswith("!commands"):
        await message.channel.send("Possible Commands:\n!community - shows online/offline/idle members in server\n"+
                                    "!deathstare - kobe\n!pubg - search pubg id on pubg.op.gg.\n     for example, !pubg pythonjavac\n"+
                                    "!gifme- gets a random gif from giphy.com based on user's search term.\n     for example, !gifme lakers\n")

    elif message.content.startswith("!deathstare"):
        file = discord.File("C:\\Users\\James\\Desktop\\discordbot\\media\\1.jpg", filename="C:\\Users\\James\\Desktop\\discordbot\\media\\1.jpg")
        await message.channel.send("charmin' soft", file=file)


    elif message.content.startswith("!community"):
        online, idle, offline = community_report(guild)
        await message.channel.send(f"Online: {online}\nOffline: {offline}\nIdle: {idle}")

    elif message.content.startswith("!pubg"):
        ign = message.content[6:]
        await message.channel.send("https://pubg.op.gg/user/"+ign+"?server=na")


    elif message.content.startswith("!gifme"):
        await message.channel.send("fetching a random gif from the gif machine...")
        tag = message.content[7:]

        if len(tag) == 0:
        
            
            r = requests.get("http://api.giphy.com/v1/gifs/search?q=spongebob&api_key="+my_key+"&limit=1000")
            data_r = r.json()
            randomint = randint(0,1000)
            gif_url = data_r['data'][randomint]['url']
            await message.channel.send("oh you want spongebob eh?")
            await message.channel.send(gif_url)
        

        elif(tag):
            
            r = requests.get("http://api.giphy.com/v1/gifs/search?q="+tag+"&api_key="+my_key+"&limit=1000")
            data_r = r.json()
            randomint = randint(0,1000)
            gif_url = data_r['data'][randomint]['url']
            await message.channel.send(gif_url)

    elif message.content.startswith("!logout"):
        await client.close()


client.run(token)