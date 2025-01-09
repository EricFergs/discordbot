from discord.ext import commands
from discord import ui, app_commands
import discord
import nso_api
from discord.ui import Button, View


class SubmitToken(ui.Modal, title='Submit Token'):
    link = ui.TextInput(label='For instruction type /tokenhelp', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response, {interaction.user}!', ephemeral=True)
        print(interaction.data['components'][0]['components'][0]['value'])

class retrieveToken(discord.Embed):
    def __init__(self):
        super().__init__()
        
        self.title = "Instruction to Sign in"
        self.description = """1. Visit link and sign in\n 2. Revisit the link\n 3. Right Click on the "Select this person"\n 4. Click copy link address\n 5. Submit the link to the bot"""
        self.colour = discord.Colour(0x81d8d0)
        self.set_footer(text="Disclaimer: You are sharing your account token, which can put your data at risk. Please only submit if you trust the author.")

class tokenButton(View):
    def __init__(self):
        super().__init__()
        self.add_item(Button(label="Redirect to Nintendo", style=discord.ButtonStyle.link, row = 0, url="https://accounts.nintendo.com/connect/1.0.0/authorize?state=q-wo3V4G5MhlqGPUsGGl-hYyByJXxKwWP5JgQFAppfYgI85H&redirect_uri=npf71b963c1b7b6d119%3A%2F%2Fauth&client_id=71b963c1b7b6d119&scope=openid+user+user.birthday+user.mii+user.screenName&response_type=session_token_code&session_token_code_challenge=dfMKebv-Khg1gZhQgIt7VY-Rhr73tJ3F6Lt6d-r7qGM&session_token_code_challenge_method=S256&theme=login_form"))
        #self.add_item(Button(label="Submit Token", style=discord.ButtonStyle.secondary,custom_id="submit_token"))
    
    @discord.ui.button(label="Submit Token", style=discord.ButtonStyle.secondary, custom_id="submit_token")
    async def submit_button(self, interaction: discord.Interaction,button: Button,):
        await interaction.response.send_modal(SubmitToken())
        
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

    @bot.tree.command(name ="token", description="Retrieve user token")
    async def token(interaction):
        await interaction.response.send_message(ephemeral = True, embed = retrieveToken(),view = tokenButton())
       