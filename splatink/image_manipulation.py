from PIL import Image, ImageDraw, ImageFont
from db.maps.online_maps import matcher
from db.maps.salmon_maps import salmatcher
from db.bosses import bossmatcher
from db.weps import weaponmatcher
from db.mode import modematcher


#database references
db = 'db/'
misc = db + 'misc/background.png'
graybg = db + 'misc/graybg.jpg'

maps = db + 'maps/online_maps/'
salmaps = db + 'maps/salmon_maps/'
bosses = db + 'bosses/'
weapons = db + 'weps/'

modefile = db + 'mode/'
font = db + 'fonts/Splatoon1.ttf'



def make_graphic(Map1, Map2, mode, rotation_time, gamemode = None):
    # Load background image
    background = Image.open(misc)

    # Load map images
    map1 = Image.open(maps + matcher.map_mapping[Map1])
    map2 = Image.open(maps + matcher.map_mapping[Map2])
    

    # Resize map images
    percentage = 80
    map1 = map1.resize((int(map1.width * (percentage / 100)), int(map1.height * (percentage / 100))))
    map2 = map2.resize((int(map2.width * (percentage / 100)), int(map2.height * (percentage / 100))))

    # Paste map images onto the background
    background.paste(map1, (0, 665))
    background.paste(map2, (0, 320))

    if gamemode:
        gamemode = Image.open(modefile + modematcher.mode_mapping[gamemode]).convert("RGBA")
        background.paste(gamemode,(0,185),mask=gamemode)
    # Create a drawing context
    draw = ImageDraw.Draw(background)

    # Add mode text
    text = mode
    font_size = 60
    myFont = ImageFont.truetype(font, font_size)

    if mode == "Turf war":
        text_color = (144, 238, 144)
    elif mode == "X":
        text_color = (16, 219, 155)
        text = "X battles"
    else:
        text_color = (204, 85, 0)
    
    font_width = myFont.getsize(text)[0]
    position = (background.width - font_width) / 2
    draw.text((position, 40), text, fill=text_color, font=myFont)

    # Add rotation time text
    text = rotation_time
    font_size = 30
    myFont = ImageFont.truetype(font, font_size)
    text_color = (0, 0, 0)
    font_width = myFont.getsize(text)[0]
    position = (background.width - font_width) / 2
    draw.text((position, 220), text, fill=text_color, font=myFont)

    # Save the final image
    background.save("final.png")

    return "final.png"

def make_salmon(map, boss, w1, w2, w3, w4, rotation_time):
    background = Image.open(graybg)

    stage = Image.open(salmaps + salmatcher.salmon_mapping[map])
    percentage = 80
    stage = stage.resize((int(stage.width * (percentage / 100)), int(stage.height * (percentage / 100))))

    boss = Image.open(bosses + bossmatcher.boss_mapping[boss])
    boss = boss.convert("RGBA")
    boss = boss.resize((boss.width, boss.height), Image.ANTIALIAS)

    wep1 = Image.open(weapons + weaponmatcher.weapon_mapping[w1])
    wep1 = wep1.convert("RGBA")
    wep1 = wep1.resize((wep1.width, wep1.height), Image.ANTIALIAS)

    wep2 = Image.open(weapons + weaponmatcher.weapon_mapping[w2])
    wep2 = wep2.convert("RGBA")
    wep2 = wep2.resize((wep2.width, wep2.height), Image.ANTIALIAS)

    wep3 = Image.open(weapons + weaponmatcher.weapon_mapping[w3])
    wep3 = wep3.convert("RGBA")
    wep3 = wep3.resize((wep3.width, wep3.height), Image.ANTIALIAS)

    wep4 = Image.open(weapons + weaponmatcher.weapon_mapping[w4])
    wep4 = wep4.convert("RGBA")
    wep4 = wep4.resize((wep4.width, wep4.height), Image.ANTIALIAS)

    background.paste(stage, (0, 0))
    background.paste(boss, (100, 100), boss)
    background.paste(wep1, (500, 500), wep1)
    background.paste(wep2, (550, 500), wep2)
    background.paste(wep3, (600, 500), wep3)
    background.paste(wep4, (650, 500), wep4)

    background.save("final.png")

    return "final.png"

