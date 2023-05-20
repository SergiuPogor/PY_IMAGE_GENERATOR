from main import *

# Image size
width = 600
height = 400

image = generate_image(width=width, height=height, color=(255, 255, 255, 255))
draw = ImageDraw.Draw(image)

# Create polygons with just their outlines
points = [(100, 100), (200, 100), (150, 200), (300, 150), (350, 250), (250, 300), (200, 250), (100, 300), ]
draw.polygon(points, fill=None, outline=(0, 0, 0, 255))
draw.line(points[0:2], fill=(0, 0, 0, 255), width=1)
draw.line(points[1:3], fill=(0, 0, 0, 255), width=1)
draw.line(points[2:4], fill=(0, 0, 0, 255), width=1)
draw.line(points[3:5], fill=(0, 0, 0, 255), width=1)
draw.line(points[4:6], fill=(0, 0, 0, 255), width=1)
draw.line(points[5:7], fill=(0, 0, 0, 255), width=1)
draw.line(points[6:8], fill=(0, 0, 0, 255), width=1)
draw.line([points[-1], points[0]], fill=(0, 0, 0, 255), width=1)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
