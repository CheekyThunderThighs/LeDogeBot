# Work with Python 3.6
import discord

TOKEN = 'NTQwNzc0Njc2MzE4NzgxNDQw.Dzamew.4vxM8ovW3k49noJ2b77Nb87X9SA'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Simple hello to the user
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention} please help me I am stuck in this code and I cannot escape'.format(message)
        await client.send_message(message.channel, msg)
    #

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)