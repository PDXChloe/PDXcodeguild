
#Draw a stick figure
from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

color = (256, 128, 128)  # pink
# draw.line((0, 0, width, height), fill=color)
draw.line((200, 400, 250, 300, 300, 400), fill=color)
draw.line((250, 300, 250, 200), fill=color)
draw.line((300, 200, 200, 200), fill=color)
draw.ellipse((200, 100, 300, 200), fill=color)

img.show()