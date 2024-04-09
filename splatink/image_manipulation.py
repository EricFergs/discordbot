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

def make_salmon(rotations):
    background = Image.open(graybg)
    y_offset = 100
    idx = 0
    for rotation in rotations:
        stage = Image.open(salmaps + salmatcher.salmon_mapping[rotation.map])
        percentage = 50
        stage = stage.resize((int(stage.width * (percentage / 100)), int(stage.height * (percentage / 100))))

        x_offset = stage.width

        boss = Image.open(bosses + bossmatcher.boss_mapping[rotation.boss])
        boss = boss.convert("RGBA")
        boss = boss.resize((int(boss.width*0.5), int(boss.height*0.5)), Image.ANTIALIAS)

        weapons_images = []
        for weapon in [rotation.weapon1, rotation.weapon2, rotation.weapon3, rotation.weapon4]:
            weapon_img = Image.open(weapons + weaponmatcher.weapon_mapping[weapon])
            weapon_img = weapon_img.convert("RGBA")
            weapon_img = weapon_img.resize((int(weapon_img.width*0.5), int(weapon_img.height*0.5)), Image.ANTIALIAS)
            weapons_images.append(weapon_img)

        background.paste(stage, (0, (idx) * stage.height))
        background.paste(boss, (x_offset, int((idx) * (stage.height))), boss)
        x_offset += 200  # Adjust x offset for next boss image
        for weapon_img in weapons_images:
            background.paste(weapon_img, (x_offset, int((idx) * (stage.height) + (stage.height/2) - (weapon_img.height/2))), weapon_img)
            x_offset += 100  # Adjust x offset for next weapon image
        
        draw = ImageDraw.Draw(background)
        text = rotation.start
        font_size = 30
        myFont = ImageFont.truetype(font, font_size)
        text_color = (0, 0, 0)
        draw.text((boss.width + stage.width, int((idx) * (stage.height))), text, fill=text_color, font=myFont)
        idx += 1

    background.save("final.png")
    return "final.png"


