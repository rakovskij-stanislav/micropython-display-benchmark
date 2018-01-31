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
## Some benchmark results

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
 
[2] (+ 7-10% speed in 'pixel' benchmarks vs [1]). +Adafruit's pixel() function port
```
Device: ESP-12 + TFT7735
Driver: https://github.com/hosaka/micropython-st7735/issues/1 - @hosaka's driver with @tmueller1970's correction + Adafruit's pixel() function port
Micropython version: MicroPython v1.9.3-8-g63826ac5c on 2017-11-01; ESP module with ESP8266
    
#Turn 1
10.0144	0.376305	3.616	6.9275	7.70369	14.4771	28.0244	110.836
Total: 181.976

#Turn 2
10.01	0.375977	3.638	6.927	7.71405	14.57	28.023	110.867
Total: 182.125
```
[3] (12x faster in 'fill_screen' test, 4.3x faster in 'rectangle x16', 7.7x faster in 'rectangle x32'). Adafruit's pixel() fill_rectangle() fill() functions port
```
Device: ESP-12 + TFT7735
Driver: https://github.com/hosaka/micropython-st7735/issues/1 - @hosaka's driver with @tmueller1970's correction + Adafruit's pixel() fill_rectangle() fill() functions port
Micropython version: MicroPython v1.9.3-8-g63826ac5c on 2017-11-01; ESP module with ESP8266
    
#Turn 1
0.832901	0.379894	3.6257	6.4893	1.789	14.5203	26.2593	14.3474
Total: 68.2437

#Turn 2
0.832794	0.376587	3.64551	6.4931	1.7955	14.6046	26.268	14.375
Total: 68.3911

```
