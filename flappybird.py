import tkinter as tk
import random
import math

# ============================================================
# FLAPPY BIRD DELUXE
# Tkinter only - no pygame or external libraries
# ============================================================

WIDTH = 600
HEIGHT = 800
GROUND_Y = HEIGHT - 110
FRAME_MS = 16

# ============================================================
# COLORS / THEMES
# ============================================================

SKY_THEMES = {
    "Classic": {
        "top": "#62c7f2",
        "bottom": "#b9edff",
        "cloud": "#ffffff",
        "sun": "#ffe37a",
        "ground": "#d9a441",
        "grass": "#57b84c",
        "mountain": "#77b47c",
    },

    "Sunset": {
        "top": "#e76f75",
        "bottom": "#ffd18a",
        "cloud": "#ffe8d6",
        "sun": "#fff0a3",
        "ground": "#a87545",
        "grass": "#557d43",
        "mountain": "#ad7070",
    },

    "Ocean": {
        "top": "#167db8",
        "bottom": "#76d5e8",
        "cloud": "#d8f4ff",
        "sun": "#d8f5ff",
        "ground": "#bf8c4a",
        "grass": "#4d9b47",
        "mountain": "#438ca1",
    },

    "Night": {
        "top": "#101a44",
        "bottom": "#394b83",
        "cloud": "#59668d",
        "sun": "#f4f1c7",
        "ground": "#4e463e",
        "grass": "#425f40",
        "mountain": "#252f5c",
    },

    "Lavender": {
        "top": "#7773bd",
        "bottom": "#d7a9df",
        "cloud": "#f1e5f5",
        "sun": "#fff0bd",
        "ground": "#9a754e",
        "grass": "#60904d",
        "mountain": "#756e9f",
    },
}

DIFFICULTIES = {
    "Easy": {
        "gravity": 0.42,
        "flap": -8.5,
        "speed": 3.2,
        "gap": 205,
        "spawn": 110,
    },

    "Normal": {
        "gravity": 0.50,
        "flap": -9.0,
        "speed": 4.0,
        "gap": 175,
        "spawn": 105,
    },

    "Hard": {
        "gravity": 0.58,
        "flap": -9.5,
        "speed": 4.8,
        "gap": 150,
        "spawn": 100,
    },
}

# Bird
BIRD_YELLOW = "#ffd83d"
BIRD_LIGHT = "#fff27a"
BIRD_ORANGE = "#f28c28"
BIRD_DARK = "#d7651c"

# Pipes
PIPE_GREEN = "#43b84b"
PIPE_DARK = "#238a36"
PIPE_LIGHT = "#71d95e"
PIPE_SHADOW = "#17682c"
PIPE_BOLT = "#286f32"

# UI
UI_DARK = "#172235"
UI_DARKER = "#101827"
UI_TEXT = "#ffffff"
UI_MUTED = "#aebbd0"
UI_BLUE = "#4285f4"
UI_GREEN = "#39b54a"
UI_RED = "#e45b5b"
UI_PURPLE = "#8e5bd9"
UI_GRAY = "#607d8b"
UI_GOLD = "#ffdf5d"

# ============================================================
# WINDOW
# ============================================================

root = tk.Tk()
root.title("Flappy Bird Deluxe")
root.resizable(False, False)
root.configure(bg=UI_DARKER)

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    highlightthickness=0,
    bd=0
)
canvas.pack()

# ============================================================
# GAME STATES
# ============================================================

TITLE = "title"
PLAYING = "playing"
PAUSED = "paused"
GAME_OVER = "gameover"
SETTINGS = "settings"

state = TITLE
previous_state = TITLE

# ============================================================
# SETTINGS
# ============================================================

sky_theme = "Classic"
difficulty = "Normal"

def apply_difficulty():
    global gravity
    global flap_strength
    global pipe_speed
    global pipe_gap
    global pipe_spawn_distance

    settings = DIFFICULTIES[difficulty]

    gravity = settings["gravity"]
    flap_strength = settings["flap"]
    pipe_speed = settings["speed"]
    pipe_gap = settings["gap"]
    pipe_spawn_distance = settings["spawn"]


