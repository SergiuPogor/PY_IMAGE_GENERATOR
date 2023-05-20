import numpy as np

from main import *


def generate_glitch_art(width, height):
    # Generate random noise
    noise = np.random.rand(height, width, 3) * 255

    # Apply random transformations
    for i in range(10):
        x_offset = np.random.randint(-50, 50)
        y_offset = np.random.randint(-50, 50)
        noise = np.roll(noise, x_offset, axis=1)
        noise = np.roll(noise, y_offset, axis=0)
        noise = np.rot90(noise, np.random.randint(4))

    # Apply color shift
    r, g, b = np.roll(noise, np.random.randint(-50, 50), axis=(0, 1)).transpose((2, 0, 1))
    noise = np.array([r, g, b]).transpose((1, 2, 0))

    # Create glitched image
    image = Image.fromarray(noise.astype(np.uint8))
    draw = ImageDraw.Draw(image)

    # Save Image to a local file
    save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))

    return image


# Image size
width = WIDTH
height = HEIGHT

generate_glitch_art(width, height)
