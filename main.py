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
        await bot.load_extension("timefolder.timeZone")
    simplecommands.setup(bot)
    rotationcmds.setup(bot)

    @bot.command()
    async def reloadtime(ctx):
        await bot.unload_extension("timefolder.timeZone")
        await bot.load_extension("timefolder.timeZone")
        await ctx.send("File has been reloaded")

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()