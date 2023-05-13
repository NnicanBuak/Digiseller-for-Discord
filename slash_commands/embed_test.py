import disnake # Импорт библиотеки disnake
import datetime # Импорт модуля времени


def init(Bot): # Функция инициализации
    @Bot.digiseller.slash_command(name="embed", description="Тест эмбедов") # Команда
    async def embed(inter): # Функция команды
        await inter.response.send_message(msg, ephemeral=True) # Отправка сообщения

    # Внутри команды, прослушивателя событий и т.д.
    msg = disnake.embeds.Embed()
    embed = disnake.Embed( # Создание эмбеда
        title="Заголовок эмбеда", # Заголовок эмбеда
        description="Описание эмбеда", # Описание эмбеда
        color=disnake.Colour.yellow(), # Цвет эмбеда
        timestamp=datetime.datetime.now(), # Время создания эмбеда
    )

    embed.set_author(
        name="Автор эмбеда", # Имя автора эмбеда
        url="https://disnake.dev/", # Ссылка на автора эмбеда
        icon_url="https://disnake.dev/assets/disnake-logo.png", # Аватар автора эмбеда
    )
    embed.set_footer( # Футер эмбеда
        text="Футер эмбеда", # Текст футера эмбеда
        icon_url="https://disnake.dev/assets/disnake-logo.png", # Аватар футера эмбеда
    )

    embed.set_thumbnail(url="https://disnake.dev/assets/disnake-logo.png") # Миниатюра эмбеда
    embed.set_image(url="https://disnake.dev/assets/disnake-thin-banner.png") # Изображение эмбеда

    embed.add_field(name="Обычный заголовок", value="Обычное значение", inline=False) # Поле эмбеда
    embed.add_field( # Поле эмбеда
        name="Встроенный заголовок", value="Встроенное значение", inline=True # Поле эмбеда
    ) # Поле эмбеда
    embed.add_field(
        name="Встроенный заголовок", value="Встроенное значение", inline=True
    )
    embed.add_field(
        name="Встроенный заголовок", value="Встроенное значение", inline=True
    )

    @Bot.digiseller.slash_command(name="embeded-test", description="Тест команда") # Команда
    async def test(inter): # Функция команды
        await inter.response.send_message( # Отправка сообщения
            embed=embed,
        )