gravity = 0.5
flap_strength = -9
pipe_speed = 4
pipe_gap = 175
pipe_spawn_distance = 105

apply_difficulty()

# ============================================================
# GAME VARIABLES
# ============================================================

bird_x = 145
bird_y = HEIGHT // 2
bird_velocity = 0
bird_angle = 0

score = 0
best_score = 0

pipes = []

frame = 0
spawn_timer = 0
ground_offset = 0
wing_phase = 0

# ============================================================
# CLOUDS
# ============================================================

clouds = []

for _ in range(10):
    clouds.append({
        "x": random.randint(-150, WIDTH + 150),
        "y": random.randint(65, 370),
        "scale": random.uniform(0.55, 1.25),
        "speed": random.uniform(0.12, 0.4),
    })

# ============================================================
# STARS
# ============================================================

stars = []

for _ in range(110):
    stars.append({
        "x": random.randint(0, WIDTH),
        "y": random.randint(20, 500),
        "size": random.choice([1, 1, 1, 2]),
        "phase": random.random() * math.pi * 2,
    })

# ============================================================
# PARTICLES
# ============================================================

particles = []

def create_particles(x, y, color, amount=5):
    for _ in range(amount):
        particles.append({
            "x": x,
            "y": y,
            "vx": random.uniform(-2.5, 2.5),
            "vy": random.uniform(-3.5, 1.0),
            "life": random.randint(20, 45),
            "size": random.randint(2, 5),
            "color": color,
        })


def update_particles():
    for particle in particles[:]:
        particle["x"] += particle["vx"]
        particle["y"] += particle["vy"]
        particle["vy"] += 0.12
        particle["life"] -= 1

        if particle["life"] <= 0:
            particles.remove(particle)


def draw_particles():
    for particle in particles:
        size = particle["size"]

        canvas.create_oval(
            particle["x"] - size,
            particle["y"] - size,
            particle["x"] + size,
            particle["y"] + size,
            fill=particle["color"],
            outline=""
        )

# ============================================================
# UTILITY
# ============================================================

def current_theme():
    return SKY_THEMES[sky_theme]


# ============================================================
# BACKGROUND
# ============================================================

def draw_gradient():
    t = current_theme()

    top = t["top"]
    bottom = t["bottom"]

    r1 = int(top[1:3], 16)
    g1 = int(top[3:5], 16)
    b1 = int(top[5:7], 16)

    r2 = int(bottom[1:3], 16)
    g2 = int(bottom[3:5], 16)
    b2 = int(bottom[5:7], 16)

    strips = 90
    strip_height = HEIGHT / strips

    for i in range(strips):
        ratio = i / (strips - 1)

        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)

        color = f"#{r:02x}{g:02x}{b:02x}"

        canvas.create_rectangle(
            0,
            i * strip_height,
            WIDTH,
            (i + 1) * strip_height + 2,
            fill=color,
            outline=""
        )


def draw_sun():
    t = current_theme()

    if sky_theme == "Night":
        # Moon
        canvas.create_oval(
            445,
            75,
            535,
            165,
            fill=t["sun"],
            outline=""
        )

        canvas.create_oval(
            472,
            63,
            548,
            139,
            fill=t["top"],
            outline=""
        )

    else:
        canvas.create_oval(
            445,
            70,
            545,
            170,
            fill=t["sun"],
            outline=""
        )

        for i in range(12):
            angle = i * math.pi / 6

            x1 = 495 + math.cos(angle) * 62
            y1 = 120 + math.sin(angle) * 62

            x2 = 495 + math.cos(angle) * 77
            y2 = 120 + math.sin(angle) * 77

            canvas.create_line(
                x1,
                y1,
                x2,
                y2,
                fill=t["sun"],
                width=3
            )


def draw_stars():
    if sky_theme != "Night":
        return

    for star in stars:
        twinkle = (math.sin(frame * 0.05 + star["phase"]) + 1) / 2

        if twinkle > 0.3:
            size = star["size"]

            canvas.create_oval(
                star["x"],
                star["y"],
                star["x"] + size,
                star["y"] + size,
                fill="#ffffff",
                outline=""
            )


