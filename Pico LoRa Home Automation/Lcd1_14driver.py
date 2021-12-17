from machine import Pin,SPI,PWM
import framebuf
import time

DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9


class Lcd1_14(framebuf.FrameBuffer):
    def __init__(self):
        self.width = 240
        self.height = 135
        
        self.cs = Pin(CS,Pin.OUT)
        self.rst = Pin(RST,Pin.OUT)
        
        self.cs(1)
        self.spi = SPI(1)
        self.spi = SPI(1,1000_000)
        self.spi = SPI(1,10000_000,polarity=0, phase=0,sck=Pin(SCK),mosi=Pin(MOSI),miso=None)
        self.dc = Pin(DC,Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)  #Red Green Blue (16-bit, 5+6+5) color format
        self.lcd_init_display()
        
        self.red   =   0x07E0
        self.green =   0x001f
        self.blue  =   0xf800
        self.white =   0xffff
        
    def lcd_write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def lcd_write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def lcd_init_display(self):
        """Initialize dispaly"""  
        self.rst(1)
        self.rst(0)
        self.rst(1)
        
        self.lcd_write_cmd(0x36)
        self.lcd_write_data(0x70)

        self.lcd_write_cmd(0x3A) 
        self.lcd_write_data(0x05)

        self.lcd_write_cmd(0xB2)
        self.lcd_write_data(0x0C)
        self.lcd_write_data(0x0C)
        self.lcd_write_data(0x00)
        self.lcd_write_data(0x33)
        self.lcd_write_data(0x33)

        self.lcd_write_cmd(0xB7)
        self.lcd_write_data(0x35) 

        self.lcd_write_cmd(0xBB)
        self.lcd_write_data(0x19)

        self.lcd_write_cmd(0xC0)
        self.lcd_write_data(0x2C)

        self.lcd_write_cmd(0xC2)
        self.lcd_write_data(0x01)

        self.lcd_write_cmd(0xC3)
        self.lcd_write_data(0x12)   

        self.lcd_write_cmd(0xC4)
        self.lcd_write_data(0x20)

        self.lcd_write_cmd(0xC6)
        self.lcd_write_data(0x0F) 

        self.lcd_write_cmd(0xD0)
        self.lcd_write_data(0xA4)
        self.lcd_write_data(0xA1)

        self.lcd_write_cmd(0xE0)
        self.lcd_write_data(0xD0)
        self.lcd_write_data(0x04)
        self.lcd_write_data(0x0D)
        self.lcd_write_data(0x11)
        self.lcd_write_data(0x13)
        self.lcd_write_data(0x2B)
        self.lcd_write_data(0x3F)
        self.lcd_write_data(0x54)
        self.lcd_write_data(0x4C)
        self.lcd_write_data(0x18)
        self.lcd_write_data(0x0D)
        self.lcd_write_data(0x0B)
        self.lcd_write_data(0x1F)
        self.lcd_write_data(0x23)

        self.lcd_write_cmd(0xE1)
        self.lcd_write_data(0xD0)
        self.lcd_write_data(0x04)
        self.lcd_write_data(0x0C)
        self.lcd_write_data(0x11)
        self.lcd_write_data(0x13)
        self.lcd_write_data(0x2C)
        self.lcd_write_data(0x3F)
        self.lcd_write_data(0x44)
        self.lcd_write_data(0x51)
        self.lcd_write_data(0x2F)
        self.lcd_write_data(0x1F)
        self.lcd_write_data(0x1F)
        self.lcd_write_data(0x20)
        self.lcd_write_data(0x23)
        
        self.lcd_write_cmd(0x21)

        self.lcd_write_cmd(0x11)

        self.lcd_write_cmd(0x29)

    def lcd_show(self):
        self.lcd_write_cmd(0x2A)
        self.lcd_write_data(0x00)
        self.lcd_write_data(0x28)
        self.lcd_write_data(0x01)
        self.lcd_write_data(0x17)
        
        self.lcd_write_cmd(0x2B)
        self.lcd_write_data(0x00)
        self.lcd_write_data(0x35)
        self.lcd_write_data(0x00)
        self.lcd_write_data(0xBB)
        
        self.lcd_write_cmd(0x2C)
        
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(self.buffer)
        self.cs(1)
