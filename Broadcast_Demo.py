'''
Project   :- PICO 1.14 inch lcd HAT
Developed :- SB-COMPONENTS
Date      :- 11/05/2021
Firmware  :- Demo code  for LORA AND 1.14inch LCD
CODE DISCREPTION :-
                    short jumper M0, short jumper M1: transmission mode
                    short jumper M0, open  jumper M1: configuration mode
                    open  jumper M0, short jumper M1: WOR mode
                    open  jumper M0, open  jumper M1: deep sleep mode
'''

import Lcd1_14driver
from machine import Pin,PWM,UART
import time #
import sys

txData = b'hellow world'

MODE = ["BROADCAST_AND_MONITOR","P2P"]

CFG_REG = [b'\xC2\x00\x09\xFF\xFF\x00\x62\x00\x17\x03\x00\x00',  
		   b'\xC2\x00\x09\x00\x00\x00\x62\x00\x17\x03\x00\x00']
RET_REG = [b'\xC1\x00\x09\xFF\xFF\x00\x62\x00\x17\x03\x00\x00',
		   b'\xC1\x00\x09\x00\x00\x00\x62\x00\x17\x03\x00\x00']
r_buff = ""
delay_temp = 1


LCD = Lcd1_14driver.Lcd1_14()

#------Mode pin declaration----- 
M0 = Pin(3,Pin.OUT)  # M0 and M1 FOR MODE SELECTION FOR LORA 
M1 = Pin(2,Pin.OUT)



BL = 13   # lcd back light pin declaration
class LoraOperation():
    def __init__(self):
        self.LoraUartInit()
        self.infoDevice()   #device information  and code version
        
    def infoDevice(self):
        LCD.fill(LCD.white) 
        LCD.lcd_show()
    
        LCD.hline(10,10,220,LCD.blue)
        LCD.hline(10,125,220,LCD.blue)
        LCD.vline(10,10,115,LCD.blue)
        LCD.vline(230,10,115,LCD.blue)       
        LCD.lcd_show()
        
        LCD.text("SB-COMPONENTS",70,40,LCD.red)
        LCD.text("PICO LORA ",70,60,LCD.red)
        LCD.text("EXPANSION",70,80,LCD.red)  
        LCD.lcd_show()
        time.sleep(2)
        LCD.fill(0xFFFF)
        
        LCD.hline(10,10,220,LCD.blue)
        LCD.hline(10,125,220,LCD.blue)
        LCD.vline(10,10,115,LCD.blue)
        LCD.vline(230,10,115,LCD.blue)       
        LCD.lcd_show()
        LCD.text("WAITING",70,40,LCD.red)
        LCD.lcd_show()
        time.sleep(2)
        x = 0
        for y in range(0,10):
             x += 4
             LCD.text(".",125+x,40,LCD.red)
             LCD.lcd_show()
             time.sleep(1)
             
    def LoraUartInit(self):
        self.uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
        
    def LoraDataSend(self,data):
        self.uart.write(data)
    def LoraReceivedData(self,RData):
        RData = self.uart.read(RData)
        if RData != "":
            print('Data found')
            return RData
        else:
            print('no data found ')
        #return RData
    def LoraModeSetConfig(self):
        M0.value(0)
        M1.value(1)
        time.sleep(1)
    def LoraModeSetTransparent(self):
        M0.value(0)
        M1.value(0)
        time.sleep(1)    
    

if __name__=='__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(100)
    pwm.duty_u16(32768)    #max value is 65535
        
    print("It's setting BROADCAST and MONITOR mode")
    Lora = LoraOperation()
    Lora.LoraModeSetConfig()
    Lora.LoraDataSend(CFG_REG[0])
    Lora.LoraModeSetTransparent()
    LCD.fill(LCD.white) 
    LCD.lcd_show()

    LCD.hline(10,10,220,LCD.blue)
    LCD.hline(10,125,220,LCD.blue)
    LCD.vline(10,10,115,LCD.blue)
    LCD.vline(230,10,115,LCD.blue)       
    LCD.lcd_show()

    while(True):
        delay_temp += 1
       
        if delay_temp > 1000:
            print('send broadcast message')
            
        
            LCD.text("MASSAGE BROADCAST",50,40,LCD.red)
            LCD.text("DATA =",50,60,LCD.red)
            LCD.text(txData,105,60,LCD.red)
            LCD.text("Recived DATA =",50,80,LCD.red)
            LCD.text(r_buff,135,80,LCD.red)
            LCD.lcd_show()
            
            Lora.LoraDataSend(txData)  # Send your message to Second/All Lora node
            
            delay_temp = 0
            time.sleep(1)
            r_buff = Lora.LoraReceivedData(10)
        if r_buff != "" :
            print("monitor message:")
            print(r_buff)
            r_buff = ""
		

					
