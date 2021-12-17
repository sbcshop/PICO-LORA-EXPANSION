#Receiver code
import utime
from machine import Pin, UART,SPI
import time
import st7789

import vga1_8x16 as font1
#import vga2_8x8 as font
import vga1_16x32 as font
import vga1_16x16 as font2

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,135,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=3)

lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

def info():
    tft.init()
    utime.sleep(0.2)
    tft.text(font,"SB-COMPONENTS", 15,0)
    tft.fill_rect(15, 40, 210,10, st7789.RED)
    
    tft.text(font,"PICO WIFI HAT", 15,55,st7789.YELLOW)
    tft.fill_rect(15, 90, 210, 10, st7789.BLUE)
    time.sleep(2)
    tft.fill(0) #clear screen
    
    
    
info()



while True:
    data_Read = lora.readline()#read data comming from other pico lora expansion
    if data_Read is not None:
            tft.text(font2,data_Read, 5,55,st7789.WHITE)
            print(data_Read)
        #if data_Read is not None and "A" in data_Read:
    utime.sleep(0.5)#wait for 200ms 
    
 

