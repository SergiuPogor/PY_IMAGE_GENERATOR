from main import *
from main.ImageGenerator import *

# Example usage
image_width = 5000
image_height = 5000
transparent_image = generate_transparent_image(image_width, image_height)

center_x = image_width / 2
center_y = image_height / 2
circle_radius = 1000
border_size = int(circle_radius / 100)

num_circles = 100
angle_step = 360 / num_circles

for i in range(num_circles):
    angle = math.radians(angle_step * i)
    offset_x = int(circle_radius * math.cos(angle))
    offset_y = int(circle_radius * math.sin(angle))
    circle_center_x = center_x + offset_x
    circle_center_y = center_y + offset_y

    # Vary the color for each circle
    # circle_color = (255, 0, 0, int(255 * (i + 1) / num_circles))
    circle_color = (random.randint(0, 255), int(255 * (i + 1) / num_circles), int(255 * (i + 1) / num_circles))

    transparent_image = generate_circle(transparent_image, circle_center_x, circle_center_y, circle_radius, border_size, circle_color)

final_filename = '{}{}/data/output/images/{}.png'.format(MEDIA_PATH, APP_NAME, datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
make_dir_if_not_exist(final_filename)

# Save the image
transparent_image.save(final_filename, "PNG")

print(Fore.MAGENTA + '{}'.format(TIMESTAMP), Fore.WHITE + '{}'.format(final_filename))
