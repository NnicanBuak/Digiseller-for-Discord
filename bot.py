import os
import logging
import disnake
from disnake.ext import commands
from dotenv import dotenv_values, load_dotenv
import slash_commands


def init():
    # загрузка переменных окружения
    config = {**dotenv_values(".env.config")}
    if config["DEV"] == True:
        env_attribute = "production"
    else:
        env_attribute = "development"
    dotenv_path = f".env.{env_attribute}"
    load_dotenv(dotenv_path=dotenv_path)

    # установка переменных окружения
    BOT_TOKEN = os.environ.get("TOKEN")

    # инициализация комманд
    slash_commands.test.init(Bot)
    slash_commands.embed_test.init(Bot)
    slash_commands.auth.init(Bot)

    # уведомление о готовности к работе
    @Bot.digiseller.event
    async def on_ready():
        print("Starting:")
        print("name:", Bot.digiseller.user.name)
        print("id:", Bot.digiseller.user.id)
        print("Status: on")

    # уведомление о изменении состояния
    @Bot.digiseller.event
    async def on_state_change(state):
        print("State changed")
        print("name:", Bot.digiseller.user.name, Bot.digiseller.user.discriminator)
        print("id:", Bot.digiseller.user.id)
        print("Status:", state)

    # уведомление об ошибке и логирование ошибки на сервере
    @Bot.digiseller.event
    async def on_slash_command_error(inter, error):
        await inter.response.send_message(
            "Произошла ошибка, попробуйте позже", ephemeral=True
        )
        await logging.error(error)

    # сообщает о том что бот остановлен
    @Bot.digiseller.event
    async def stop():
        print("Stopping:")
        print("name:", Bot.digiseller.user.name)
        print("id:", Bot.digiseller.user.id)
        print("Status: off")

    # запуск бота
    Bot.digiseller.run(BOT_TOKEN)


# класс бота
class Bot:
    digiseller = commands.Bot(
        command_prefix="-",
        intents=disnake.Intents.all(),
        activity=disnake.Activity(
            type=disnake.ActivityType.watching,  # watching, listening, playing, streaming - активность бота
            name="Nnican.store",  # название активности
            url="https://discord.nnican.store",  # ссылка в статусе
            application_id=1105450039830134784,  # id бота
            large_image="nnican",  # большая картинка в статусе
            small_image="digiseller",  # маленькая картинка в статусе
            large_text="Nnican.store",  # текст при наведении на большую картинку
            small_text="digiseller",
        ),  # текст при наведении на маленькую картинку
        status=disnake.Status.online,  # статус бота (online, idle, dnd, invisible)
    )


if __name__ == "__main__":
    init()
