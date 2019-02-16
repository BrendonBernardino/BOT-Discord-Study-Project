import discord
import random
#import youtube_dl
import time
import datetime
import asyncio
import requests
import json

client = discord.Client()

players = {}
COR = 0xF7FE2E

@client.event
async def on_ready():
    print('Funfando!')
    print(client.user.name)
    print(client.user.id)
    print('___________________ON_____________________')

#lista = ["test"]
@client.event
async def on_message(message):
#FUNÇÃO INFORMAÇÃO DO BOT

    if message.content.lower().startswith('?info'):
        await client.delete_message(message)
        embedbot = discord.Embed(
            title='**🤖 Informações do Bot**',
            color=0x00a3cc,
            description='\n'
        )
        embedbot.add_field(name='`💮 | Nome`', value=client.user.name, inline=True)
        embedbot.add_field(name='`◼ | Id bot`', value=client.user.id, inline=True)
        embedbot.add_field(name='💠 | Criado em', value=client.user.created_at.strftime("%d %b %Y %H:%M"))
        embedbot.add_field(name='📛 | Tag', value=client.user)
        embedbot.add_field(name='‍💻 | Servidores', value=len(client.servers))
        embedbot.add_field(name='👥 | Usuários', value=len(list(client.get_all_members())))
        embedbot.add_field(name='‍⚙️ | Programador', value="`Brendon Wesley (βØટટ.Ъιη)`")
        embedbot.add_field(name='🐍 Python  | Version',
                           value="`3.6.5`")
        embedbot.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)
        embedbot.add_field(name='‍--COMANDOS--', value=" ?info - ?status - ?ping - ?quest - ?day - ?fon - ?moeda - "
                                                   "?contagem5 - ?contagem10 - ?vote - ?hora - ?entrar - ?sair - "
                                                   "?champ - ?top - ?jg - ?adc - ?supp - ?d6 - ?2d6 - ?d10 - ?2d10 - "
                                                    "?d100 - ?2d100 ")
        embedbot.add_field(name='‍--COMANDOS DE NOTÍCIAS BR--', value=" ?newsglobo - ?newsgoogle ")
        embedbot.add_field(name='‍--COMANDOS DE NOTÍCIAS--', value=" ?newsreddit - ?newsign - ?newspolygon - "
                                                                   "?newsbbc - ?newscbc - ?newshacker - ?newsmoney - "
                                                                   "?newsnationalgeo - ?newsyorktimes - "
                                                                   "?newscryptomoedas ")
        await client.send_message(message.channel, embed=embedbot)

    if message.content.lower().startswith('?status'):
        await client.send_message(message.channel,"Tamo aq po")

    if message.content.lower().startswith('?day'):
        await client.send_message(message.channel,"Amanheceu o dia...")

    if message.content.lower().startswith('?fon'):
        await client.send_message(message.channel,"fon")

    if message.content.lower().startswith('?olhou'):
        await client.send_message(messagechannel, "chupou")


#FUNÇÃO DE CARA OU COROA

    if message.content.lower().startswith('?moeda'):
        choice = random.randint(1,2)
        if choice == 1:
            #await client.add_reaction(message, '😀')
            await client.send_message(message.channel, "😀\nVocê tirou CARA!")
        if choice == 2:
            #await client.add_reaction(message, '👑')
            await client.send_message(message.channel, "👑\nVocê tirou COROA!")

#FUNÇÃO RESPOSTA EM PALAVRA

    #for palavra in lista:
    #    if palavra in message.content.lower():
    #        return await client.send_message(message.channel,
    #                                        "test funfou")

    #if 'test' in message.content.lower():
    #    await client.send_message(message.channel,
    #                                    "funfou")

