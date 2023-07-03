import math

from main import *

# Image size
width = WIDTH
height = HEIGHT


# Function to draw a spirograph pattern
def draw_spirograph_pattern(draw, cx, cy, R, r, l):
    t = 0
    while t < 2 * math.pi:
        x = (R - r) * math.cos(t) + l * math.cos((R - r) * t / r)
        y = (R - r) * math.sin(t) - l * math.sin((R - r) * t / r)
        draw.point((cx + x, cy + y), fill=(255, 255, 255))
        t += 0.01


# Generate the image
image = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(image)
draw_spirograph_pattern(draw, WIDTH // 2, HEIGHT // 2, 150, 75, 60)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
