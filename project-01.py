import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():

    print(client.user.name)
    print('봇이 성공적으로 시작되었습니다.')
    game = discord.Game('형진이 전용 재떨이')
    await client.change_presence(status=discord.Status.online, activity=game)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

