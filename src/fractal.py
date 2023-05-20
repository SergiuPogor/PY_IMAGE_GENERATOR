from PIL import Image

# Fractal parameters
width = 800
height = 800
max_iterations = 1000
zoom = 1.0
x_offset = -0.5
y_offset = 0.0

# Create a blank image
image = Image.new("RGB", (width, height), (0, 0, 0))
pixels = image.load()

# Generate the Mandelbrot fractal
for x in range(width):
    for y in range(height):
        zx, zy = 0.0, 0.0
        cx = (x - width / 2) / (0.5 * zoom * width) + x_offset
        cy = (y - height / 2) / (0.5 * zoom * height) + y_offset

        iteration = 0
        while zx * zx + zy * zy < 4 and iteration < max_iterations:
            zx, zy = zx * zx - zy * zy + cx, 2 * zx * zy + cy
            iteration += 1

        color = (iteration % 8 * 32, iteration % 16 * 16, iteration % 32 * 8)
        pixels[x, y] = color

# Save the fractal image
image.save("mandelbrot_fractal.png", "PNG")
