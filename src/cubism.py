from main import *

# Image size
width = WIDTH
height = HEIGHT

# Color palette
COLORS = [(255, 255, 255), (0, 0, 0), (128, 128, 128), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]


# Helper function to create randomized colors
def get_rand_color():
    return random.choice(COLORS)


# Helper function to create a random polygon
def get_rand_polygon(width, height):
    points = []
    for _ in range(3):
        x = random.randint(0, width)
        y = random.randint(0, height)
        points.append((x, y))
    return points


# Image generation function
def generate_cubist_image(width, height):
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Calculate the central point of the image
    center_x = width // 2
    center_y = height // 2

    # Draw the outlines of random polygons
    for i in range(10):
        color = get_rand_color()
        draw.line(get_rand_polygon(width, height), fill=color, width=3)

    # Draw the overlapping shapes
    for i in range(10):
        color = get_rand_color()
        points = get_rand_polygon(width, height)
        draw.polygon(points, fill=color)
        draw.line(points + [points[0]], fill=color, width=3)

    # Save Image to a local file
    save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))


generate_cubist_image(WIDTH, HEIGHT)