def draw_cloud(x, y, scale):
    color = current_theme()["cloud"]

    parts = [
        (-42, 8, 45, 38),
        (-12, -17, 60, 54),
        (25, 0, 65, 48),
        (57, 14, 45, 35),
    ]

    for dx, dy, width, height in parts:
        canvas.create_oval(
            x + dx * scale,
            y + dy * scale,
            x + (dx + width) * scale,
            y + (dy + height) * scale,
            fill=color,
            outline=""
        )

    canvas.create_rectangle(
        x - 18 * scale,
        y + 15 * scale,
        x + 72 * scale,
        y + 35 * scale,
        fill=color,
        outline=""
    )


def update_clouds():
    for cloud in clouds:
        cloud["x"] -= cloud["speed"]

        if cloud["x"] < -180:
            cloud["x"] = WIDTH + random.randint(30, 180)
            cloud["y"] = random.randint(65, 370)
            cloud["scale"] = random.uniform(0.55, 1.25)


def draw_clouds():
    if sky_theme == "Night":
        return

    for cloud in clouds:
        draw_cloud(
            cloud["x"],
            cloud["y"],
            cloud["scale"]
        )


def draw_mountains():
    color = current_theme()["mountain"]

    points = [
        0, 590,
        80, 505,
        160, 555,
        270, 430,
        360, 540,
        460, 450,
        600, 555,
        600, 700,
        0, 700,
    ]

    canvas.create_polygon(
        points,
        fill=color,
        outline=""
    )

# ============================================================
# PIPES
# ============================================================

def draw_pipe_cap(x, y):
    # Main cap
    canvas.create_rectangle(
        x - 8,
        y,
        x + 80,
        y + 30,
        fill=PIPE_GREEN,
        outline=PIPE_SHADOW,
        width=2
    )

    # Bright top
    canvas.create_rectangle(
        x + 3,
        y + 4,
        x + 71,
        y + 10,
        fill=PIPE_LIGHT,
        outline=""
    )

    # Right shadow
    canvas.create_rectangle(
        x + 62,
        y + 2,
        x + 78,
        y + 28,
        fill=PIPE_DARK,
        outline=""
    )

    # Bolts
    for bx in (x + 7, x + 66):
        canvas.create_oval(
            bx,
            y + 14,
            bx + 7,
            y + 21,
            fill=PIPE_BOLT,
            outline=PIPE_SHADOW
        )


def draw_pipe_body(x, y1, y2):
    if y2 <= y1:
        return

    # Main body
    canvas.create_rectangle(
        x,
        y1,
        x + 72,
        y2,
        fill=PIPE_GREEN,
        outline=PIPE_SHADOW,
        width=2
    )

    # Right shadow
    canvas.create_rectangle(
        x + 54,
        y1,
        x + 72,
        y2,
        fill=PIPE_DARK,
        outline=""
    )

    # Main highlight
    canvas.create_rectangle(
        x + 9,
        y1,
        x + 22,
        y2,
        fill=PIPE_LIGHT,
        outline=""
    )

    # Secondary highlight
    canvas.create_rectangle(
        x + 25,
        y1,
        x + 30,
        y2,
        fill="#5dcc55",
        outline=""
    )


def draw_pipes():
    for pipe in pipes:
        x = pipe["x"]
        top = pipe["gap_top"]
        bottom = pipe["gap_bottom"]

        draw_pipe_body(
            x,
            -20,
            top
        )

        draw_pipe_cap(
            x,
            top - 30
        )

        draw_pipe_body(
            x,
            bottom,
            GROUND_Y
        )

        draw_pipe_cap(
            x,
            bottom
        )

# ============================================================
# GROUND
# ============================================================

