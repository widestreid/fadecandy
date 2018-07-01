from blink_oscillator import BlinkOscillator
from rgbw_color import RGBWColor

green = RGBWColor(0, 255, 0, 0)
red = RGBWColor(255, 0, 0, 0)
bo = BlinkOscillator(green, red, 50)

while True:
    frames = bo.get_frames(80)