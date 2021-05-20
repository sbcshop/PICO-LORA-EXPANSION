# PICO LORA Expansion

Pico LoRa™ Expansion is a low-power consumption data transmission board, comes with an onboard CH340 USB TO UART converter, Voltage Level Translator(74HC125V), E22-900T22S/E22-400T22S SMA antenna connector that covers 868MHz/433MHz frequency band , Onboard 1.14" LCD,IPEX antenna connector, LoRa™ Spread Spectrum Modulation technology with auto multi-level repeating.

<img src="https://learn.sb-components.co.uk/images/9/94/Pico_lora_868.png" />

## How to use ?

### Board Details :



### Requirements

* Pico LORA Expansion: (Buy it from : https://shop.sb-components.co.uk/products/pico-dual-channel-relay-hat  )
* Raspberry Pi Pico (Buy it from : https://shop.sb-components.co.uk/collections/latest-collections/products/raspberry-pi-pico-board-with-header )
* USB Cable


## Steps :

### For Communication between two Pico Lora Expansion

* First take 2 LORA Expansion board and set jumper position as mention below:
  * <b> Mode Selection Jumper :</b> M0 - OPEN, M1 - Open (we are going to use PICO gpio pi GP2 and GP3 to control MODE Selection)
  * <b> Device Selection Jumper : </b> Set is as MODE 2 to enable PICO to LORA Communication

<b> For Board 1 </b>

* Stack Raspberry Pi Pico on both boards.
* Now connect USB Cable on USB Port of Pico 1.
* Open Thonny IDE and Choose interpreter as MicroPython (Raspberry Pi pico).

<img src="https://github.com/sbcshop/Raspberry-Pi-Pico-RFID-Expansion/blob/main/images/thonny-interpreter.PNG" />

* Now Create a file "Lcd1_14driver.py" as same content from PICO LORA Expansion's github repository in thonny ide, and save it in root location of first Raspberry Pi Pico with same name "Lcd1_14driver.py" (without quotes).
* Copy and Paste or Open "Broadcast_Demo.py" code in thonny ide.
* Click on green play button to run example of Pico LORA Expansion on Board 1, You can either save this file on root location of PICO or on your Computer drive.

<b> For Board 2 </b>

* Stack Raspberry Pi Pico on both boards.
* Now connect USB Cable on USB Port of Pico 2.
* Open Thonny IDE and Choose interpreter as MicroPython (Raspberry Pi pico).

<img src="https://github.com/sbcshop/Raspberry-Pi-Pico-RFID-Expansion/blob/main/images/thonny-interpreter.PNG" />

* Now Create a file "Lcd1_14driver.py" as same content from PICO LORA Expansion's github repository in thonny ide, and save it in root location of second Raspberry Pi Pico with same name "Lcd1_14driver.py" (without quotes).
* Copy and Paste or Open "Broadcast_Demo.py" code in thonny ide.
* Click on green play button to run example of Pico LORA Expansion on Board 2, You can either save this file on root location of PICO or on your Computer drive.

<b> Once setup both board successfully, you can notice that both board are sending text to each other </b>
You can change below variable to change transmitting text :

``` txData = b'hellow world' ``` 

Put your text between single quote.
