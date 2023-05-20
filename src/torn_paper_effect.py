from main import *

# Image size
width = WIDTH
height = HEIGHT

# Color of torn edges
edge_color = (255, 255, 255, 255)

# Create a blank image
image = Image.new(mode='RGBA', size=(width, height), color=(0, 0, 0, 0))

# Draw a rectangle with jagged edges
draw = ImageDraw.Draw(image)
x1, y1, x2, y2 = 50, 50, 450, 450
edge_width = 20
draw.line((x1, y1 + edge_width, x1, y1, x1 + edge_width, y1), fill=edge_color, width=edge_width)
draw.line((x2 - edge_width, y2, x2, y2, x2, y2 - edge_width), fill=edge_color, width=edge_width)
draw.line((x2, y1 + edge_width, x2, y2, x2 - edge_width, y2), fill=edge_color, width=edge_width)
draw.line((x1 + edge_width, y1, x2 - edge_width, y1, x2, y1 + edge_width, x2, y1), fill=edge_color, width=edge_width)
draw.line((x1, y2 - edge_width, x1 + edge_width, y2, x2 - edge_width, y2, x1, y2), fill=edge_color, width=edge_width)

# Add texture image underneath torn edges
texture_image = Image.open('texture.png')
image.paste(texture_image, mask=texture_image)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
