from main import *

# Example usage
image_width = WIDTH
image_height = HEIGHT

transparent_image = generate_transparent_image(image_width, image_height)

center_x = image_width // 2
center_y = image_height // 2
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

    # Generate random colors for the gradient effect
    start_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    end_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Create a linear gradient from start_color to end_color
    for j in range(border_size):
        ratio = j / border_size
        interpolated_color = tuple(int(start + (end - start) * ratio) for start, end in zip(start_color, end_color))

        circle_radius_j = circle_radius + j
        transparent_image = generate_circle(transparent_image, circle_center_x, circle_center_y, circle_radius_j, 1, interpolated_color)

final_filename = '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
make_dir_if_not_exist(final_filename)

# Save the image
transparent_image.save(final_filename, "PNG")

print(Fore.MAGENTA + '{}'.format(TIMESTAMP), Fore.WHITE + '{}'.format(final_filename))
