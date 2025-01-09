from discord.ext import commands
from discord import ui, app_commands
import discord
import nso_api


class SubmitToken(ui.Modal, title='Submit Token'):
    link = ui.TextInput(label='For instruction type /tokenhelp', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response, {interaction.user}!', ephemeral=True)
        print(interaction.data['components'][0]['components'][0]['value'])


def setup(bot):
    @bot.command()
    async def getid(ctx):
        user_id = ctx.author.id
        await ctx.send(f'Your ID is {user_id}')

    @bot.tree.command(name="yess", description="Check bot's latency")
    async def yes(interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! Latency: {round(bot.latency * 1000)}ms",ephemeral=True)

    @bot.tree.command(name="yipyip")
    @app_commands.describe(input="What should I say")
    async def say(interaction: discord.Interaction, input: str):
        await interaction.response.send_message(f'{input} :)')

    @bot.tree.command(name="modal", description="testing Modal")
    async def modal_test(interaction: discord.Interaction):

        await interaction.response.send_modal(SubmitToken())

   