#Transmiter code
import utime
from machine import UART,SPI
from machine import Pin
import st7789
import time

import vga1_8x16 as font1
#import vga2_8x8 as font
import vga1_16x32 as font
import vga1_16x16 as font2

tx_data = "hello how are you"
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,135,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=3)

lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

def info():
    tft.init()
    utime.sleep(0.2)
    tft.text(font,"SB-COMPONENTS", 15,0)
    tft.fill_rect(15, 40, 210,10, st7789.RED)
    
    tft.text(font,"PICO LORA", 15,55,st7789.YELLOW)
    tft.fill_rect(15, 90, 210, 10, st7789.BLUE)
    time.sleep(1)
    tft.fill(0) #clear screen
    tft.text(font,"BROADCAST DATA", 5,10,st7789.WHITE)
    
    
    
info()


while True:
    lora.write(tx_data)#send data
    tft.text(font,tx_data, 5,50,st7789.YELLOW)
    print("A")
    utime.sleep(0.2)#wait 200ms
#Transmitter code Ends here
