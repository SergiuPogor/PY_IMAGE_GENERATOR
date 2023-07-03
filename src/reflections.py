from PIL import ImageFilter

from main import *

# Load image
image = Image.open("original_image.jpg")

# Get width and height
width, height = image.size

# Create a new image with double the height to hold the reflection
reflection = Image.new('RGBA', (width, height * 2), (255, 255, 255, 0))

# Paste the original image into the reflection
reflection.paste(image, (0, 0))

# Flip the reflection image vertically
reflection = reflection.transpose(Image.FLIP_TOP_BOTTOM)

# Draw a gradient mask on the reflection to fade it out
gradient = Image.new('L', (width, height * 2), 0)
draw = ImageDraw.Draw(gradient)
draw.rectangle((0, height // 2, width, height * 2), fill=255)
gradient = gradient.filter(ImageFilter.GaussianBlur(radius=10))
reflection.putalpha(gradient)

# Paste the reflection back onto the original image with a lowered opacity
image.paste(reflection, (0, height), mask=reflection)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
