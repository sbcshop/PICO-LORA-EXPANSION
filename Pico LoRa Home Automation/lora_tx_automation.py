#Transmiter code
import utime
from machine import UART
from machine import Pin
import Lcd1_14driver#lcd driver

lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

push_button_1 = Pin(20, Pin.IN, Pin.PULL_DOWN)#connect button at pin 20 of pico
push_button_2 = Pin(19, Pin.IN, Pin.PULL_DOWN)#connect button at pin 19 of pico
push_button_3 = Pin(18, Pin.IN, Pin.PULL_DOWN)#connect button at pin 18 of pico

push_button_1.value(0)#initally button at LOW
push_button_2.value(0)#initally button at LOW
push_button_3.value(0)#initally button at LOW

LCD = Lcd1_14driver.Lcd1_14()

LCD.fill(LCD.white) 
LCD.lcd_show()
        
LCD.text("SB-COMPONENTS PICO LORA",30,10,LCD.red)
LCD.text("HOME AUTOMATION",50,30,LCD.red)
LCD.text("TRANSMITTER",70,50,LCD.red)
LCD.text("Button 1 Press for relay 1", 10,70,LCD.blue)# print on tft screen
LCD.text("Button 2 Press for relay 2", 10,90,LCD.blue)# print on tft screen
LCD.text("Button 3 Press for relay 3", 10,110,LCD.blue)# print on tft screen
LCD.lcd_show()


while True:
    if push_button_1.value()== 1:
        lora.write("A")#send "A"
        print("A")
        
    if push_button_1.value()== 0:
        lora.write("X")#send "X"
        print("X")
        
    if push_button_2.value()== 1:
        lora.write("B")#send "B"
        print("B")
        
    if push_button_2.value()== 0:
        lora.write("Y")#send "Y"
        print("Y")
        
    if push_button_3.value()== 1:
        lora.write("C")#send "C"
        print("C")
        
    if push_button_3.value()== 0:
        lora.write("Z")#send "Z"
        print("Z")
        
    utime.sleep(0.2)#wait 200ms
#Transmitter code Ends here
