from main import *

# Image size
width = WIDTH
height = HEIGHT

# Create image
image = generate_image(width=width, height=height)
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Define the number of drips and their width range
num_drips = random.randint(50, 500)
min_drip_width = 10
max_drip_width = 50

# Loop through the number of drips and draw them randomly across the image
for i in range(num_drips):
    # Choose a random color for the drip
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Choose a random width for the drip
    drip_width = random.randint(min_drip_width, max_drip_width)

    # Choose a random starting location for the drip
    start_x = random.randint(0, width)
    start_y = random.randint(0, height)

    # Draw the drip as a series of concentric ellipses, with each ellipse slightly smaller than the last
    for j in range(drip_width):
        draw.ellipse((start_x - j, start_y - j, start_x + j, start_y + j), fill=color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