def draw_ground():
    t = current_theme()

    # Dirt
    canvas.create_rectangle(
        0,
        GROUND_Y,
        WIDTH,
        HEIGHT,
        fill=t["ground"],
        outline=""
    )

    # Grass
    canvas.create_rectangle(
        0,
        GROUND_Y,
        WIDTH,
        GROUND_Y + 18,
        fill=t["grass"],
        outline=""
    )

    # Grass blades
    for x in range(-30, WIDTH + 40, 18):
        offset = (ground_offset + x) % 18

        canvas.create_polygon(
            x - offset,
            GROUND_Y + 18,
            x + 5 - offset,
            GROUND_Y + 5,
            x + 10 - offset,
            GROUND_Y + 18,
            fill="#3f963b",
            outline=""
        )

    # Dirt details
    for x in range(-50, WIDTH + 50, 45):
        offset = (ground_offset * 0.5 + x) % 45

        canvas.create_line(
            x - offset,
            GROUND_Y + 42,
            x + 20 - offset,
            GROUND_Y + 52,
            fill="#9a702e",
            width=3
        )

        canvas.create_line(
            x + 10 - offset,
            GROUND_Y + 77,
            x + 35 - offset,
            GROUND_Y + 67,
            fill="#e2b84d",
            width=3
        )

# ============================================================
# BIRD
# ============================================================

def draw_bird():
    x = bird_x
    y = bird_y

    # Shadow
    canvas.create_oval(
        x - 20,
        y + 17,
        x + 20,
        y + 25,
        fill="#5794a5",
        outline=""
    )

    # Tail
    canvas.create_polygon(
        x - 20,
        y + 2,
        x - 39,
        y - 8,
        x - 32,
        y + 10,
        x - 40,
        y + 20,
        x - 18,
        y + 16,
        fill=BIRD_ORANGE,
        outline=BIRD_DARK
    )

    # Body
    canvas.create_oval(
        x - 25,
        y - 25,
        x + 25,
        y + 25,
        fill=BIRD_YELLOW,
        outline="#c99616",
        width=2
    )

    # Belly
    canvas.create_oval(
        x - 14,
        y - 3,
        x + 17,
        y + 22,
        fill=BIRD_LIGHT,
        outline=""
    )

    # Wing
    wing_offset = math.sin(wing_phase) * 5

    canvas.create_oval(
        x - 21,
        y - 2 + wing_offset,
        x + 5,
        y + 18 + wing_offset,
        fill=BIRD_ORANGE,
        outline=BIRD_DARK,
        width=2
    )

    canvas.create_line(
        x - 10,
        y + 6 + wing_offset,
        x - 2,
        y + 12 + wing_offset,
        fill="#ffb436",
        width=3
    )

    # Eye
    canvas.create_oval(
        x + 3,
        y - 18,
        x + 18,
        y - 3,
        fill="#ffffff",
        outline="#c99616"
    )

    canvas.create_oval(
        x + 10,
        y - 14,
        x + 16,
        y - 8,
        fill="#111111",
        outline=""
    )

    # Beak
    canvas.create_polygon(
        x + 19,
        y - 2,
        x + 40,
        y + 5,
        x + 19,
        y + 11,
        fill=BIRD_ORANGE,
        outline=BIRD_DARK
    )

    # Beak line
    canvas.create_line(
        x + 20,
        y + 5,
        x + 35,
        y + 5,
        fill=BIRD_DARK,
        width=2
    )

# ============================================================
# PIPE GENERATION
# ============================================================

def create_pipe():
    margin = 90

    minimum = margin
    maximum = GROUND_Y - pipe_gap - margin

    gap_top = random.randint(
        minimum,
        maximum
    )

    pipes.append({
        "x": WIDTH + 30,
        "gap_top": gap_top,
        "gap_bottom": gap_top + pipe_gap,
        "scored": False,
    })

# ============================================================
# COLLISION
# ============================================================

def bird_collision():
    bx1 = bird_x - 21
    bx2 = bird_x + 21
    by1 = bird_y - 22
    by2 = bird_y + 22

    if by1 <= 0:
        return True

    if by2 >= GROUND_Y:
        return True

    for pipe in pipes:
        px1 = pipe["x"] - 8
        px2 = pipe["x"] + 80

        if bx2 > px1 and bx1 < px2:

            if by1 < pipe["gap_top"]:
                return True

            if by2 > pipe["gap_bottom"]:
                return True

    return False

# ============================================================
# SCORE
# ============================================================

def update_score():
    global score

    for pipe in pipes:
        if not pipe["scored"] and pipe["x"] + 80 < bird_x:
            pipe["scored"] = True
            score += 1

            create_particles(
                bird_x,
                bird_y,
                "#fff7a8",
                8
            )

