import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready() :
    print('BOT LIGADO COM SUCESSO')
    print(client.user.name)
    print(client.user.id)
    print('Criado por ILUFan')


@client.event
async def on_message(message):
    if message.content.lower().startswith('jv!tnt'):
        await client.send_message(message.channel, ":warning: Lá vai Bomba :warning:")
    if message.content.lower().startswith('jv!kill'):
        await client.send_message(message.channel, ":warning: Matando a Moonkase :warning:")
    if message.content.lower().startswith('jv!info'):
        await client.send_message(message.channel, ":white_check_mark:  JVNQ_BOT - Versão : 1.0 :white_check_mark:")



client.run("NDI0MjUzMDMxOTEyMTc3Njg1.DZu55Q.7-mmdy5WiEMozj8DTMRnN_JXaQI")
