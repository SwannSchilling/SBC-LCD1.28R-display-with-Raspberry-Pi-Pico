import os, sys
import board
import busio
import terminalio
import displayio

import adafruit_st7789
import time
import gifio
import gc9a01

import gc

# Release any resources currently in use for the displays
displayio.release_displays()

# 3V3               -> VCC
# GND               -> GND
# GPIO 19(MOSI)     -> SDI(MOSI) DIN
# GPIO 18(SCK)      -> SCK CLK
# GPIO 17           -> CS
# GPIO 27           -> DC
# GPIO 26           -> RESET RST
# GPIO 28           -> LED BL
tft_clk = board.GP18 # must be a SPI CLK
tft_mosi= board.GP19 # must be a SPI TX
tft_rst = board.GP26
tft_dc  = board.GP27
tft_cs  = board.GP17
tft_bl  = board.GP28
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)

# Make the displayio SPI bus and the GC9A01 display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = gc9a01.GC9A01(display_bus, width=240, height=240, backlight_pin=tft_bl)

# Make the main display context
main = displayio.Group()
display.show(main)
# end of setup
# ------------------------------------------------------------------------------------------

#=======================================
info = os.uname()[4] + "\n" + \
       sys.implementation[0] + " " + os.uname()[3] + "\n" + \
       adafruit_st7789.__name__  + " " + adafruit_st7789.__version__  + "\n" + \
       str(display.width) + "x" + str(display.height)
print("=======================================")
print(info)
print("=======================================")
print("CircuitPython play GIF")
print()
time.sleep(5)

splash = displayio.Group()
display.root_group = splash

def showGIF(gif):
    odg = gifio.OnDiskGif(gif)  # Create an OnDiskGif object with the given file.

    print("------------------")
    print("GIF:", gif)
    print("W x H:", odg.width, "x", odg.height)
    print("frame_count:", odg.frame_count)
    gc.collect()
    print(gc.mem_free())

    odg.next_frame() # Load the first frame

    face = displayio.TileGrid(
        odg.bitmap,
        pixel_shader=displayio.ColorConverter(
            input_colorspace=displayio.Colorspace.RGB565_SWAPPED
        ),
        x = int((display.width-odg.width)/2),
        y = int((display.height-odg.height)/2),
    )
    splash.append(face)
    display.refresh()

    for r in range(odg.frame_count-1):
        odg.next_frame() #load next frame

    splash.remove(face)

gifFiles = ("/GIF/GIF_01.gif","/GIF/GIF_01.gif",)

while True:
    for f in gifFiles:
        showGIF(f)