# ============================================================
# UI HELPERS
# ============================================================

def draw_button(x1, y1, x2, y2, text, color):
    # Shadow
    canvas.create_rectangle(
        x1 + 4,
        y1 + 5,
        x2 + 4,
        y2 + 5,
        fill="#101827",
        outline=""
    )

    # Main
    canvas.create_rectangle(
        x1,
        y1,
        x2,
        y2,
        fill=color,
        outline="#ffffff",
        width=2
    )

    # Highlight
    canvas.create_rectangle(
        x1 + 3,
        y1 + 3,
        x2 - 3,
        y1 + 7,
        fill="#ffffff",
        outline=""
    )

    canvas.create_text(
        (x1 + x2) / 2,
        (y1 + y2) / 2 + 2,
        text=text,
        font=("Arial", 17, "bold"),
        fill="#ffffff"
    )


def draw_score():
    canvas.create_text(
        WIDTH // 2 + 3,
        56,
        text=str(score),
        font=("Arial", 44, "bold"),
        fill="#1f5f73"
    )

    canvas.create_text(
        WIDTH // 2,
        52,
        text=str(score),
        font=("Arial", 44, "bold"),
        fill="#ffffff"
    )


def draw_pause_button():
    canvas.create_oval(
        WIDTH - 78,
        17,
        WIDTH - 20,
        75,
        fill="#375468",
        outline=""
    )

    canvas.create_oval(
        WIDTH - 75,
        14,
        WIDTH - 23,
        67,
        fill="#ffffff",
        outline="#dce9ef",
        width=2
    )

    canvas.create_rectangle(
        WIDTH - 59,
        29,
        WIDTH - 53,
        53,
        fill="#263238",
        outline=""
    )

    canvas.create_rectangle(
        WIDTH - 46,
        29,
        WIDTH - 40,
        53,
        fill="#263238",
        outline=""
    )

# ============================================================
# TITLE SCREEN
# ============================================================

def draw_title():
    draw_gradient()
    draw_stars()
    draw_sun()
    draw_clouds()
    draw_mountains()

    # Floating bird
    original_y = bird_y

    floating_y = 285 + math.sin(frame * 0.06) * 12

    draw_bird_at(
        bird_x,
        floating_y
    )

    # Logo shadow
    canvas.create_text(
        WIDTH // 2 + 4,
        135 + 4,
        text="FLAPPY",
        font=("Arial", 58, "bold"),
        fill="#365b6a"
    )

    canvas.create_text(
        WIDTH // 2,
        135,
        text="FLAPPY",
        font=("Arial", 58, "bold"),
        fill="#ffffff"
    )

    canvas.create_text(
        WIDTH // 2 + 3,
        198 + 3,
        text="DELUXE",
        font=("Arial", 34, "bold"),
        fill="#765f20"
    )

    canvas.create_text(
        WIDTH // 2,
        195,
        text="DELUXE",
        font=("Arial", 34, "bold"),
        fill="#fff06a"
    )

    draw_button(
        WIDTH // 2 - 125,
        470,
        WIDTH // 2 + 125,
        530,
        "START GAME",
        UI_GREEN
    )

    draw_button(
        WIDTH // 2 - 125,
        545,
        WIDTH // 2 + 125,
        605,
        "SETTINGS",
        UI_BLUE
    )

    canvas.create_text(
        WIDTH // 2,
        665,
        text="SPACE / CLICK  •  FLAP",
        font=("Arial", 14, "bold"),
        fill="#ffffff"
    )

    canvas.create_text(
        WIDTH // 2,
        695,
        text=f"Best Score: {best_score}",
        font=("Arial", 13),
        fill="#ffffff"
    )

# ============================================================
# BIRD AT POSITION
# ============================================================

def draw_bird_at(x, y):
    global bird_x
    global bird_y

    old_x = bird_x
    old_y = bird_y

    bird_x = x
    bird_y = y

    draw_bird()

    bird_x = old_x
    bird_y = old_y

# ============================================================
# PAUSE SCREEN
# ============================================================

