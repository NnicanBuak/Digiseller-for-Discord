import disnake
from disnake.ext import commands
# библиотеки

# статус бота (онлайн и т.д.)
bot = commands.Bot(command_prefix='!',
                     intents= disnake.Intents.all(), # Intents discordа
                      activity = disnake.Game('Nnican', # статус что он делает (Играет в Nnican)
                       status = disnake.Status.online)) # статус по типу Онлайн и т.д.
bot.remove_command('help')
#удаляет обычную команду help (зачемяем потом на красивую)

# уведомление о готовности к работе
@bot.event
async def on_ready():
    print('Запущено:')
    print(bot.user.name)
    print(bot.user.id)
    print('Статус: готово')


# команда бота для теста
@bot.slash_command(name='тест', description='Тест команда')
async def test(inter):
    msg = "Тест успешен"
    await inter.response.send_message(msg)


# токен (хранится в файле token.txt)
token = open('token.txt', 'r').readline()
bot.run(token)