#FUNÇÃO DE NOTÍCIAS


    if message.content.lower().startswith('?newsglobo'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=globo&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    if message.content.lower().startswith('?newsign'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=ign&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    if message.content.lower().startswith('?newspolygon'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=polygon&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    if message.content.lower().startswith('?newsreddit'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=reddit-r-all&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    if message.content.lower().startswith('?newsbbc'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    if message.content.lower().startswith('?newscbc'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=cbc-news&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    if message.content.lower().startswith('?newsgoogle'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=google-news-br&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    if message.content.lower().startswith('?newshacker'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=hacker-news&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    if message.content.lower().startswith('?newsmoney'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=info-money&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    if message.content.lower().startswith('?newsnationalgeo'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=national-geographic&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    if message.content.lower().startswith('?newsyorktimes'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=the-new-york-times&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)

    if message.content.lower().startswith('?newscryptomoedas'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=crypto-coins-news&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)



#FUNÇÕES DE CONTAGEM REGRESSIVA

    if message.content.startswith("?contagem5"):
        mensagem = "**5**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**4**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**3**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**2**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**1**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**💥 BOOM 💥**"
        await client.send_message(message.channel, mensagem)

    if message.content.startswith("?contagem10"):
        mensagem = "**10**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**9**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**8**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**7**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**6**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**5**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**4**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**3**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**2**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**1**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**💥 BOOM 💥**"
        await client.send_message(message.channel, mensagem)

#FUNÇÃO DE VOTAÇÃO

    if message.content.lower().startswith('?vote'):
        vote = message.content[6:].strip()
        votee = await client.send_message(message.channel,
                                          message.author.mention + " **Iniciou uma votação**\n\n➜``" + vote + "``")
        await client.delete_message(message)
        await client.add_reaction(votee, '👍')
        await client.add_reaction(votee, '👎')

#FUNÇÃO DE HORA

    if message.content.startswith('?hora'):
        horario = datetime.datetime.now().strftime("\n%H:%M:%S")
        await client.send_message(message.channel,
                                  "**⌚ Hora local atual {} **{}".format(message.server.region, horario))
        await client.send_message(message.channel,
                                  "**Servidor: {}**".format(
                                      message.server.region))


#FUNÇÃO DE MS

    if message.content.lower().startswith('?ping'):
        channel = message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        ping_embed = discord.Embed(title="🏓 Pong!", color=0x000000,
                                   description='Meu ping é `{}ms`!'.format(round((t2 - t1) * 1000)))
        await client.send_message(message.channel, f"{message.author.mention}", embed=ping_embed)

#FUNÇÃO DE PERGUNTA

    if message.content.lower().startswith('?quest'):
        try:
            respostas = ['Sim', 'Não', 'Talvez', 'Nunca', 'Claro']
            resposta = random.choice(respostas)
            mensagem = message.content[7:]
            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name="Pergunta:", value='{}'.format(mensagem), inline=False)
            embed.add_field(name="Resposta:", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Você precisa perguntar alguma coisa!')

#FUNÇÕES DENTRO DE CANAL DE VOZ

    if message.content.startswith('?entrar'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "Já estou em um canal de voz, animal")
        except Exception as error:
            await client.send_message(message.channel, "Não posso entrar nesse canal.".format(error=error))

    if message.content.startswith('?sair'):
        try:
            mscleave = discord.Embed(
                title="\n",
                color=COR,
                description="Saí do canal de voz e a música parou!"
            )
            voice_client = client.voice_client_in(message.server)
            await client.send_message(message.channel, embed=mscleave)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "O bot não está em nenhum canal de voz, fela")
        except Exception as Hugo:
            await client.send_message(message.channel, "Error 2: ```{haus}```".format(haus=Hugo))

#FUNÇÕES DE LOL

    if message.content.lower().startswith('?teotop'):
        await client.delete_message(message)
        embed = discord.Embed(color=0xCD0BD9)
        embed.add_field(name='‍🥇 Champion Pool do Téo 🏆', value=" Malphite - Darius - Sion - Jax - Cho gath ")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('?felipejg'):
        await client.delete_message(message)
        embed = discord.Embed(color=0xCD0BD9)
        embed.add_field(name='‍🥇 Champion Pool do Felipe 🏆', value=" ")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('?natanmid'):
        await client.delete_message(message)
        embed = discord.Embed(color=0xCD0BD9)
        embed.add_field(name='‍🥇 Champion Pool do Natan 🏆', value=" Syndra - Orianna - Swain - Zoe - Galio ")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('?emersonadc'):
        await client.delete_message(message)
        embed = discord.Embed(color=0xCD0BD9)
        embed.add_field(name='‍🥇 Champion Pool do Emerson 🏆', value=" ")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('?brendonsupp'):
        await client.delete_message(message)
        embed = discord.Embed(color=0xCD0BD9)
        embed.add_field(name='‍🥇 Champion Pool do Brendon 🏆', value=" Thresh - Bardo - Shen - Pyke - Braum ")
        await client.send_message(message.channel, embed=embed)


    if message.content.lower().startswith('?champ'):
        try:
            respostas = ['Aatrox', 'Ahri', 'Akali', 'Allistar', 'Amumu', 'Anivia', 'Annie', 'Ashe', 'Aurelion', 'Azir',
                         'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', 'Cho Gath',
                         'Corki', 'Darius', 'Diana', 'Dr.Mundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal',
                         'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves',
                         'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce',
                         'Jhin', 'Jinx', 'Kai sa', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle',
                         'Kayn', 'Kennen', 'Kha Zix', 'Kindred', 'Kled', 'Kog Maw', 'LeBlanc', 'Lee Sin', 'Leona',
                         'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Master Yi',
                         'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Nidalee', 'Nocturne',
                         'Nunu e Willump', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Quinn', 'Rakan',
                         'Rammus', 'Rek sai', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Sejuani', 'Shaco',
                         'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Syndra',
                         'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle',
                         'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', 'Vel Koz',
                         'Vi', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xayah', 'Xerath', 'Xin Zhao',
                         'Yasuo', 'Yorick', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']
            resposta = random.choice(respostas)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0xD4A413)
            embed.add_field(name="Champ Aleatório:", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Você precisa perguntar alguma coisa!')

    if message.content.lower().startswith('?top'):
        try:
            respostas = ['Aatrox', 'Akali', 'Camille', 'Cho Gath', 'Darius', 'Dr.Mundo', 'Fiora', 'Gangplank', 'Garen',
                         'Gnar', 'Gragas', 'Illaoi', 'Irelia', 'Jax', 'Jayce', 'Kayle', 'Kennen', 'Kled', 'Malphite',
                         'Maokai', 'Mordekaiser', 'Nasus', 'Nautilus', 'Ornn', 'Pantheon', 'Poppy', 'Quinn', 'Renekton',
                         'Riven', 'Rumble', 'Ryze', 'Shen', 'Singed', 'Sion', 'Swain', 'Teemo', 'Trundle', 'Tryndamere',
                         'Urgot', 'Vladimir', 'Wukong', 'Yorick']
            resposta = random.choice(respostas)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0x666666)
            embed.add_field(name="Top Aleatório:", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Você precisa perguntar alguma coisa!')

    if message.content.lower().startswith('?jg'):
        try:
            respostas = ['Amumu', 'Camille', 'Cho Gath', 'Diana', 'Dr.Mundo', 'Ekko', 'Elise', 'Evelynn', 'Ezreal',
                         'Fiddlesticks', 'Fiora', 'Gragas', 'Graves', 'Hecarim', 'Ivern', 'Jarvan IV', 'Jax', 'Kayn',
                         'Kha Zix', 'Kindred', 'Lee Sin', 'Maokai', 'Master Yi', 'Nautilus', 'Nidalee', 'Nocturne',
                         'Nunu e Willump', 'Olaf', 'Pantheon', 'Poppy', 'Rammus', 'Rek sai', 'Rengar', 'Riven',
                         'Sejuani','Shaco', 'Shyvana', 'Singed', 'Skarner', 'Taliyah', 'Teemo', 'Trundle', 'Tryndamere',
                         'Twitch', 'Udyr', 'Vi', 'Volibear', 'Warwick', 'Wukong', 'Xin Zhao', 'Zac']
            resposta = random.choice(respostas)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0x6AA84F)
            embed.add_field(name="Jungle Aleatório:", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Você precisa perguntar alguma coisa!')

    if message.content.lower().startswith('?mid'):
        try:
            respostas = ['Ahri', 'Akali', 'Anivia', 'Annie', 'Aurelion', 'Azir', 'Brand', 'Cassiopeia', 'Corki',
                         'Diana', 'Ekko', 'Ezreal', 'Fizz', 'Galio', 'Heimerdinger', 'Karma', 'Karthus', 'Kassadin',
                         'Katarina', 'Kayle', 'LeBlanc', 'Lissandra', 'Lucian', 'Lux', 'Malzahar', 'Mordekaiser',
                         'Morgana', 'Orianna', 'Pantheon', 'Ryze', 'Syndra', 'Taliyah', 'Talon', 'Twisted Fate',
                         'Veigar', 'Vel Koz', 'Viktor', 'Vladimir', 'Xerath', 'Yasuo', 'Zed', 'Ziggs', 'Zilean', 'Zoe']
            resposta = random.choice(respostas)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0xFFFF00)
            embed.add_field(name="Mid Aleatório:", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Você precisa perguntar alguma coisa!')

    if message.content.lower().startswith('?adc'):
        try:
            respostas = ['Ashe', 'Caitlyn', 'Corki', 'Draven', 'Ezreal', 'Graves', 'Jhin', 'Jinx', 'Kai sa', 'Kalista',
                         'Kindred', 'Kog Maw', 'Lucian', 'Miss Fortune', 'Mordekaiser', 'Quinn', 'Sivir', 'Tristana',
                         'Twitch', 'Varus', 'Vayne', 'Xayah', 'Ziggs']
            resposta = random.choice(respostas)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0x660000)
            embed.add_field(name="Adc Aleatório:", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Você precisa perguntar alguma coisa!')

    if message.content.lower().startswith('?supp'):
        try:
            respostas = ['Allistar', 'Annie', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Fiddlesticks', 'Janna', 'Karma',
                         'Leona', 'Lulu', 'Lux', 'Malzahar', 'Morgana', 'Nami', 'Nautilus', 'Nidalee', 'Ornn', 'Pyke',
                         'Rakan', 'Shen', 'Sona', 'Soraka', 'Tahm Kench', 'Taric', 'Teemo', 'Thresh', 'Trundle',
                         'Veigar', 'Vel Koz', 'Volibear', 'Xerath', 'Zilean', 'Zyra']
            resposta = random.choice(respostas)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0x00FFFF)
            embed.add_field(name="Suporte Aleatório:", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Você precisa perguntar alguma coisa!')

#FUNÇÃO DE ROLAR DADO

    if message.content.lower().startswith('?d6'):
        try:
            respostas = ['1', '2', '3', '4', '5', '6']
            resposta = random.choice(respostas)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0xFFFFFF)
            embed.add_field(name="🎲 D6 Played", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Deu pau aqui, joga o dado man.')

    if message.content.lower().startswith('?2d6'):
        try:
            respostas = ['1', '2', '3', '4', '5', '6']
            respostas2 = ['1', '2', '3', '4', '5', '6']
            resposta = random.choice(respostas)
            resposta2 = random.choice(respostas2)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0xFFFFFF)
            embed.add_field(name="🎲 2D6 Played", value=resposta, inline=False)
            embed.add_field(name="🎲", value=resposta2, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Deu pau aqui, joga o dado man.')

    if message.content.lower().startswith('?d20'):
        try:
            respostas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                         '18', '19', '20']
            resposta = random.choice(respostas)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0xFFFFFF)
            embed.add_field(name="🎲 D20 Played", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Deu pau aqui, joga o dado man.')

    if message.content.lower().startswith('?2d20'):
        try:
            respostas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                         '18', '19', '20']
            respostas2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                         '18', '19', '20']
            resposta = random.choice(respostas)
            resposta2 = random.choice(respostas2)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0xFFFFFF)
            embed.add_field(name="🎲 2D20 Played", value=resposta, inline=False)
            embed.add_field(name="🎲", value=resposta2, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Deu pau aqui, joga o dado man.')

    if message.content.lower().startswith('?d100'):
        try:
            respostas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                         '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33',
                         '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                         '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65',
                         '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77','78', '79', '80', '81',
                         '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97',
                         '98', '99', '100']
            resposta = random.choice(respostas)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0xFFFFFF)
            embed.add_field(name="🎲 D100 Played", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Deu pau aqui, joga o dado man.')

    if message.content.lower().startswith('?2d100'):
        try:
            respostas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                         '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33',
                         '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                         '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65',
                         '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81',
                         '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97',
                         '98', '99', '100']
            respostas2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                         '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33',
                         '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                         '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65',
                         '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81',
                         '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97',
                         '98', '99', '100']
            resposta = random.choice(respostas)
            resposta2 = random.choice(respostas2)
            #mensagem = message.content[7:]
            embed = discord.Embed(color=0xFFFFFF)
            embed.add_field(name="🎲 2D100 Played", value=resposta, inline=False)
            embed.add_field(name="🎲", value=resposta2, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Deu pau aqui, joga o dado man.')

    #if message.content.startswith('?play'):
    #    try:
    #        yt_url = message.content[6:]
    #        if client.is_voice_connected(message.server):
    #            try:
    #                voice = client.voice_client_in(message.server)
    #                players[message.server.id].stop()
    #                player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
    #                players[message.server.id] = player
    #                player.start()
    #                mscemb = discord.Embed(
    #                    title="Música para tocar:",
    #                    color=COR
    #                )
    #                mscemb.add_field(name="Nome:", value="`{}`".format(player.title))
    #                mscemb.add_field(name="Visualizações:", value="`{}`".format(player.views))
    #                mscemb.add_field(name="Enviado em:", value="`{}`".format(player.uploaded_date))
    #                mscemb.add_field(name="Enviado por:", value="`{}`".format(player.uploadeder))
    #                mscemb.add_field(name="Duraçao:", value="`{}`".format(player.uploadeder))
    #                mscemb.add_field(name="Likes:", value="`{}`".format(player.likes))
    #                mscemb.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
    #                await client.send_message(message.channel, embed=mscemb)
    #            except Exception as e:
    #                await client.send_message(message.server, "Error 3: [{error}]".format(error=e))

    #        if not client.is_voice_connected(message.server):
    #            try:
    #                channel = message.author.voice.voice_channel
    #                voice = await client.join_voice_channel(channel)
    #                player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
    #                players[message.server.id] = player
    #                player.start()
    #                mscemb2 = discord.Embed(
    #                    title="Música para tocar:",
    #                    color=COR
    #                )
    #                mscemb2.add_field(name="Nome:", value="`{}`".format(player.title))
    #                mscemb2.add_field(name="Visualizações:", value="`{}`".format(player.views))
    #                mscemb2.add_field(name="Enviado em:", value="`{}`".format(player.upload_date))
    #                mscemb2.add_field(name="Enviado por:", value="`{}`".format(player.uploader))
    #                mscemb2.add_field(name="Duraçao:", value="`{}`".format(player.duration))
    #                mscemb2.add_field(name="Likes:", value="`{}`".format(player.likes))
    #                mscemb2.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
    #                await client.send_message(message.channel, embed=mscemb2)
    #            except Exception as error:
    #                await client.send_message(message.channel, "Error 4: Sala full mano".format(error=error))
    #    except Exception as e:
    #        await client.send_message(message.channel, "Error 5: [{error}]".format(error=e))

    #if message.content.startswith('?pause'):
    #    try:
    #        mscpause = discord.Embed(
    #            title="\n",
    #            color=COR,
    #            description="Musica pausada com sucesso!"
    #        )
    #        await client.send_message(message.channel, embed=mscpause)
    #        players[message.server.id].pause()
    #    except Exception as error:
    #        await client.send_message(message.channel, "Error 6: [{error}]".format(error=error))
    #if message.content.startswith('?resume'):
    #    try:
    #        mscresume = discord.Embed(
    #            title="\n",
    #            color=COR,
    #            description="De volta a música!"
    #        )
    #        await client.send_message(message.channel, embed=mscresume)
    #        players[message.server.id].resume()
    #    except Exception as error:
    #        await client.send_message(message.channel, "Error 7: [{error}]".format(error=error))

client.run('')
