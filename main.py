import settings
import discord
import simplecommands
from timefolder import timeZone
from discord.ext import commands
from splatink import rotationcmds

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    simplecommands.setup(bot)
    timeZone.setup(bot)
    rotationcmds.setup(bot)

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()