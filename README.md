# micropython-display-benchmark
Speed Draw Test for for each display (TFT, OLED, even LED matrix) that has at least 64x64 pixel rate. Micropython.

## How to use it
1) Download it
2) ampy --port /dev/ttyYOUR_DEVICE put benchmark.py
3) Conect to your micropython console, `import benchmark`

## Included benchmarks
```
Benchmark 1 - color full screen using 'fill_screen'
Benchmark 2 - invert screen using 'invert'
32x32 benchmarks:
Benchmark 3 - fill 32x32 rectangle using 'pixel'.
Benchmark 4 - draw lines in 32x32 rect using 'line'
Benchmark 5 - draw 16x16 rects using 'rectangle'
64x64 benchmarks:
Benchmark 6 - fill 64x64 rectangle using 'pixel'.
Benchmark 7 - draw lines in 64x64 rect using 'line'
Benchmark 8 - draw 32x32 rects using 'rectangle'
```
## Some benchmarks

[1]

    Device: ESP-12 + TFT7735
    Driver: https://github.com/hosaka/micropython-st7735/issues/1 - @hosaka's driver with @tmueller1970's correction
    Micropython version: MicroPython v1.9.3-8-g63826ac5c on 2017-11-01; ESP module with ESP8266
    
    #Turn 1
    10.0157	0.373703	3.97211	6.9016	7.7209	15.72	27.9025	110.898
    Total: 183.504
    #Turn 2
    10.012	0.377991	3.92401	6.89801	7.71997	15.705	27.9009	110.903
    Total: 183.441
