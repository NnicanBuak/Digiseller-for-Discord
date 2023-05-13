import disnake
import requests
import time
from hashlib import sha256


def init(Bot):
    # команда
    @Bot.digiseller.slash_command(name="auth", description="Тест команда")
    async def auth(inter, seller_id: int, api_key: str):
        command_time = time.time()
        response = await requests.post(
            "https://api.digiseller.ru/api/apilogin",
            data={
                "seller_id": seller_id,
                "timestamp": command_time,
                "sign": sha256(api_key + str(command_time)),
            },
        )
        await inter.response.send_message(
            "Вы успешно авторизовались!\n" + response,
            ephemeral=True,
        )
