# KMBOX B+ / Pro

## Content
- [Firmware]()
- [Tutorial]()
- [Flashing]()
- [Spoofing]()


## Firmware


| Date       |  Name                                     |
|------------|-------------------------------------------|
| Latest     |  [kmboxB+ quad-port firmware 20240701.bin](http://www.kmbox.top/wiki_doc/firmware/kmboxB/latest/kmboxB+20240701.bin) |
| 2024-05-16 |  [	kmboxB+ firmware 20240516.bin](http://www.kmbox.top/wiki_doc/firmware/kmboxB/history/kmboxB+%E5%9B%BA%E4%BB%B620240516.bin) |
| 2024-04-17 |  [kmboxB+ firmware 20240417.bin](http://www.kmbox.top/wiki_doc/firmware/kmboxB/history/kmboxB+%E5%9B%BA%E4%BB%B620240417.bin) |

last updated: 07/01/2024

## Setting up

### 1. Connecting USB cables to KMBox
Connect your USB Cables to the KMBox via the respective ports as seen in the image below

![Kmbox B+](https://github.com/user-attachments/assets/7a961aab-f81c-4cc5-bf05-de598fcc06f8)

The Main PC USB goes into the PC port (bottom left)

The Second PC USB goes into the COM port (top left)

The mouse and keyboard go into any port on the right side of the KMBox

### 2. Driver installing

On the second PC after plugging the USB into the COM port on the KMBox, you should see a USB Serial Device under Other Devices within Device Manager as seen in the image below

![image](https://github.com/user-attachments/assets/070d40b0-754c-49dc-b459-a2a825f976c3)

If you see this, Download [CH341SER.EXE](https://www.wch.cn/downloads/file/65.html?time=2023-03-17%2016:47:34&code=DZOI4uB6P0dEfCxL0bp5AGLyOaggJMAb025ICJEt?time=2024-07-15%2012:09:09&code=bHjmlFZUgldeCHSHm0N9q3Ogcifv7sUpcTIS1BTV), or visit [WCH-IC](https://www.wch-ic.com/downloads/CH341SER_EXE.html) for CH341SER.EXE

After running CH341SER.exe you should have an option to install CH341SER.INF, click on the install button.

If the install was successful, you should get a popup saying "Driver install success"

You can then check to see if the driver was installed in Device Manager, and if installed correctly, you should see a USB-SERIAL CH340 (COM4) Device under Ports(COM & LPT) as seen in the image below

![image](https://github.com/user-attachments/assets/c02bdde7-0345-4659-9bd6-e544a3ff5771)

After the driver has been installed, your KMBox has been set up. Follow the Flashing part below

## Flashing

To flash firmware to your KMBox B+ check the Firmware Section above, or visit [kmbox.top](http://www.kmbox.top/BPro_firmware.html) for the latest firmware

You will also need to install [uPyCraft.exe](https://github.com/Rakeshmonkee/KMBOX/blob/main/KMBOX%20B%2B/uPyCraft.exe) or visit [uPyCraft Github](https://github.com/DFRobot/uPyCraft_src) for the source code if you want to run the program manually via your Python interpreter

After you have installed uPyCraft.exe and the latest version of the KMBox firmware, run uPyCraft.exe

Within uPyCraft click on the tools button in the header section and click Burn Firmware

Make sure to follow the settings below

Board: esp32
Burn_addr: 0x1000
erase_flash: yes
com: com of the KMBox
Firmware: bin file of the latest KMBox firmware

to check the com of your KMBox, go to Device Manager and back under Ports (COM & LPT) look for the USB-SERIAL CH340

After the CH340, there should be a COM x, with x representing the number. See the image below for example. So in my case, since my COM is COM4 I will choose COM4.

![image](https://github.com/user-attachments/assets/dece3122-5d24-4092-b85c-677025fe20f2)

Image showing everything selected correctly

![image](https://github.com/user-attachments/assets/33913a11-a710-4ad8-bbaf-3134d1ec8619)

Image showing the flashing

![image](https://github.com/user-attachments/assets/97bced60-3b19-43d3-a72a-d05adf0fbe74)

Once the flash has been successful, the screen on the KMBox should restart and should display the latest firmware version on the bottom of the screen.

To test that the KMBox is working successfully, run the KMBoxBTest.py file above. input the COM port number and you should see your mouse move in a positive and negative direction on the x and y axis.

> [!Warning]
> 
> Unless you are from china and have Chinese encoding on your computer, I do not recommend downloading the latest firmware version (20240701) as you will have errors. If you install this firmware, your KMBox screen will tell you to activate the firmware. When trying to activate the firmare using the activation program, an error saying "The softwares file name had been changed" this is due to encoding issues with the file name. Follow below if you have chinese encoding and the file name appears properly, not in a random encoded format.

Download [KMBOXB Activator](http://www.kmbox.top/tools/kmboxBcheck.zip)

After running the program, input the COM port number, and hit the activate button, your kmbox should then activate.

