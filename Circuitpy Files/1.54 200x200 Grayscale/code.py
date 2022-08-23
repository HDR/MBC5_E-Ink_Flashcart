import time
import board
import displayio
import busio
import os
import adafruit_ssd1681

print("Updating Display")
displayio.release_displays()

display_bus = displayio.FourWire(
    busio.SPI(board.GP10, board.GP11), command=board.GP8, chip_select=board.GP9, reset=board.GP12, baudrate=1000000
)

time.sleep(1)

display = adafruit_ssd1681.SSD1681(
    display_bus, width=200, height=200, busy_pin=board.GP13, rotation=180
)

def loadBMP(pic):
    g = displayio.Group()
    t = displayio.TileGrid(pic, pixel_shader=pic.pixel_shader)
    g.append(t)
    display.show(g)
    display.refresh()

for file in os.listdir('/'):
    if file.endswith(".bmp"):
        pic = displayio.OnDiskBitmap(file)

try:
    loadBMP(pic)
except NameError:
    loadBMP(displayio.OnDiskBitmap('/assets/hdr.bmp'))

