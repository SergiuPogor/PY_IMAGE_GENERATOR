from PIL import ImageFont

from main import *

# Image size
width = WIDTH
height = HEIGHT

# Font options
fonts = ['arial.ttf', 'arial.ttf', 'arial.ttf']
font_sizes = [20, 30, 40, 50]

# Characters to choose from
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=[]{}|;:,.<>?'

image = generate_image(width=width, height=height, color=(255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Algorithm logic here
for _ in range(50):
    char = random.choice(characters)
    font = ImageFont.truetype(random.choice(fonts), random.choice(font_sizes))
    x = random.randint(0, width)
    y = random.randint(0, height)
    angle = random.randint(0, 360)
    draw.text((x, y), char, font=font, fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), stroke_width=1, stroke_fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), align='center', spacing=0, direction=None, features=None, language=None, stroke_width_ratio=0.05, stroke_miterlimit=10, align_shift=None, anchor=None, features_data=None, fit=None, fill_opacity=None, stroke_opacity=None, xy=None, stroke_xy=None, font_metrics=None, stroke_width_method=None, blend=None, underline=None, encoding=None, url=None)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
