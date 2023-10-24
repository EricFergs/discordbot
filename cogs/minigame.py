import asyncio
import discord
import os
from discord.ext import commands
from cogs import moves
import image_manipulation


def player1(new_embed, value1,value2,player1,player2,line2 = ""):
    move1, damage1 = moves.select_move(player1)
    value2 = value2 - damage1
    line1 = f":arrow_backward:{player1} uses __{move1}__ against {player2} for __{damage1}__"
    if value1 <= 0 or value2 <= 0:
        if value1 > value2:
            winner = player1
        else:
            winner = player2
        new_embed = discord.Embed(
        colour=discord.Colour.dark_teal(),
        description=f'{line1}\n{line2}\n:trophy: {winner} has won!',
    )
    else:
        new_embed = discord.Embed(
            colour=discord.Colour.dark_teal(),
            description= f"{line1}\n{line2}"
        )
    new_embed.add_field(name=player1,value= str(value1)+"/100")
    new_embed.insert_field_at(0,name=player2,value=str(value2)+"/100")
    return new_embed, value1, value2, line1

def player2(new_embed, value1,value2,player1,player2,line1):
    move2, damage2 = moves.select_move(player2)
    value1 = value1 - damage2
    line2 = f":arrow_forward: {player2} uses __{move2}__ against {player1} for __{damage2}__"
    if value1 <= 0 or value2 <= 0:
        if value1 > value2:
            winner = player1
        else:
            winner = player2
        new_embed = discord.Embed(
        colour=discord.Colour.dark_teal(),
        description=f'{line2}\n{line1}\n:trophy: {winner} has won!',
    )
    else:
        new_embed = discord.Embed(
            colour=discord.Colour.dark_teal(),
            description= f"{line2}\n{line1}"
        )
    new_embed.add_field(name=player1,value= str(value1)+"/100")
    new_embed.insert_field_at(0,name=player2,value=str(value2)+"/100")
    return new_embed, value1, value2, line2

class Minigame(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def hello(self, ctx, *,member: discord.Member):
        await ctx.send(f'Hello {member.name} i made this changes')

    
    @commands.command()
    async def fight(self,ctx):
        author = ctx.author.display_name
        display_name = ctx.message.mentions[0].display_name
        #author_pfp = ctx.author.display_avatar
        #display_pfp = ctx.message.mentions[0].display_avatar
        image_manipulation.fight_scene(author,display_name)
        embed = discord.Embed(
            colour=discord.Colour.dark_teal(),
            description=":boom: The battle has started!",
        )
        embed.add_field(name=author,value="100/100")
        embed.insert_field_at(0,name=display_name,value="100/100")
        value1 = 100
        value2 = 100
        await ctx.send(file=discord.File('fight.png'))
        message = await ctx.send(embed=embed)
        i = 2 
        line2 = ""
        while(value1 > 0 and value2 >0):
            if(i%2 == 0):
                new_embed, value1, value2, line1 = player1(embed,value1,value2,author,display_name,line2)
            else:
                new_embed, value1, value2, line2 = player2(embed,value1,value2,author,display_name,line1)
            await asyncio.sleep(2.5)
            await message.edit(embed=new_embed)
            i += 1




    @commands.command()
    async def who(self,ctx):
        author = ctx.author
        author_name = author.display_name
        if ctx.message.mentions:
            display_name = ctx.message.mentions[0].display_name
        await ctx.send(f"That's {display_name} and you are {author_name}")

    @commands.command()
    async def profile(self,ctx):
        filename  = "pfp.png"
        filename2 = "pfp2.png"
        author = ctx.author
        author_pfp = author.display_avatar
        display_pfp = ctx.message.mentions[0].display_avatar
        await author_pfp.save(filename)
        await display_pfp.save(filename2)
        await ctx.send("file saved")
        #os.remove(filename)
    

async def setup(bot):
    await bot.add_cog(Minigame(bot))








        
'''
    @bot.command()
    async def extract(ctx):
        image = 'maps/haggle.png'
        file = discord.File(image)
        channel_id = bot.get_channel(1165731670524166184)
        message = await channel_id.send(file=file)
        image_url = message.attachments[0].url
        await ctx.send(image_url)


'''

    

 