def draw_pause():
    canvas.create_rectangle(
        0,
        0,
        WIDTH,
        HEIGHT,
        fill="#182235",
        stipple="gray50",
        outline=""
    )

    canvas.create_rectangle(
        70,
        120,
        WIDTH - 70,
        590,
        fill=UI_DARK,
        outline="#ffffff",
        width=2
    )

    canvas.create_text(
        WIDTH // 2 + 3,
        175 + 3,
        text="PAUSED",
        font=("Arial", 48, "bold"),
        fill="#101827"
    )

    canvas.create_text(
        WIDTH // 2,
        175,
        text="PAUSED",
        font=("Arial", 48, "bold"),
        fill="#ffffff"
    )

    draw_button(
        WIDTH // 2 - 125,
        260,
        WIDTH // 2 + 125,
        320,
        "RESUME",
        UI_GREEN
    )

    draw_button(
        WIDTH // 2 - 125,
        340,
        WIDTH // 2 + 125,
        400,
        "SETTINGS",
        UI_BLUE
    )

    draw_button(
        WIDTH // 2 - 125,
        420,
        WIDTH // 2 + 125,
        480,
        "QUIT TO MENU",
        UI_RED
    )

    canvas.create_text(
        WIDTH // 2,
        535,
        text="Press P or ESC to resume",
        font=("Arial", 13),
        fill=UI_MUTED
    )

# ============================================================
# SETTINGS SCREEN
# ============================================================

def draw_settings():
    draw_gradient()
    draw_stars()
    draw_sun()
    draw_clouds()
    draw_mountains()

    canvas.create_rectangle(
        45,
        35,
        WIDTH - 45,
        HEIGHT - 35,
        fill=UI_DARK,
        outline="#ffffff",
        width=2
    )

    canvas.create_text(
        WIDTH // 2,
        90,
        text="SETTINGS",
        font=("Arial", 35, "bold"),
        fill="#ffffff"
    )

    # Sky
    canvas.create_text(
        85,
        150,
        text="SKY",
        anchor="w",
        font=("Arial", 17, "bold"),
        fill=UI_MUTED
    )

    draw_button(
        90,
        180,
        WIDTH - 90,
        240,
        sky_theme,
        UI_BLUE
    )

    canvas.create_text(
        72,
        210,
        text="‹",
        font=("Arial", 31, "bold"),
        fill="#ffffff"
    )

    canvas.create_text(
        WIDTH - 72,
        210,
        text="›",
        font=("Arial", 31, "bold"),
        fill="#ffffff"
    )

    # Difficulty
    canvas.create_text(
        85,
        275,
        text="DIFFICULTY",
        anchor="w",
        font=("Arial", 17, "bold"),
        fill=UI_MUTED
    )

    draw_button(
        90,
        305,
        WIDTH - 90,
        365,
        difficulty,
        UI_PURPLE
    )

    canvas.create_text(
        72,
        335,
        text="‹",
        font=("Arial", 31, "bold"),
        fill="#ffffff"
    )

    canvas.create_text(
        WIDTH - 72,
        335,
        text="›",
        font=("Arial", 31, "bold"),
        fill="#ffffff"
    )

    descriptions = {
        "Easy": "Larger gaps • slower pipes • relaxed physics",
        "Normal": "Balanced classic gameplay",
        "Hard": "Smaller gaps • faster pipes • stronger gravity",
    }

    canvas.create_text(
        WIDTH // 2,
        400,
        text=descriptions[difficulty],
        font=("Arial", 13),
        fill="#c7d2e9"
    )

    # Controls
    canvas.create_text(
        WIDTH // 2,
        455,
        text="CONTROLS",
        font=("Arial", 17, "bold"),
        fill=UI_MUTED
    )

    canvas.create_text(
        WIDTH // 2,
        490,
        text="SPACE / LEFT CLICK     Flap",
        font=("Arial", 14),
        fill="#ffffff"
    )

    canvas.create_text(
        WIDTH // 2,
        520,
        text="P / ESC                 Pause",
        font=("Arial", 14),
        fill="#ffffff"
    )

    canvas.create_text(
        WIDTH // 2,
        550,
        text="← / →                   Change Sky",
        font=("Arial", 14),
        fill="#ffffff"
    )

    canvas.create_text(
        WIDTH // 2,
        580,
        text="A / D                    Difficulty",
        font=("Arial", 14),
        fill="#ffffff"
    )

    draw_button(
        WIDTH // 2 - 120,
        625,
        WIDTH // 2 + 120,
        680,
        "BACK",
        UI_GRAY
    )

