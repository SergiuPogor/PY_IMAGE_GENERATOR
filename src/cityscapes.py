from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height)
draw = ImageDraw.Draw(image)

# Define color palette
background_color = (255, 255, 255)
building_colors = [(29, 145, 192), (100, 181, 246), (56, 102, 193), (44, 58, 70)]
window_colors = [(239, 83, 80), (156, 39, 176), (33, 150, 243), (103, 58, 183), (205, 220, 57), (255, 152, 0)]

# Draw background
draw.rectangle((0, 0, width, height), fill=background_color)

# Draw buildings
for i in range(20):
    x = random.randint(0, width)
    y = random.randint(0, height // 2)
    height_ratio = random.uniform(0.5, 2)
    building_color = random.choice(building_colors)
    building_height = int(height * height_ratio)
    draw.rectangle((x, y, x + 200, y + building_height), fill=building_color)

    # Draw windows
    window_size = random.randint(5, 10)
    for j in range(10):
        window_x = random.randint(x + 10, x + 190)
        window_y = random.randint(y + 10, y + building_height - 10)
        window_color = random.choice(window_colors)
        draw.rectangle((window_x, window_y, window_x + window_size, window_y + window_size), fill=window_color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
