import disnake


def add(Bot):
    @Bot.digiseller.slash_command(name="test", description="Тест команда")
    async def test(inter):
        await inter.response.send_message(
            "тест прошел успешно?",
            components=[
                disnake.ui.Button(
                    label="Да", style=disnake.ButtonStyle.success, custom_id="yes"
                ),
                disnake.ui.Button(
                    label="Нет", style=disnake.ButtonStyle.danger, custom_id="no"
                ),
            ],
        )

    @Bot.digiseller.listen("on_button_click")
    async def help_listener(inter: disnake.MessageInteraction):
        if inter.component.custom_id not in ["yes", "no"]:
            # We filter out any other button presses except
            # the components we wish to process.
            return

        if inter.component.custom_id == "yes":
            await inter.response.send_message("Можно сохранять код!")
        elif inter.component.custom_id == "no":
            await inter.response.send_message(
                "Жаль! проверьте код и перезапустите бота"
            )