# ============================================================
# GAME OVER
# ============================================================

def draw_game_over():
    canvas.create_rectangle(
        0,
        0,
        WIDTH,
        HEIGHT,
        fill="#111827",
        stipple="gray50",
        outline=""
    )

    canvas.create_rectangle(
        55,
        160,
        WIDTH - 55,
        625,
        fill=UI_DARK,
        outline="#ffffff",
        width=2
    )

    canvas.create_text(
        WIDTH // 2,
        220,
        text="GAME OVER",
        font=("Arial", 40, "bold"),
        fill=UI_GOLD
    )

    canvas.create_text(
        WIDTH // 2,
        275,
        text="SCORE",
        font=("Arial", 14, "bold"),
        fill=UI_MUTED
    )

    canvas.create_text(
        WIDTH // 2,
        315,
        text=str(score),
        font=("Arial", 44, "bold"),
        fill="#ffffff"
    )

    canvas.create_text(
        WIDTH // 2,
        365,
        text="BEST",
        font=("Arial", 14, "bold"),
        fill=UI_MUTED
    )

    canvas.create_text(
        WIDTH // 2,
        400,
        text=str(best_score),
        font=("Arial", 31, "bold"),
        fill="#7dd3fc"
    )

    if score == best_score and score > 0:
        canvas.create_text(
            WIDTH // 2,
            440,
            text="NEW BEST!",
            font=("Arial", 15, "bold"),
            fill=UI_GOLD
        )

    draw_button(
        WIDTH // 2 - 125,
        470,
        WIDTH // 2 + 125,
        525,
        "PLAY AGAIN",
        UI_GREEN
    )

    draw_button(
        WIDTH // 2 - 125,
        540,
        WIDTH // 2 + 125,
        595,
        "MAIN MENU",
        UI_GRAY
    )

# ============================================================
# GAME RESET
# ============================================================

def reset_game():
    global bird_x
    global bird_y
    global bird_velocity
    global bird_angle
    global score
    global pipes
    global spawn_timer
    global ground_offset
    global state

    bird_x = 145
    bird_y = HEIGHT // 2

    bird_velocity = 0
    bird_angle = 0

    score = 0

    pipes.clear()

    spawn_timer = 0
    ground_offset = 0

    state = PLAYING

    create_pipe()

# ============================================================
# GAME OVER
# ============================================================

def end_game():
    global state
    global best_score

    state = GAME_OVER

    if score > best_score:
        best_score = score

    create_particles(
        bird_x,
        bird_y,
        "#ffe066",
        25
    )

# ============================================================
# FLAP
# ============================================================

def flap():
    global bird_velocity

    if state == TITLE:
        reset_game()
        return

    if state == GAME_OVER:
        reset_game()
        return

    if state == PLAYING:
        bird_velocity = flap_strength

        create_particles(
            bird_x - 14,
            bird_y + 8,
            "#ffffff",
            3
        )

# ============================================================
# PAUSE
# ============================================================

def toggle_pause():
    global state

    if state == PLAYING:
        state = PAUSED

    elif state == PAUSED:
        state = PLAYING

# ============================================================
# TITLE
# ============================================================

def go_title():
    global state
    state = TITLE

# ============================================================
# SETTINGS
# ============================================================

def open_settings():
    global state
    global previous_state

    previous_state = state
    state = SETTINGS


def close_settings():
    global state
    state = previous_state


def change_sky(direction):
    global sky_theme

    names = list(SKY_THEMES.keys())

    index = names.index(sky_theme)
    index += direction

    if index < 0:
        index = len(names) - 1

    if index >= len(names):
        index = 0

    sky_theme = names[index]


def change_difficulty(direction):
    global difficulty

    names = list(DIFFICULTIES.keys())

    index = names.index(difficulty)
    index += direction

    if index < 0:
        index = len(names) - 1

    if index >= len(names):
        index = 0

    difficulty = names[index]

    apply_difficulty()

