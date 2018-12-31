import discord

color = 0xe081e4

client = discord.Client ()

@client.event
async def on_ready():
    print ( "------------ Carregando -------------" )
    print ( "Servidores: {} Serves".format ( str ( len ( client.servers ) ) ) )
    print ( "------------ Bot Online -------------" )

@client.event
async def on_message(message):
        if not (not message.content.startswith('!fale')and not message.content.startswith('!falar')):
        if message.author.id == 'ID DO BOT':
            return
        try:
            mensagem = message.content[7:]
            await client.delete_message ( message )
            await client.send_message ( message.channel, mensagem, tts=False)
            print ( 'Fale on' )
            print ( mensagem )
        except:
            embed1 = discord.Embed ( color=color)
            embed1.add_field(name="Falar",value='Você Precisa Digitar Algo Para Eu Falar')
            await client.send_message(message.channel, embed=embed1)

