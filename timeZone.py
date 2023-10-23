from discord.ext import commands
import timecalc

def setup(bot):
    #basic command, looks for the word link and return send()
    @bot.command()
    async def Japan(ctx):
        await ctx.send(timecalc.jp)

    @bot.command()
    async def est(ctx):
        await ctx.send(timecalc.easternst)

    @bot.command()
    async def pst(ctx):
        await ctx.send(timecalc.pst)

    @bot.command()
    async def mst(ctx):
        await ctx.send(timecalc.mst)

    @bot.command()
    async def cst(ctx):
        await ctx.send(timecalc.cst)

   