# ============================================================
# MOUSE
# ============================================================

def mouse_click(event):
    x = event.x
    y = event.y

    if state == TITLE:

        if 460 <= y <= 540:
            reset_game()
            return

        if 540 <= y <= 620:
            open_settings()
            return

        flap()
        return

    if state == PLAYING:

        # Pause button
        if x >= WIDTH - 95 and y <= 90:
            toggle_pause()
            return

        flap()
        return

    if state == PAUSED:

        if 250 <= y <= 320:
            toggle_pause()
            return

        if 330 <= y <= 405:
            open_settings()
            return

        if 410 <= y <= 490:
            go_title()
            return

    if state == GAME_OVER:

        if 460 <= y <= 535:
            reset_game()
            return

        if 535 <= y <= 610:
            go_title()
            return

    if state == SETTINGS:

        if 170 <= y <= 250:
            if x < WIDTH // 2:
                change_sky(-1)
            else:
                change_sky(1)

            return

        if 295 <= y <= 375:
            if x < WIDTH // 2:
                change_difficulty(-1)
            else:
                change_difficulty(1)

            return

        if 615 <= y <= 690:
            close_settings()
            return

# ============================================================
# KEYBOARD
# ============================================================

def key_press(event):
    key = event.keysym.lower()

    if key == "space":
        flap()
        return

    if key == "p" or key == "escape":

        if state == PLAYING:
            toggle_pause()
            return

        if state == PAUSED:
            toggle_pause()
            return

    if key == "r":
        if state == GAME_OVER:
            reset_game()
            return

    if state == SETTINGS:

        if key == "left":
            change_sky(-1)

        elif key == "right":
            change_sky(1)

        elif key == "a":
            change_difficulty(-1)

        elif key == "d":
            change_difficulty(1)

# ============================================================
# UPDATE
# ============================================================

def update():
    global bird_y
    global bird_velocity
    global bird_angle
    global spawn_timer
    global ground_offset
    global wing_phase

    wing_phase += 0.35

    update_clouds()
    update_particles()

    if state == PLAYING:

        # Physics
        bird_velocity += gravity
        bird_y += bird_velocity

        # Rotation
        target_angle = bird_velocity * 4

        target_angle = max(-25, min(85, target_angle))

        bird_angle += (
            target_angle - bird_angle
        ) * 0.15

        # Pipes
        for pipe in pipes:
            pipe["x"] -= pipe_speed

        # Spawn
        spawn_timer += 1

        if spawn_timer >= pipe_spawn_distance:
            create_pipe()
            spawn_timer = 0

        # Remove pipes
        pipes[:] = [
            pipe
            for pipe in pipes
            if pipe["x"] > -100
        ]

        update_score()

        # Ground
        ground_offset += pipe_speed

        if ground_offset > 100:
            ground_offset = 0

        # Collision
        if bird_collision():
            end_game()

    elif state == TITLE:
        pass

    elif state == GAME_OVER:

        bird_velocity += gravity * 0.7
        bird_y += bird_velocity

        if bird_y > GROUND_Y - 20:
            bird_y = GROUND_Y - 20

# ============================================================
# DRAW PLAYING
# ============================================================

def draw_game():
    draw_gradient()
    draw_stars()
    draw_sun()
    draw_clouds()
    draw_mountains()

    draw_pipes()
    draw_ground()

    draw_particles()
    draw_bird()

    draw_score()
    draw_pause_button()

# ============================================================
# MAIN RENDER
# ============================================================

def render():
    global frame

    frame += 1

    update()

    canvas.delete("all")

    if state == TITLE:
        draw_title()

    elif state == PLAYING:
        draw_game()

    elif state == PAUSED:
        draw_game()
        draw_pause()

    elif state == GAME_OVER:
        draw_game()
        draw_game_over()

    elif state == SETTINGS:
        draw_settings()

    root.after(FRAME_MS, render)

# ============================================================
# INPUT
# ============================================================

root.bind("<KeyPress>", key_press)
root.bind("<Button-1>", mouse_click)

canvas.focus_set()

# ============================================================
# START
# ============================================================

render()
root.mainloop()
