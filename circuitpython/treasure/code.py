import board
import time
import math
import random
from digitalio import DigitalInOut, Direction, Pull
from neopixel import NeoPixel

# NeoPixels
pixels = NeoPixel(board.NEOPIXEL, 10, brightness=1.0, auto_write=False)

# Toggle Switch
switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
switch_state = switch.value

# Button A
button_a = DigitalInOut(board.BUTTON_A)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN
button_a_state = False

# Button B
button_b = DigitalInOut(board.BUTTON_B)
button_b.direction = Direction.INPUT
button_b.pull = Pull.DOWN
button_b_state = False

def event_sleep(seconds):
    check_inputs()
    time.sleep(seconds)

def check_inputs():
    global switch_state, button_a_state, button_b_state

    if button_b.value is not button_b_state:
        button_b_state = button_b.value
        if button_b_state: press_b()
    if switch.value is not switch_state:
        switch_state = switch.value
        flip_switch()

def press_b():
    global shader_index
    shader_index = (shader_index + 1) % len(SHADERS)

def flip_switch():
    global power

    if switch_state:
        power = True
    else:
        if power:
            power = False
            pixels.fill((0, 0, 0))
            pixels.brightness = 0.0
            pixels.show()

def show_timer(shader):
    for frame in range(20):
        frame_sleep = shader(frame)
        pixels.show()
        event_sleep(frame_sleep)

def shader_breathe(frame):
    color = (255, 0, 0)
    idx = frame if frame < 10 else frame - ((frame - 10) << 1)
    gamma = LOG_10[idx]

    for pixel in range(10):
        pixels[pixel] = list(map(lambda c: math.ceil(gamma * c), color))

    if(gamma == 1.0): return random.randrange(1, 50, 1) / 10
    elif(gamma == 0.0): return 2.0
    else: return 0.2

def shader_sparkle(frame):
    for pixel in range(10):
        redgreen = round(random.random(), 2)
        gamma_palette = redgreen, redgreen, round(random.random(), 2) / 10
        color = 15 + ((pixel & 3) * 80)
        pixels[random.randrange(10)] = list(map(lambda g: math.ceil(color * g), gamma_palette))
    return 0.05

def shader_rainbow(frame):
    for pixel in range(10):
        color = (0, 0, 0)
        base = (pixel % 3) * 60
        if pixel <= 2 or pixel == 9: color = (100 - int(base / 2), base, 0)
        elif pixel <= 5: color = (0, 200 - base, base)
        else: color = (base, 0, 200 - base)
        pixels[(pixel + frame) % 10] = color
    return 0.05

# Constants
LOG_10 = [0.0, 0.3010, 0.4771, 0.6021, 0.6990, 0.7782, 0.8451, 0.9031, 0.9542, 1.0, 1.0]
SHADERS = [ shader_sparkle, shader_breathe, shader_rainbow ]

# Default state
power = switch_state
last_time_seconds = time.time()
shader_index = 0

while True:
    if power:
        pixels.brightness = 1.0
        show_timer(SHADERS[shader_index])
    else:
        event_sleep(1.0)