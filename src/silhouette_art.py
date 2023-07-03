from main import *

# Image size
WIDTH = 600
HEIGHT = 400

# Create a new Image object
image = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 255, 255))

# Create a new ImageDraw object
draw = ImageDraw.Draw(image)

# Define the silhouette color
SILHOUETTE_COLOR = (0, 0, 0)

# Define the background color
BACKGROUND_COLOR = (255, 0, 0)

# Draw a silhouette
draw.rectangle((150, 100, 450, 300), fill=SILHOUETTE_COLOR)

# Draw the background
draw.rectangle((0, 0, WIDTH, HEIGHT), fill=BACKGROUND_COLOR)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))

