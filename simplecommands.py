from discord.ext import commands
import discord
import stageinfo
import image_manipulation
import os
import asyncio
import cat
from PIL import Image
import matcher


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
        image_map = image_manipulation.make_graphic(
            rotation.stage1, rotation.stage2, rotation.mode, rotation.time, rotation.gamemode)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')

    async def send_rotation_info(ctx):
        rotation = stageinfo.rotation_info()
        rotation.get_xBattles()
        image_map = image_manipulation.make_graphic(
            rotation.stage1, rotation.stage2, rotation.mode, rotation.time, rotation.gamemode)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')

    @bot.command()
    async def x(ctx):
        await send_rotation_info(ctx)

    @bot.command()
    async def ranked(ctx):
        await send_rotation_info(ctx)

    @bot.command()
    async def solo(ctx):
        await send_rotation_info(ctx)

    @bot.command()
    async def open(ctx):
        rotation = stageinfo.rotation_info()
        rotation.get_anarchyOpen()
        image_map = image_manipulation.make_graphic(
            rotation.stage1, rotation.stage2, rotation.mode, rotation.time, rotation.gamemode)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')

    @bot.command()
    async def series(ctx):
        rotation = stageinfo.rotation_info()
        rotation.get_anarchySeries()
        image_map = image_manipulation.make_graphic(
            rotation.stage1, rotation.stage2, rotation.mode, rotation.time, rotation.gamemode)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')

    @bot.command()
    async def salmon(ctx):
        await send_rotation_info(ctx)

    @bot.command()
    async def searchopen(ctx, *args):
        if (len(args) == 1):
            word = args[0]
            rotaton = stageinfo.rotation_info()
            invalid = False
            if (word in matcher.abbreviations):
                map = matcher.abbreviations[word]
                maplist = rotaton.findmaps("open", map=map)
            elif (word in matcher.gamemodes):
                gamemode = matcher.gamemodes[word]
                maplist = rotaton.findmaps("open",gamemode=gamemode)
            else:
                await ctx.send("Invalid please send map or mode")
                invalid = True
            if not invalid:
                if (len(maplist) == 0):
                    await ctx.send(f'No matches')
                else:
                    list_as_string = '\n'.join(maplist)
                    await ctx.send(list_as_string)
        elif (len(args) == 2):
            map = matcher.abbreviations[args[0]]
            gamemode = matcher.gamemodes[args[1]]
            rotaton = stageinfo.rotation_info()
            maplist = rotaton.findmaps("open", map, gamemode)
            if (len(maplist) == 0):
                await ctx.send(f'No {gamemode} {map}')
            else:
                list_as_string = '\n'.join(maplist)
                await ctx.send(list_as_string)
        else:
            await ctx.send("Invalid please provide mode, map, and then gamemode")


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

    @bot.command()
    async def neko(ctx):
        image = cat.get_cat()
        await ctx.send(image)
