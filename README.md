Flappy Deluxe

A lightweight Flappy Bird-inspired game built entirely with Python and Tkinter. The project focuses on implementing a complete 2D game loop, physics, collision detection, procedural obstacles, animated environments, and interactive menus without relying on third-party game engines or external dependencies.

Overview

Flappy Bird Deluxe recreates the core mechanics of the classic arcade-style game while adding customizable environments, multiple difficulty levels, a pause system, particle effects, and a more detailed user interface.

The project is intentionally implemented as a standalone Python application using Tkinter's Canvas, making the source code easy to run, inspect, and modify.

Features
Gameplay

Flappy Bird-style physics and controls

Gravity-based movement

Adjustable flap strength

Procedurally generated pipes

Collision detection

Score tracking

High-score tracking

Three difficulty levels

Game-over and restart system

Smooth game loop

Visuals

Custom vector-style graphics rendered with Tkinter

Detailed pipe designs with highlights and shadows

Animated bird

Animated wings

Scrolling ground

Moving clouds

Background mountains

Sun and moon

Night-time stars

Particle effects

Multiple visual themes

User Interface

Main menu

Pause menu

Settings menu

Game-over screen

Score display

High-score display

Interactive buttons

Keyboard and mouse controls

Customization

The game currently includes five sky themes:

Classic

Sunset

Ocean

Night

Lavender

Difficulty can also be configured:

Difficulty	Characteristics
Easy	Larger gaps, slower movement, lighter physics
Normal	Balanced gameplay
Hard	Smaller gaps, faster movement, stronger gravity
Requirements

Python 3.x

Tkinter

Tkinter is included with most standard Python installations.

No external Python packages are required.

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/flappy-bird-deluxe.git


Navigate to the project directory:

cd flappy-bird-deluxe


Run the game:

python flappybird.py

Windows

On Windows systems with the Python launcher installed:

py flappybird.py

Controls
Input	Action
Space	Flap
Left Mouse Button	Flap
P	Pause / Resume
Esc	Pause / Resume
R	Restart after game over
Left Arrow	Previous sky theme
Right Arrow	Next sky theme
A	Decrease difficulty
D	Increase difficulty
Project Structure
flappy-bird-deluxe/
│
├── flappybird.py
├── README.md
├── LICENSE
└── screenshots/
    ├── menu.png
    ├── gameplay.png
    ├── pause.png
    ├── settings.png
    └── gameover.png


The core game is contained in flappybird.py, allowing the project to remain simple and portable.

Architecture

The game is built around a continuous update and rendering loop.

Input
  │
  ▼
Game State
  │
  ▼
Physics & Movement
  │
  ▼
Collision Detection
  │
  ▼
Score & Gameplay Events
  │
  ▼
Particle / Environment Updates
  │
  ▼
Rendering
  │
  └──────────────► Next Frame


The application maintains several game states:

TITLE
PLAYING
PAUSED
SETTINGS
GAME_OVER


This state-based structure separates menus and gameplay while allowing the same rendering loop to manage the entire application.

Technical Details
Physics

The bird uses simple velocity-based physics.

Gravity continuously increases the bird's vertical velocity:

bird_velocity += gravity
bird_y += bird_velocity


Flapping applies an upward impulse:

bird_velocity = flap_strength


The physics parameters are configurable through the difficulty system.

Procedural Pipes

Pipe gaps are generated dynamically using randomized vertical positions.

Each pipe contains:

Horizontal position

Gap position

Gap size

Scoring state

Pipes move toward the player each frame:

pipe["x"] -= pipe_speed


Pipes that leave the screen are removed to prevent unnecessary accumulation of objects.

Collision Detection

Collision detection checks the bird against:

The top boundary

The ground

Upper pipes

Lower pipes

A collision transitions the game into the GAME_OVER state.

Rendering

Graphics are rendered using Tkinter's Canvas primitives, including:

Rectangles

Ovals

Polygons

Lines

Text

No image assets are required for the core game.

This makes the project particularly useful for experimenting with procedural 2D graphics in Python.

Customization

The game's behavior can be modified directly in flappybird.py.

For example, the game window is configured using:

WIDTH = 600
HEIGHT = 800


Physics can be adjusted through:

gravity = 0.5
flap_strength = -9
pipe_speed = 4
pipe_gap = 175


Additional themes can be added to the SKY_THEMES dictionary without changing the rendering system.

Screenshots

Add screenshots of the game to the screenshots/ directory and reference them here:

![Main Menu](screenshots/menu.png)

![Gameplay](screenshots/gameplay.png)

![Settings](screenshots/settings.png)

![Game Over](screenshots/gameover.png)

Roadmap

Potential future improvements include:

Sound effects

Background music

Persistent high scores

Collectible coins

Unlockable bird skins

Additional environment themes

Weather effects

Achievement system

Statistics screen

Controller support

Improved animation system

Saveable configuration

Additional game modes

Contributing

Contributions are welcome.

To contribute:

Fork the repository.

Create a feature branch.

git checkout -b feature/your-feature


Make and test your changes.

Commit your changes.

git commit -m "Add your feature"


Push the branch.

git push origin feature/your-feature


Open a Pull Request.

When submitting changes, please keep the project dependency-free where practical and maintain compatibility with supported Python versions.

Bug Reports

If you encounter an issue, open a GitHub Issue and include:

Operating system

Python version

Steps to reproduce the issue

Expected behavior

Actual behavior

Relevant traceback or error message

Example:

Operating System: Windows 11
Python: 3.14

Description:
The game crashes when opening the settings menu.

Error:
[paste traceback here]

License

This project is released under the MIT License. See LICENSE for details.

Disclaimer

This is an independent game inspired by the gameplay concept of Flappy Bird. It is not affiliated with, sponsored by, or endorsed by the original Flappy Bird developers or rights holders.

Acknowledgements

Built with:

Python

Tkinter

No third-party game engine is required.

Flappy Bird Deluxe — a small Python project demonstrating game development fundamentals with Tkinter.
