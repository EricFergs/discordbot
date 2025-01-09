import settings
import discord
import simplecommands
from timefolder import timeZone
from discord.ext import commands
from discord import app_commands
from splatink import rotationcmds
from splatnet import nsobot
from discord import HTTPException



logger = settings.logging.getLogger("bot")
GUILD_ID = discord.Object(id=1326236006772375682) 
deletecommand = [1288758710310801441,1288758710310801440]

class MyBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.tree = app_commands.CommandTree(self)  # This handles the slash commands

    async def setup_hook(self):
        # Load extensions during bot setup
        nsobot.setup(self)
        
        # Sync application commands (slash commands)

        
        
        self.tree.copy_global_to(guild=GUILD_ID)
        await self.tree.sync(guild=GUILD_ID)
        
        #self.log_synced_commands()

        await self.load_extension("timefolder.timeZone")
        simplecommands.setup(self)
        rotationcmds.setup(self)
        

    def log_synced_commands(self):
        # Retrieve and print all commands in the command tree
        commands_list = self.tree.get_commands(guild=GUILD_ID)  # Get commands for the specific guild
        logger.info("Synced Commands:")
        
        if not commands_list:
            logger.info("No commands synced.")
        
        for command in commands_list:
            logger.info(f" - {command.name}: {command.description}")
    def check_synced_guilds(self):
        # List all guilds this bot is in
        guilds = self.guilds
        logger.info("This bot is currently in the following guilds:")
        
        for guild in guilds:
            logger.info(f" - Guild ID: {guild.id}, Name: {guild.name}")
   
def run():
    intents = discord.Intents.default()
    intents.guilds = True 
    intents.message_content = True

    bot = MyBot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

       
    
    @bot.command()
    async def reloadtime(ctx):
        await bot.unload_extension("timefolder.timeZone")
        await bot.load_extension("timefolder.timeZone")
        await ctx.send("File has been reloaded")
    
    @bot.command()
    async def end(ctx):
        await ctx.send("Bot shutting off")
        await bot.close()
    

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()