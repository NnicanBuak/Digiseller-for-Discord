# discord.py приложение которое создаёт интерфейс для взаимодействия с API digiseller и созданя панели магазина digiseller для дискорда, используется Digiseller API
# Версия: 1.0
# Автор: NnicanBuak#0001
# Гитхаб: https://github.com/NnicanBuak/Digiseller-for-Discord
import discord as ds
from discord.app_commands import Command
import requests
import dotenv
from time import time
from hashlib import sha256


ENDPOINTS = {"APIlogin": "https://api.digiseller.ru/api/apilogin"}
TOKEN = "MTEwNTAzNDcxNzM2OTIxMjkzOA.G85xIa.DPzEBdIlUbvJrCUjFyT-aaWOzuy__3f5w6nfSs"

# Инициализация приложния
client = ds.Client(intents=ds.Intents.all())
guild = ds.Guild
tree = ds.app_commands.CommandTree(
    client=client,
)


# Определение всех слэш-команд (команды используют third-party API Digiseller)


# команда авторизации /auth <SELLER_ID> <API_KEY> (для администратора)
@tree.add_command(
    guild=[guild.id],
)
async def auth(ctx, SELLER_ID, API_KEY: str):
    # GET запрос к API Digiseller
    response = await requests.get(
        endpoints["APIlogin"],
        params={
            "seller_id": SELLER_ID,
            "timestamp": "1",
            "sign": sha256(API_KEY + str(time())),
        },
    )
    # Проверка на успешность запроса
    if response.status_code != 200:
        await ctx.respond("Ошибка, попробуйте позже")
        return
    # Проверка на успешность авторизации
    if response.json()["IsSuccess"] != True:
        await ctx.respond("Ошибка авторизации, проверьте ключ")
        return
    # Ответ бота
    ctx.respond("Вы авторизовались в системе Digiseller")


# Синхронизация команд когда клиент готов
@client.event
async def on_ready():
    print("Bot is ready")
    await tree.sync_all_commands()


# Запуск бота
client.run(PUBLIC_KEY)
