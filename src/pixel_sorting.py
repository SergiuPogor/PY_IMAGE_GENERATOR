from main import *

# Image size
width = WIDTH
height = HEIGHT

# Generate image with random pixels
image = Image.new('RGB', (width, height))
pixels = image.load()
for x in range(width):
    for y in range(height):
        pixels[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Sort pixels horizontally based on their red component
for y in range(height):
    row = [pixels[x, y] for x in range(width)]
    row.sort(key=lambda p: p[0])
    for x in range(width):
        pixels[x, y] = row[x]

# Sort pixels vertically based on their green component
for x in range(width):
    column = [pixels[x, y] for y in range(height)]
    column.sort(key=lambda p: p[1])
    for y in range(height):
        pixels[x, y] = column[y]

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
