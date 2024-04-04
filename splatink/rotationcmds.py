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
                await ctx.send("Invalid please insert map, mode, or both")
                invalid = True
            if not invalid:
                if (len(maplist) == 0):
                    await ctx.send(f'No matches')
                else:
                    list_as_string = '\n'.join(maplist)
                    await ctx.send(list_as_string)
        elif (len(args) == 2):
            word = args[0]
            word2 = args[1]
            invalid = False
            rotaton = stageinfo.rotation_info()
            if (word in matcher.abbreviations):
                map = matcher.abbreviations[word]
                if (word2 in matcher.gamemodes):
                    gamemode = matcher.gamemodes[word2]
                    maplist = rotaton.findmaps("open", map=map, gamemode=gamemode)
                else:
                    invalid = True
            elif (word in matcher.gamemodes):
                gamemode = matcher.gamemodes[word]
                if(word2 in matcher.abbreviations):
                    map = matcher.abbreviations[word2]
                    maplist = rotaton.findmaps("open", map=map, gamemode=gamemode)
                else:
                    invalid = True
            else:
                invalid = True
            if not invalid:
                if (len(maplist) == 0):
                    await ctx.send(f'No {gamemode} {map}')
                else:
                    list_as_string = '\n'.join(maplist)
                    await ctx.send(list_as_string)
            else: 
                await ctx.send("Invalid the map or mode has a typo")
        else:
            await ctx.send("Invalid please insert map, mode, or both")
