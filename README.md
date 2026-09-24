🐦 Flappy Bird Deluxe

A polished Flappy Bird-style game built entirely with Python and Tkinter — no Pygame, no external libraries, and no complicated setup.

Flap through increasingly challenging pipes, customize your sky, beat your high score, and try not to hit anything!






✨ Features
🎮 Gameplay

Classic Flappy Bird-style gameplay

Smooth gravity and flap physics

Randomly generated pipe gaps

Score tracking

High-score tracking

Three difficulty levels

Collision detection

Particle effects

Animated bird wings

Animated ground

Smooth scrolling gameplay

🎨 Visuals

Fully drawn using Tkinter Canvas

Detailed pipes with:

Highlights

Shadows

Caps

Decorative bolts

Custom bird graphics

Animated clouds

Mountains in the background

Sun and moon

Twinkling stars

Multiple sky themes

Animated grass and ground details

⚙️ Settings

Choose between several visual themes:

☀️ Classic

🌅 Sunset

🌊 Ocean

🌙 Night

💜 Lavender

Choose your difficulty:

Difficulty	Description
🟢 Easy	Larger gaps and slower pipes
🔵 Normal	Balanced classic gameplay
🔴 Hard	Smaller gaps and faster pipes
⏸️ Pause Menu

Press P or Esc during gameplay to open the pause menu.

From there you can:

Resume the game

Open settings

Return to the main menu

🕹️ Controls
Key / Input	Action
SPACE	Flap
LEFT CLICK	Flap
P	Pause
ESC	Pause
R	Restart after game over
←	Previous sky
→	Next sky
A	Easier difficulty
D	Harder difficulty
📸 Screenshots

Add screenshots of your game here:

screenshots/
├── menu.png
├── gameplay.png
├── pause.png
├── settings.png
└── gameover.png


Then you can display them in the README:

![Main Menu](screenshots/menu.png)

![Gameplay](screenshots/gameplay.png)

![Settings](screenshots/settings.png)

🚀 Getting Started
Requirements

You only need:

Python 3.x

Tkinter

Tkinter is included with most standard Python installations.

No Pygame installation is required.

1. Clone the repository
git clone https://github.com/YOUR_USERNAME/flappy-bird-deluxe.git


Then enter the directory:

cd flappy-bird-deluxe

2. Run the game
python flappybird.py


On Windows, you can also use:

py flappybird.py


That's it!

📁 Project Structure
flappy-bird-deluxe/
│
├── flappybird.py
├── README.md
├── LICENSE
│
└── screenshots/
    ├── menu.png
    ├── gameplay.png
    ├── pause.png
    ├── settings.png
    └── gameover.png


The game is intentionally contained in a single Python file, making it easy to download, inspect, modify, and learn from.

🛠️ Built With
Python

The game's logic, physics, menus, and rendering are written in Python.

Tkinter

Tkinter's Canvas is used to render:

The bird

Pipes

Clouds

Mountains

Ground

UI

Menus

Particles

Background effects

No External Game Engine

This project does not use:

Pygame

Arcade

Godot

Unity

Other external game engines

The entire game runs with Python's standard GUI toolkit.

🧠 How It Works

The game uses a simple game loop that runs approximately every 16 milliseconds.

Input
  ↓
Physics
  ↓
Collision Detection
  ↓
Score / Pipes
  ↓
Particles
  ↓
Rendering
  ↓
Repeat

Bird Physics

The bird has a vertical velocity affected by gravity.

When the player presses Space or clicks:

bird_velocity = flap_strength


Gravity is then continuously applied:

bird_velocity += gravity
bird_y += bird_velocity


This creates the familiar Flappy Bird-style movement.

Pipes

Pipe positions are randomly generated while maintaining a gap large enough for the bird to pass through.

The pipes continuously move toward the player:

pipe["x"] -= pipe_speed


When the bird successfully passes a pipe, the score increases.

🎨 Customizing the Game

The game is designed to be easy to modify.

Change the window size

At the top of flappybird.py:

WIDTH = 600
HEIGHT = 800

Change gravity
gravity = 0.5


Higher values make the bird fall faster.

Change flap strength
flap_strength = -9


More negative values make the bird flap higher.

Change pipe speed
pipe_speed = 4


Higher values make the game faster.

Add a new sky

Add another entry to:

SKY_THEMES = {
    ...
}


For example:

"Forest": {
    "top": "#4b8f5a",
    "bottom": "#b8df9f",
    "cloud": "#e7f4df",
    "sun": "#fff0a3",
    "ground": "#795548",
    "grass": "#388e3c",
    "mountain": "#477a4b",
},

💡 Ideas for Future Updates

Some possible improvements:

🔊 Sound effects

🎵 Background music

🪙 Collectible coins

🏆 Achievement system

🐦 Unlockable bird skins

🎨 More backgrounds

🌧️ Weather effects

❄️ Snow mode

🌧️ Rain mode

🏪 Bird/skin shop

📊 Statistics screen

💾 Save settings and high scores

🌐 Online leaderboard

🎮 Controller support

📱 Mobile version

✨ More particle effects

🏅 Daily challenges

🤝 Contributing

Contributions are welcome!

If you'd like to improve the game:

Fork the repository.

Create a new branch.

git checkout -b feature/my-new-feature


Make your changes.

Test the game.

Commit your changes.

git commit -m "Add my new feature"


Push your branch.

git push origin feature/my-new-feature


Open a Pull Request.

🐛 Reporting Bugs

Found a bug?

Open a GitHub Issue and include:

Your operating system

Python version

What happened

What you expected to happen

Steps to reproduce the issue

Any error message from the terminal

For example:

OS: Windows 11
Python: 3.14

Problem:
The game crashes when opening the settings menu.

Error:
[paste error here]

📜 License

This project is licensed under the MIT License.

See LICENSE for the full license text.

⚠️ Disclaimer

This is an independent Flappy Bird-style project created for educational and entertainment purposes.

It is not affiliated with or endorsed by the original Flappy Bird creators.

⭐ Support the Project

If you enjoyed the game:

⭐ Star the repository

🐛 Report bugs

💡 Suggest features

🔧 Submit improvements

📢 Share it with other Python developers

Every contribution helps!

🐦 Have Fun!
       __
   ___( o)>
   \ <_. )
    `---'

  FLAPPY BIRD DELUXE


How far can you fly?
