import discord
from discord.ext import commands

token = "NzkzNzA5MDQ5NTg1MjA1MjY5"

bot = commands.Bot(command_prefix = "123456789")

print('What would you like to stream?')
status = input('purple status color haha')

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = status,
        url = 'https://www.twitch.tv/twitch'
    )
    print('Streaming: ' + status)
    await bot.change_presence(activity=stream)

bot.run(token, bot=False)    
