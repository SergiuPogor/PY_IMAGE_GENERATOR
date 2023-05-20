from main import *

# Image size
width = WIDTH
height = HEIGHT

image = generate_image(width=width, height=height)
draw = ImageDraw.Draw(image)

# Initial position and velocity of the point
x = random.randint(0, width)
y = random.randint(0, height)
vx = random.uniform(-5, 5)
vy = random.uniform(-5, 5)

# Algorithm logic here
for i in range(width):
    # Calculate the position of the point in the next frame
    x += vx
    y += vy

    # Adjust velocity randomly
    vx *= random.uniform(0.9, 1.1)
    vy *= random.uniform(0.9, 1.1)

    # Draw a line from the previous position to the current position
    draw.line((x, y, x - vx, y - vy), fill=generate_random_color(), width=100)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
