from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height, color=(255, 255, 255, 255))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Create the circuitry pattern
num_lines = random.randint(20, 100)
for i in range(num_lines):
    # Choose a random start point and end point
    start_x = random.randint(0, width)
    start_y = random.randint(0, height)
    end_x = random.randint(0, width)
    end_y = random.randint(0, height)

    # Draw the line
    draw.line((start_x, start_y, end_x, end_y), width=random.randint(1, 10), fill=generate_random_color())

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
