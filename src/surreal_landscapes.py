from main import *

# Image size
width = 800
height = 600

image = Image.new('RGBA', (width, height), (255, 255, 255, 255))
draw = ImageDraw.Draw(image)

# Calculate the central point of the image
center_x = width // 2
center_y = height // 2

# Draw the sky background
draw.rectangle((0, 0, width, height // 2), fill=(135, 206, 235, 255))

# Draw the ground
ground_color = (126, 200, 80, 255)
ground_top_y = height // 2
ground_bottom_y = 3 * height // 4
draw.rectangle((0, ground_top_y, width, ground_bottom_y), fill=ground_color)

# Draw a sun
sun_radius = 80
sun_center = (center_x - 200, center_y - 200)
draw.ellipse((sun_center[0] - sun_radius, sun_center[1] - sun_radius, sun_center[0] + sun_radius, sun_center[1] + sun_radius), fill=(255, 255, 0, 255))

# Draw a tree
tree_color = (89, 37, 20, 255)
tree_top_x = center_x + 100
tree_top_y = ground_top_y - 150
tree_bottom_x = center_x + 50
tree_bottom_y = ground_top_y
draw.rectangle((tree_top_x, tree_top_y, tree_bottom_x, tree_bottom_y), fill=tree_color)

# Draw a bird
bird_color = (255, 255, 255, 255)
bird_x = center_x + 200
bird_y = center_y - 100
bird_size = 40
draw.ellipse((bird_x - bird_size, bird_y - bird_size, bird_x + bird_size, bird_y + bird_size), fill=bird_color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
