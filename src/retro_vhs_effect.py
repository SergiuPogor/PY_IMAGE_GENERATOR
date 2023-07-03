from main import *

# Image size
width = 640
height = 480

# Generate image
image = Image.new("RGBA", (width, height), color=(0, 0, 0, 0))

# Define scan line parameters
scan_line_opacity = 60  # Scan line opacity
scan_line_width = 2  # Scan line width
scan_line_gap = 2  # Scan line gap

# Define noise parameters
noise_opacity = 20  # Noise opacity

# Define color aberration parameters
color_offset = 10  # Color offset in pixels
color_aberration_opacity = 50  # Color aberration opacity

# Add scan lines
for y in range(0, height, scan_line_width + scan_line_gap):
    draw = ImageDraw.Draw(image)
    draw.line((0, y, width, y), fill=(255, 255, 255, scan_line_opacity), width=scan_line_width)

# Add noise
for x in range(width):
    for y in range(height):
        noise_color = random.randint(0, noise_opacity)
        image.putpixel((x, y), (noise_color, noise_color, noise_color, noise_opacity))

# Add color aberration
for x in range(width):
    for y in range(height):
        if x < (width - color_offset) and y < (height - color_offset):
            r, g, b, a = image.getpixel((x + color_offset, y + color_offset))
            image.putpixel((x, y), (r, 0, 0, color_aberration_opacity))
            image.putpixel((x + color_offset, y + color_offset), (0, g, 0, color_aberration_opacity))
            image.putpixel((x + color_offset, y), (0, 0, b, color_aberration_opacity))

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
