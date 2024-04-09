from discord.ext import commands
import discord
import splatink.stageinfo as stageinfo
import splatink.image_manipulation as image_manipulation
import os
from PIL import Image
from splatink import matcher
import splatink.editdistance as editdistance


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
        rotations = []
        for i in range(1, 5):  
            rotation = stageinfo.salmon_info()
            rotation.get_salmon(str(i))  
            rotations.append(rotation)

        image_map = image_manipulation.make_salmon(rotations)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')
        

    async def searchrotation(ctx, mode, *args):
        if (len(args) == 1):
            word = args[0]
            rotaton = stageinfo.rotation_info()
            invalid = False
            if (word in matcher.gamemodes):
                gamemode = matcher.gamemodes[word]
                maplist = rotaton.findmaps(mode, gamemode=gamemode)
            elif (len(editdistance.check_close_maps(word)) != 0):
                word = matcher.abbreviations[editdistance.check_close_maps(word)[0]]
                maplist = rotaton.findmaps(mode, map=word)
            else:
                await ctx.send("Invalid please insert map, mode, or both")
                invalid = True
            if not invalid:
                if (len(maplist) == 0):
                    await ctx.send(f'No {word} matches')
                else:
                    list_as_string = '\n'.join(maplist)
                    await ctx.send(list_as_string)
        elif (len(args) == 2):
            word = args[0]
            word2 = args[1]
            invalid = False
            rotaton = stageinfo.rotation_info()
            if (len(editdistance.check_close_maps(word)) != 0):
                map = matcher.abbreviations[editdistance.check_close_maps(word)[0]]
                if (word2 in matcher.gamemodes):
                    gamemode = matcher.gamemodes[word2]
                    maplist = rotaton.findmaps(
                        mode, map=map, gamemode=gamemode)
                else:
                    invalid = True
            elif (word in matcher.gamemodes):
                gamemode = matcher.gamemodes[word]
                if (len(editdistance.check_close_maps(word2)) != 0):
                    map = matcher.abbreviations[editdistance.check_close_maps(word2)[0]]
                    maplist = rotaton.findmaps(
                        mode, map=map, gamemode=gamemode)
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
                await ctx.send("Invalid please insert map, mode, or both")
        else:
            await ctx.send("Invalid please insert map, mode, or both")

    @bot.command()
    async def searchturf(ctx, *args):
        if (len(args) == 1 and (args[0] in matcher.abbreviations)):
            map = matcher.abbreviations[args[0]]
            rotaton = stageinfo.rotation_info()
            maplist = rotaton.findmaps("turf", map=map, gamemode="Turf War")
            if (len(maplist) == 0):
                    await ctx.send(f'No {map}')
            else:
                list_as_string = '\n'.join(maplist)
                await ctx.send(list_as_string)
        else:
            await ctx.send("Please insert a map")

    @bot.command()
    async def searchopen(ctx, *args):
        await searchrotation(ctx, "open", *args)

    @bot.command()
    async def searchseries(ctx, *args):
        await searchrotation(ctx, "series", *args)

    @bot.command()
    async def searchx(ctx, *args):
        await searchrotation(ctx, "x", *args)
