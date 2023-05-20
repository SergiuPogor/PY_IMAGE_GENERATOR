import os
import sys
import math
import os.path
import random

from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw
from colorama import Fore
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env file

MEDIA_PATH = os.environ.get('MEDIA_PATH')

WIDTH = int(os.environ.get('WIDTH'))
HEIGHT = int(os.environ.get('HEIGHT'))

PROJECT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))

# Get the absolute path of the current app (i.e. the parent directory of the parent directory of the script)
APP_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/'

# script_path = os.path.realpath(__file__)
APP_NAME = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

TIMESTAMP = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

print()
print(Fore.MAGENTA + '{}'.format(TIMESTAMP), Fore.WHITE + 'START')


def make_dir_if_not_exist(file_path):
    dir_path = os.path.dirname(file_path)
    path_to_dir = Path(dir_path)
    path_to_dir.mkdir(parents=True, exist_ok=True)


def generate_transparent_image(width, height):
    # Create a new image with transparent background
    return Image.new("RGBA", (width, height), (0, 0, 0, 0))


def generate_circle(image, center_x, center_y, radius, border_size, color):
    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Calculate the bounding box for the circle
    bounding_box = [(center_x - radius, center_y - radius), (center_x + radius, center_y + radius)]

    # Draw the circle with the specified border size
    draw.ellipse(bounding_box, outline=color, width=border_size)

    return image
