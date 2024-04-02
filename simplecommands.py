from discord.ext import commands
import discord
import asyncio


def setup(bot):
    @bot.command()
    async def riki(ctx):
        await ctx.send("squeeze")

    @bot.command()
    async def edit(ctx):
        message = await ctx.send("https://cdn.discordapp.com/attachments/1162519403401859263/1165385244166336602/barnacle.png?ex=6546a896&is=65343396&hm=dbec87d6d93d5abd06f0972385a323063f2830f8c057773207fb1968401a4330&")
        await asyncio.sleep(2)
        await message.edit(content="https://cdn.discordapp.com/attachments/1162519403401859263/1165389464269496331/031.png?ex=6546ac84&is=65343784&hm=d0c851533c793e0b497d0b235c98854f7ba3f83344e7c9cc7f0707c410ca74c8&")

    @bot.command()
    async def embed(ctx):
        embed = discord.Embed(
            title="Turf rotation", description="This is an embed that will show how to build an embed and the different components", color=0x90EE90)
        embed.set_thumbnail(
            url='https://splatoon3.ink/assets/regular.64299513.svg')
        await ctx.send(embed=embed)

    