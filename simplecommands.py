from discord.ext import commands
import discord
import stageinfo
import image_manipulation
import os
import asyncio
import cat
from PIL import Image
import pytesseract


def setup(bot):
    @bot.command()
    async def riki(ctx):
        await ctx.send("squeeze")

    @bot.command()
    async def testing(ctx):
        await ctx.send("testing")

    @bot.command()
    async def turf(ctx):
        rotation = stageinfo.rotation_info()
        rotation.get_turf()
        image_map = image_manipulation.make_graphic(rotation.stage1,rotation.stage2,rotation.mode,rotation.time)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')


    @bot.command()
    async def open(ctx):
        rotation = stageinfo.rotation_info()
        rotation.get_anarchyOpen()
        image_map = image_manipulation.make_graphic(rotation.stage1,rotation.stage2,rotation.mode,rotation.time)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')

    @bot.command()
    async def series(ctx):
        rotation = stageinfo.rotation_info()
        rotation.get_anarchySeries()
        image_map = image_manipulation.make_graphic(rotation.stage1,rotation.stage2,rotation.mode,rotation.time)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')

    @bot.command()
    async def edit(ctx):
        message = await ctx.send("https://cdn.discordapp.com/attachments/1162519403401859263/1165385244166336602/barnacle.png?ex=6546a896&is=65343396&hm=dbec87d6d93d5abd06f0972385a323063f2830f8c057773207fb1968401a4330&")
        await asyncio.sleep(2)
        await message.edit(content="https://cdn.discordapp.com/attachments/1162519403401859263/1165389464269496331/031.png?ex=6546ac84&is=65343784&hm=d0c851533c793e0b497d0b235c98854f7ba3f83344e7c9cc7f0707c410ca74c8&")
        
    @bot.command()
    async def embed(ctx):
        embed=discord.Embed(title="Turf rotation", description="This is an embed that will show how to build an embed and the different components", color=0x90EE90)
        embed.set_thumbnail(url='https://splatoon3.ink/assets/regular.64299513.svg')
        await ctx.send(embed=embed)
    
    @bot.command()
    async def neko(ctx):
        image = cat.get_cat()
        await ctx.send(image)