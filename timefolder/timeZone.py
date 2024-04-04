from discord.ext import commands
import timefolder.timecalc as timecalc

class TimeZone(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    
    @commands.command()
    async def Japan(self,ctx):
        await ctx.send(timecalc.jp)
        
    @commands.command()
    async def est(self,ctx):
        await ctx.send(timecalc.easternst)

    @commands.command()
    async def pst(self,ctx):
        await ctx.send(timecalc.pst)

    @commands.command()
    async def mst(self,ctx):
        await ctx.send(timecalc.mst)

    @commands.command()
    async def cst(self,ctx):
        await ctx.send(timecalc.cst)

async def setup(bot):
    await bot.add_cog(TimeZone(bot))
