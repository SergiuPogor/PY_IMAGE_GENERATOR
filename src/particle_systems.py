import random

from PIL import Image, ImageDraw

from main import *

# Particle system parameters
width = WIDTH
height = HEIGHT
num_particles = 100
max_velocity = 50
gravity = 0.2

# Create a blank image
image = generate_image(width, height)
draw = ImageDraw.Draw(image)

# Define the Particle class
class Particle:
    def __init__(self, position, velocity, size):
        self.position = position
        self.velocity = velocity
        self.size = size

    def update(self):
        self.velocity += gravity  # Apply gravity
        self.position += self.velocity

    def draw(self, outline):
        bounding_box = [
            (self.position.x - self.size, self.position.y - self.size),
            (self.position.x + self.size, self.position.y + self.size)
        ]
        draw.rectangle(bounding_box, outline=outline)

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector2D(self.x + other, self.y + other)
        else:
            raise TypeError("Unsupported operand type for +: {}".format(type(other)))

    def __iadd__(self, other):
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
        else:
            raise TypeError("Unsupported operand type for +=: {}".format(type(other)))
        return self

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector2D(self.x - other, self.y - other)
        else:
            raise TypeError("Unsupported operand type for -: {}".format(type(other)))

    def __isub__(self, other):
        if isinstance(other, Vector2D):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, (int, float)):
            self.x -= other
            self.y -= other
        else:
            raise TypeError("Unsupported operand type for -=: {}".format(type(other)))
        return self

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Unsupported operand type for *: {}".format(type(scalar)))

    def __imul__(self, scalar):
        if isinstance(scalar, (int, float)):
            self.x *= scalar
            self.y *= scalar
        else:
            raise TypeError("Unsupported operand type for *=: {}".format(type(scalar)))
        return self

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


# Generate random particles
particles = []
for _ in range(num_particles):
    position = Vector2D(random.randint(0, width), random.randint(0, height))
    velocity = Vector2D(random.uniform(-max_velocity, max_velocity), random.uniform(-max_velocity, max_velocity))
    size = random.randint(10, 50)  # Adjust the size range as desired
    particle = Particle(position, velocity, size)
    particles.append(particle)

color = generate_random_color()

# Simulate the particle system
for _ in range(1000):
    for particle in particles:
        particle.update()
        particle.draw(color)

final_filename = '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
make_dir_if_not_exist(final_filename)

# Save the image
image.save(final_filename, "PNG")

print(Fore.MAGENTA + '{}'.format(TIMESTAMP), Fore.WHITE + '{}'.format(final_filename))
