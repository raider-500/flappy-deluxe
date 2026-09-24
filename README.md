# Flappy Bird Deluxe

![Flappy Bird Deluxe](screenshots/gameplay.png)

A polished Flappy Bird-inspired game built entirely in Python using `tkinter`, featuring animated environments, customizable skies, detailed pipes, particle effects, multiple difficulty levels, and a full pause/settings system.

> **Note:** This project does not use Pygame or any external game engine. Everything is rendered using Python's built-in `tkinter` Canvas.

## Features

- 🐦 Smooth Flappy Bird-style physics
- 🎨 Multiple animated sky themes
- ☀️ Dynamic sun and moon
- ⭐ Twinkling stars in Night mode
- ☁️ Moving clouds
- ⛰️ Background mountains
- 🌱 Animated scrolling ground
- ✨ Particle effects
- 🪽 Animated bird wings
- 🟢 Detailed pipes with highlights, shadows, caps, and bolts
- 🏆 Score and high-score tracking
- ⚙️ Three difficulty levels
- ⏸️ Pause menu
- 🎨 Customization/settings menu
- 💀 Improved game-over screen
- 🖱️ Mouse controls
- ⌨️ Keyboard controls
- 📦 No external dependencies

## Screenshots

### Main Menu

![Main Menu](screenshots/menu.png)

### Gameplay

![Gameplay](screenshots/gameplay.png)

### Pause Menu

![Pause Menu](screenshots/pause.png)

### Settings

![Settings](screenshots/settings.png)

### Game Over

![Game Over](screenshots/gameover.png)

## Sky Themes

The game includes several different environments that can be changed from the settings menu.

| Theme | Description |
|---|---|
| Classic | Bright blue daytime sky |
| Sunset | Warm orange and pink sunset |
| Ocean | Blue atmospheric theme |
| Night | Dark sky with stars and moon |
| Lavender | Purple/pink sky |

Each theme changes multiple elements of the environment, including the sky gradient, clouds, sun/moon, mountains, grass, and ground.

## Difficulty

Three gameplay difficulties are available:

| Difficulty | Gameplay |
|---|---|
| Easy | Larger pipe gaps and slower movement |
| Normal | Balanced gameplay |
| Hard | Smaller pipe gaps, faster pipes, and stronger gravity |

Difficulty can be changed from the Settings menu.

## Controls

| Key / Input | Action |
|---|---|
| `Space` | Flap |
| `Left Click` | Flap |
| `P` | Pause |
| `Esc` | Pause |
| `R` | Restart after game over |
| `←` | Previous sky theme |
| `→` | Next sky theme |
| `A` | Easier difficulty |
| `D` | Harder difficulty |

## Installation

### Requirements

- Python 3.x
- Tkinter

No Pygame installation is required.

Tkinter is included with most standard Python installations.

### Windows

Clone the repository:

```powershell
git clone https://github.com/YOUR_USERNAME/flappy-bird-deluxe.git
cd flappy-bird-deluxe
