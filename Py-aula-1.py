import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Carregando")
    print("Servidores: {} Serves".format(str(len(client.servers))))
    print("Bot Online")


client.run("")
