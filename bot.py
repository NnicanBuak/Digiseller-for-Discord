# библиотеки
import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

# переменные окружения
env_config = os.getenv(".config")
print(env_config)
env_attribute = "ENVIRONMENT"
if env_config == "production":
    env_attribute = os.getenv("production")
if env_config == "development":
    env_attribute = os.getenv("development")
dotenv_path = f".env.{env_attribute}"
load_dotenv(dotenv_path=dotenv_path)

# статус бота (онлайн и т.д.)
bot = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents.all(),  # Intents discordа
    activity=disnake.Game(
        "Nnican", status=disnake.Status.online  # статус что он делает (Играет в Nnican)
    ),
)  # статус по типу Онлайн и т.д.
bot.remove_command("help")
# удаляет обычную команду help (зачемяем потом на красивую)


# уведомление о готовности к работе
@bot.event
async def on_ready():
    print("Запущено:")
    print(bot.user.name)
    print(bot.user.id)
    print("Статус: готово")


# команда бота для теста
@bot.slash_command(name="тест", description="Тест команда")
async def test(inter):
    msg = "Тест успешен"
    await inter.response.send_message(msg)


# токен (хранится в файле token.txt)
token = open("token.txt", "r").readline()
bot.run(token)
