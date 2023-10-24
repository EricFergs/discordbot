from PIL import Image, ImageDraw, ImageFont
from maps import matcher
from cogs import moves
import requests
from io import BytesIO

def make_graphic(Map1, Map2, mode, rotation_time):
  background = Image.open('misc/background.png')
  map1 = Image.open('maps/' + matcher.map_mapping[Map1])
  map2 = Image.open('maps/' + matcher.map_mapping[Map2])
  percentage = 80
  map1_width, map1_height = map1.size
  new_width = int(map1_width * (percentage / 100))
  new_height = int(map1_height * (percentage / 100))
  resized_map1 = map1.resize((new_width, new_height))
  resized_map2 = map2.resize((new_width, new_height))

  background.paste(resized_map1, (0,665))
  background.paste(resized_map2, (0,320))

  draw = ImageDraw.Draw(background)
  text = mode
  font_size = 100
  myFont = ImageFont.truetype('Splatoon1.ttf', 60)
  if(mode == "Turf war"):
    text_color = (144, 238, 144)  
    position = (130,40)
  else:
    text_color = (204, 85, 0) 
    position = (60,40)
  draw.text(position, text, fill=text_color, font=myFont)
  #//
  draw = ImageDraw.Draw(background)
  text = rotation_time
  font_size = 100
  myFont = ImageFont.truetype('Splatoon1.ttf', 30)
  text_color = (0, 0, 0) 
  position = (90,220)
  draw.text(position, text, fill=text_color, font=myFont)
  background.save("final.png")
  return ("final.png")


def resize(img):
  response = requests.get(img)
  image = Image.open(BytesIO(response.content))
  desired_size = (130, 130)
  image = image.convert('RGBA')
  image.thumbnail(desired_size)
  return image




def fight_scene(profile1, profile2):
  background = Image.open('misc/bg.png').convert('RGBA')
  profile1 = Image.open(moves.pfps[profile1]).convert('RGBA')
  profile2 = Image.open(moves.pfps[profile2]).convert('RGBA')
  background.paste(profile2,(200,50))
  background.paste(profile1,(-10,50))
  background.save('fight.png')


