from main import *

# Image size
width = WIDTH
height = HEIGHT

# Specify colors
# colors = [(178, 34, 34), (255, 69, 0), (255, 215, 0), (50, 205, 50), (0, 191, 255), (128, 0, 128)]
colors = []
for i in range(1, random.randint(5, 50)):
    colors.append(generate_random_color())

# Create image
image = generate_image(width=width, height=height)
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Loop through the colors and interpolate between them to create a gradient effect
for i in range(len(colors) - 1):
    # Calculate the start and end points for this segment of the gradient
    start_x = int(center_x * (i / (len(colors) - 1)))
    start_y = int(center_y * (i / (len(colors) - 1)))
    end_x = int(center_x * ((i + 1) / (len(colors) - 1)))
    end_y = int(center_y * ((i + 1) / (len(colors) - 1)))

    # Create a linear gradient between the two colors
    for j in range(start_x, end_x):
        # Interpolate the color
        red = int(colors[i][0] + (colors[i + 1][0] - colors[i][0]) * ((j - start_x) / (end_x - start_x)))
        green = int(colors[i][1] + (colors[i + 1][1] - colors[i][1]) * ((j - start_x) / (end_x - start_x)))
        blue = int(colors[i][2] + (colors[i + 1][2] - colors[i][2]) * ((j - start_x) / (end_x - start_x)))
        color = (red, green, blue)

        # Draw a vertical line of this color
        draw.line((j, start_y, j, end_y), fill=color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
