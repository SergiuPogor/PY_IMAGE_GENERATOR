from main import *

# Image size
width = 800
height = 600

# Colors for glitch effect
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Generate black image
image = Image.new('RGB', (width, height), (0, 0, 0))

# Draw a rectangle
rect_width = 400
rect_height = 400
rect_pos_x = (width - rect_width) // 2
rect_pos_y = (height - rect_height) // 2
rect = (rect_pos_x, rect_pos_y, rect_pos_x + rect_width, rect_pos_y + rect_height)
draw = ImageDraw.Draw(image)
draw.rectangle(rect, fill='white')

# Add glitches
for i in range(0, width, 20):
    for j in range(0, height, 20):
        if random.random() < 0.2:
            color = random.choice(colors)
            draw.rectangle([(i, j), (i + 20, j + 20)], fill=color)
        if random.random() < 0.05:
            draw.line([(i, j), (i + 20, j + 20)], fill='white')
        if random.random() < 0.05:
            draw.line([(i, j + 20), (i + 20, j)], fill='white')

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
