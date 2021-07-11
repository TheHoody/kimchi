import discord
import asyncio

client = discord.Client()

token = "ODYzNzc5MDYwMDI5ODQ5NjEx.YOr28A.B2BpGVoAxQIsidvWc3QPQ06vovc"

@client.event
async def on_ready():

    print(client.user.name)
    print('봇이 성공적으로 시작되었습니다.')
    game = discord.Game('형진이 전용 재떨이')
    await client.change_presence(status=discord.Status.online, activity=game)

client.run(token)