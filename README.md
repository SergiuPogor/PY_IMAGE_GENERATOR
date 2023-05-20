# PY_IMAGE_GENERATOR

Python Script to Generate Geometrical Images

---

## Table of Contents

- [Installation](#installation)
- [How to use](#usage)
- [Effects](#effects)
- [Support](#support)
- [Contributing](#contributing)
- [License](#license)
---

## Installation
```
pip install -r requirements.txt 
```
---

## Usage
<b>Run any examples from src/*.py</b>
```
python src/gradient_effects.py
```
---

## Effects
<details>
<summary><b> Gradient Effects </b></summary>
Instead of using a solid color for each circle, you can create gradient effects by generating random colors within a certain range and smoothly transitioning the colors from one circle to another.

    python src/gradient_effects.py

Examples:
<p align="center">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/73aecda0be76554cd85eea3a2dc66fddee817942/data/input/images/gradient_effects/2023-05-20_13-14-16.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/73aecda0be76554cd85eea3a2dc66fddee817942/data/input/images/gradient_effects/2023-05-20_13-14-22.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/73aecda0be76554cd85eea3a2dc66fddee817942/data/input/images/gradient_effects/2023-05-20_13-14-24.png" alt="">
</p>

</details>

<details>
<summary><b> Random Shapes </b></summary>
Instead of circles, you can experiment with drawing random shapes such as squares, triangles, or polygons at different positions and sizes. You can also combine multiple shapes to create more complex patterns.

    python src/random_shapes.py

Examples:
<p align="center">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/505cfbdd3c098f2c609e96a10cdb1fef45fe3d1f/data/input/images/random_shapes/2023-05-20_14-03-56.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/505cfbdd3c098f2c609e96a10cdb1fef45fe3d1f/data/input/images/random_shapes/2023-05-20_14-04-05.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/505cfbdd3c098f2c609e96a10cdb1fef45fe3d1f/data/input/images/random_shapes/2023-05-20_14-04-17.png" alt="">
</p>

</details>

<details>
<summary><b> Particle Systems </b></summary>
Simulate particle systems by generating multiple small shapes (e.g., dots) with random positions and velocities. You can add gravity or other forces to create interesting movement patterns.

    python src/particle_systems.py

Examples:
<p align="center">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/c68c539f1c3434c8b677db43d85350d3ae907e0f/data/input/images/particle_systems/2023-05-20_14-39-34.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/c68c539f1c3434c8b677db43d85350d3ae907e0f/data/input/images/particle_systems/2023-05-20_14-40-18.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/c68c539f1c3434c8b677db43d85350d3ae907e0f/data/input/images/particle_systems/2023-05-20_14-40-21.png" alt="">
</p>

</details>


<details>
<summary><b> Noise-based </b></summary>
Utilize various noise functions (e.g., Perlin noise) to create organic and natural-looking effects. You can manipulate the noise parameters to control the density, scale, and variation of the patterns.

    python src/noise_based.py

Examples:
<p align="center">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/b879a03c9e21324136753d2e13d741f692d3c5fc/data/input/images/noise_based/2023-05-20_15-44-02.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/b879a03c9e21324136753d2e13d741f692d3c5fc/data/input/images/noise_based/2023-05-20_15-47-27.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/b879a03c9e21324136753d2e13d741f692d3c5fc/data/input/images/noise_based/2023-05-20_15-48-17.png" alt="">
</p>

</details>


<details>
<summary><b> Pixel Art </b></summary>
Create pixel art by randomly coloring individual pixels on a canvas. You can define a palette of colors and randomly assign them to pixels, resulting in a retro and nostalgic visual style.

    python src/pixel_art.py

Examples:
<p align="center">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/8777f3275487302a811944ab1d1892e12e12772e/data/input/images/pixel_art/2023-05-20_15-54-26.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/8777f3275487302a811944ab1d1892e12e12772e/data/input/images/pixel_art/2023-05-20_16-01-44.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/8777f3275487302a811944ab1d1892e12e12772e/data/input/images/pixel_art/2023-05-20_16-01-49.png" alt="">
</p>

</details>



<details>
<summary><b> Fractal Trees </b></summary>
Implement a recursive algorithm to draw fractal trees. Starting from a trunk, branch out into smaller branches recursively, varying the length and angle of each branch. This creates intricate and self-repeating tree-like patterns.

    python src/fractal_trees.py

Examples:
<p align="center">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/8777f3275487302a811944ab1d1892e12e12772e/data/input/images/fractal_trees/2023-05-20_15-54-26.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/8777f3275487302a811944ab1d1892e12e12772e/data/input/images/fractal_trees/2023-05-20_16-01-44.png" alt="">
<img width=30% src="https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/raw/8777f3275487302a811944ab1d1892e12e12772e/data/input/images/fractal_trees/2023-05-20_16-01-49.png" alt="">
</p>

</details>

---

## Support

The team is always here to help you.
Happen to face an issue? Want to report a bug?
You can submit one here on GitHub using the [Issue Tracker](https://github.com/SergiuPogor/PY_IMAGE_GENERATOR/issues/new).

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create.
Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
You can also simply open an issue with the tag "feature".
Don't forget to give the project a star!
**Thanks again !!!**

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourNewFeature`)
3. Commit your Changes (`git commit -m 'Add some YourNewFeature'`)
4. Push to the Branch (`git push origin feature/YourNewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Buy Me a Coffee

This project will be always an open source, even if I don't get donations.
That being said, I know there are amazing people who may still want to donate just to show their appreciation.


<a href="https://www.buymeacoffee.com/SergiuPogor" target="_blank">
<img src="https://cdn.buymeacoffee.com/buttons/arial-orange.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>


**Thank you very much in advance !!!**


We accept donations through Ko-fi, PayPal, BTC or ETH.
You can use the buttons below to donate through your method of choice.

|   Donate With   |                      Address                       |
|:---------------:|:--------------------------------------------------:|
|      Ko-fi      |       [Click Here](https://ko-fi.com/256cub)       |
|     PayPal      | [Click Here](https://paypal.me/256cub) |
|   BTC Address   |         3MsUYeUfmpwVS2QrnRbLpCjGaVn2WDD6sj         |
|   ETH Address   |     0x10cd16ba338661d2FB683B2481f8F5000FEd5663     |

<p align="right">(<a href="#top">back to top</a>)</p>

---

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

---
