#!/usr/bin/python
#-*-encoding:utf-8-*-

"""
Add a number into your QQ user header Image
"""
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

num = "4"
shuiyin = "draw by http://fangself.com.cn"
img = Image.open("user.png")
width= 150


font_num = ImageFont.truetype("simfang.ttf",50)
font_shui_yin = ImageFont.truetype("simfang.ttf",10)
draw = ImageDraw.Draw(img)
draw.text((120,0),num,font=font_num)
draw.text((0,140),shuiyin,font=font_shui_yin)
img.save("cpy.png","png")