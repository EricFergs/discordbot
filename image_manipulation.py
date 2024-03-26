from PIL import Image, ImageDraw, ImageFont
from maps import matcher
from mode import modematcher

def make_graphic(Map1, Map2, mode, rotation_time, gamemode = None):
    # Load background image
    background = Image.open('misc/background.png')

    # Load map images
    map1 = Image.open('maps/' + matcher.map_mapping[Map1])
    map2 = Image.open('maps/' + matcher.map_mapping[Map2])
    

    # Resize map images
    percentage = 80
    map1 = map1.resize((int(map1.width * (percentage / 100)), int(map1.height * (percentage / 100))))
    map2 = map2.resize((int(map2.width * (percentage / 100)), int(map2.height * (percentage / 100))))

    # Paste map images onto the background
    background.paste(map1, (0, 665))
    background.paste(map2, (0, 320))

    if gamemode:
        gamemode = Image.open('mode/'+ modematcher.mode_mapping[gamemode]).convert("RGBA")
        background.paste(gamemode,(0,185),mask=gamemode)
    # Create a drawing context
    draw = ImageDraw.Draw(background)

    # Add mode text
    text = mode
    font_size = 60
    myFont = ImageFont.truetype('Splatoon1.ttf', font_size)

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
    myFont = ImageFont.truetype('Splatoon1.ttf', font_size)
    text_color = (0, 0, 0)
    font_width = myFont.getsize(text)[0]
    position = (background.width - font_width) / 2
    draw.text((position, 220), text, fill=text_color, font=myFont)

    # Save the final image
    background.save("final.png")

    return "final.png"
