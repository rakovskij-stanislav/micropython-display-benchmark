print("SCREEN BENCHMARK by https://github.com/rakovskij-stanislav\n"
      "It helps to look at perfomance differences)\n"
      "This test is suitable for each display (TFT, OLED, LED matrix)\n"
      "that has at least 64x64 pixels")

# 1 - YOUR MODULE PREPARATION SCENE
from tft import TFT_GREEN
from machine import Pin, SPI, reset
dc  = Pin(5, Pin.OUT)
cs  = Pin(4, Pin.OUT)
rst = Pin(15, Pin.OUT)
spi = SPI(1, baudrate=8000000, polarity=1, phase=0)
t = TFT_GREEN(128, 128, spi, dc, cs, rst)
t.init()
t.clear(t.rgbcolor(255, 255, 255))
## 1 - END

# 2 - SET UNIVERSAL PARAMETERS FOR BENCHMARK
# You should remake this defs for your screen class

def line(x1, y1, x2, y2, r, g, b):
    # draw the line
    t.line(x1, y1, x2, y2,t.rgbcolor(r, g, b))
def fill_screen(r=255, g=255, b=255):
    t.clear(t.rgbcolor(r, g, b))
def invert(state):
    # state = 0 if do_not_invert else 1
    t.invert(state)
def pixel(x, y, r, g, b):
    # draw single pixel
    t.pixel(x, y, t.rgbcolor(r,g,b))
def rectangle(x1, y1, width, height, r, g, b):
    t.rect(x1, y1, width, height, t.rgbcolor(r, g, b))
# 2 - END

# 3 - benchmark. Do not change anything here
import utime
def timestamp():
    ans= str(utime.ticks_us()/1000000)
    return float(ans[:7])

print("Set benchmark count number (usually 2): ", end ='')
rara = int(input())
print("\nBenchmark 1 - color full screen using 'fill_screen'"
      "\nBenchmark 2 - invert screen using 'invert'"
      "\n#32x32 benchmarks"
      "\nBenchmark 3 - fill 32x32 rectangle using 'pixel'."
      "\nBenchmark 4 - draw lines in 32x32 rect using 'line'"
      "\nBenchmark 5 - draw 16x16 rects using 'rectangle'"
      "\n#64x64 benchmarks"
      "\nBenchmark 6 - fill 64x64 rectangle using 'pixel'."
      "\nBenchmark 7 - draw lines in 64x64 rect using 'line'"
      "\nBenchmark 8 - draw 32x32 rects using 'rectangle'")
for i in range(rara):
    print("\n#Turn", i+1)
    tt = timestamp()
    # 1
    for i in range(5):
        fill_screen(i*10, i*20, i*5)
    fill_screen()
    b1 = timestamp()-tt
    # 2
    for i in range(256):
            invert(1)
            invert(0)
    b2 = timestamp()-tt-b1
    # 3
    for i in range(32):
        for j in range(32):
            pixel(i, j, i*2, j*2, i+j)
    b3 = timestamp()-tt-b1-b2
    # 4
    for i in range(32):
            line(0, i, 31, 31-i, 100, 255, 100)
            line(i, 0, 31-i, 31, 12, 12, 255 )
    b4 = timestamp()-tt-b1-b2-b3

    # 5
    for i in range(16):
            for j in range(16):
                rectangle(i, j, 16, 16, i*10, j*10, 5*i+5*j)
    b5 = timestamp()-tt-b1-b2-b3-b4
    # 6
    for i in range(64):
        for j in range(64):
            pixel(i, j, i*2, j*2, i+j)
    b6 = timestamp()-tt-b1-b2-b3-b4-b5
    # 7
    for i in range(64):
            line(0, i, 63, 63-i, 100, 255, 100)
            line(i, 0, 63-i, 63, 12, 12, 255 )
    b7 = timestamp()-tt-b1-b2-b3-b4-b5-b6
    # 8
    for i in range(32):
            for j in range(32):
                rectangle(i, j, 32, 32, i*6, j*6, 3*i+3*j)
    b8 = timestamp()-tt-b1-b2-b3-b4-b5-b6-b7
    # result
    print(b1, b2, b3, b4, b5, b6, b7, b8, sep="\t")
    print("Total:", b1+b2+b3+b4+b5+b6+b7+b8)
