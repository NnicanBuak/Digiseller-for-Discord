import disnake


def init(Bot):
    @Bot.digiseller.slash_command(name="test", description="Тест команда")
    async def test(inter):
        msg = "тест прошел успешно?"
        await inter.response.send_message(
            msg,
            ephemeral=True,
            components=[
                disnake.ui.Button(
                    label="Да", style=disnake.ButtonStyle.success, custom_id="yes"
                ),
                disnake.ui.Button(
                    label="Нет", style=disnake.ButtonStyle.danger, custom_id="no"
                ),
                disnake.ui.Button(
                    label="Нахуй я сюда нажал?",
                    style=disnake.ButtonStyle.danger, # danger, primary, secondary, success
                    custom_id="what???",
                ),
            ],
        )

    @Bot.digiseller.listen("on_button_click")
    async def help_listener(inter: disnake.MessageInteraction):
        if inter.component.custom_id not in ["yes", "no", "what???"]:
            # We filter out any other button presses except
            # the components we wish to process.
            return

        if inter.component.custom_id == "yes":
            await inter.response.send_message("Можно сохранять код!", ephemeral=True)
        elif inter.component.custom_id == "no":
            await inter.response.send_message(
                "Жаль! проверьте код и перезапустите бота", ephemeral=True
            )
        elif inter.component.custom_id == "what???":
            await inter.response.send_message("я че ебу!", ephemeral=True)
