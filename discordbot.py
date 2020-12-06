import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('리그순위 확인 '))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!프리미어리그순위'):
        a = ''

        source = requests.get(
            "https://sports.news.naver.com/wfootball/index.nhn").text
        soup = BeautifulSoup(source, "html.parser")
        result = soup.find('div', id='_team_rank_epl')
        i = 1
        for key in result.select('span.name'):
            a = a + str(i) + "위: " + key.get_text() + "\n"
            i = i + 1

        await message.channel.send(a)

    if message.content.startswith('!분데스리가순위'):
        a = ''

        source = requests.get(
            "https://sports.news.naver.com/wfootball/index.nhn").text
        soup = BeautifulSoup(source, "html.parser")
        result = soup.find('div', id='_team_rank_bundesliga')
        i = 1
        for key in result.select('span.name'):
            a = a + str(i) + "위: " + key.get_text() + "\n"
            i = i + 1

        await message.channel.send(a)

    if message.content.startswith('!라리가순위'):
        a = ''

        source = requests.get(
            "https://sports.news.naver.com/wfootball/index.nhn").text
        soup = BeautifulSoup(source, "html.parser")
        result = soup.find('div', id='_team_rank_primera')
        i = 1
        for key in result.select('span.name'):
            a = a + str(i) + "위: " + key.get_text() + "\n"
            i = i + 1

        await message.channel.send(a)

    if message.content.startswith('!세리에A순위'):
        a = ''

        source = requests.get(
            "https://sports.news.naver.com/wfootball/index.nhn").text
        soup = BeautifulSoup(source, "html.parser")
        result = soup.find('div', id='_team_rank_seria')
        i = 1
        for key in result.select('span.name'):
            a = a + str(i) + "위: " + key.get_text() + "\n"
            i = i + 1

        await message.channel.send(a)

client.run('Nzg1MDMzNzAyNjE0NjMwNDQx.X8x9mw.wHsz9Uz0yxaYxEcDaywsGC6fJ_M')
