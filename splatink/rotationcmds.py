from discord.ext import commands
import discord
import splatink.stageinfo as stageinfo
import splatink.image_manipulation as image_manipulation
import os
from PIL import Image
from splatink import matcher


def setup(bot):
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
        rotation = stageinfo.salmon_info()
        await ctx.send(rotation.get_salmon())

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
