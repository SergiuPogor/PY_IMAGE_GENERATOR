from main import *

# Image size
width = WIDTH
height = HEIGHT
tile_size = 20
tiles_per_row = width // tile_size

image = generate_image(width=width, height=height)
draw = ImageDraw.Draw(image)

color_choices = [generate_random_color(), generate_random_color(), generate_random_color()]

for y in range(height // tile_size):
    for x in range(tiles_per_row):
        tile_color = random.choice(color_choices)
        tile_x = x * tile_size
        tile_y = y * tile_size
        tile_coords = (tile_x, tile_y, tile_x + tile_size, tile_y + tile_size)
        draw.rectangle(tile_coords, fill=tile_color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
