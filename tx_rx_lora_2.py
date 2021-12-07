import utime
from machine import UART
from machine import Pin
import Lcd1_14driver
import time
import vga1_bold_16x32 as font

txdata = "123456"
    
lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
LCD = Lcd1_14driver.Lcd1_14()#driver of lcd display

def lcd_border():
        LCD.hline(10,10,220,LCD.blue)
        LCD.hline(10,125,220,LCD.blue)
        LCD.vline(10,10,115,LCD.blue)
        LCD.vline(230,10,115,LCD.blue)       
        LCD.lcd_show()
    
def infoDevice():
        LCD.fill(LCD.white) 
        LCD.lcd_show()
        lcd_border()
        
        LCD.text("SB-COMPONENTS",70,40,LCD.red)
        LCD.text("PICO LORA ",70,60,LCD.red)
        LCD.text("EXPANSION",70,80,LCD.red)  
        LCD.lcd_show()
        time.sleep(2)
        LCD.fill(0xFFFF)
        
        LCD.text("WAITING.....",70,40,LCD.red)
        LCD.lcd_show()
        x = 0
        for y in range(0,1):
             x += 4
             LCD.text("......",125+x,40,LCD.red)
             LCD.lcd_show()
             time.sleep(1)
        
        
def tx_data_in_display():
    LCD.text(txdata,80,60,LCD.red)

    
def transmit_data():
    lora.write(txdata)
    
def receive_data():
        dataRead = lora.readline(6)# 6 denotes number of data in bytes(you can change as you can w.r.t application)
        tx_data_in_display()
        if dataRead is not None:
            print(dataRead)
            LCD.text(dataRead,135,80,LCD.red)
            LCD.text("DATA =",20,60,LCD.blue)
            LCD.text("Recived DATA =",20,80,LCD.blue)
            LCD.lcd_show()
            LCD.fill(0xFFFF)
           
infoDevice()

LCD.lcd_show()

while True:
    transmit_data()#for transmit data
    time.sleep(2)
    receive_data()#for receive data
    
    
#Receiver code Ends here
