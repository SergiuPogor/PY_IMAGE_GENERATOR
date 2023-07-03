from main import *

# Image size
width = WIDTH
height = HEIGHT


def generate_rainbow_gradient(width, height, colors):
    gradient = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)
    num_colors = len(colors)
    color_step = 1 / (num_colors - 1)
    for i in range(num_colors - 1):
        start_color = colors[i]
        end_color = colors[i + 1]
        for x in range(width):
            color_pct = x / (width - 1)
            color = (int((1 - color_pct) * start_color[0] + color_pct * end_color[0]), int((1 - color_pct) * start_color[1] + color_pct * end_color[1]), int((1 - color_pct) * start_color[2] + color_pct * end_color[2]), int((1 - color_pct) * start_color[3] + color_pct * end_color[3]))
            draw.line([(x, 0), (x, height)], fill=color, width=1)
    return gradient


# Rainbow colors
RAINBOW_COLORS = [(255, 0, 0, 255),  # Red
    (255, 127, 0, 255),  # Orange
    (255, 255, 0, 255),  # Yellow
    (0, 255, 0, 255),  # Green
    (0, 0, 255, 255),  # Blue
    (127, 0, 255, 255),  # Purple
]

# Generate and save rainbow gradient image
image = generate_rainbow_gradient(WIDTH, HEIGHT, RAINBOW_COLORS)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
