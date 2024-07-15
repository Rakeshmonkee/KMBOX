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
Connect your USB Cables to the kmbox via the respective ports as seen in the image below

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

After the driver has been installed, your KMBox has been setup. Follow to the Flashing part below

## Flashing

To flash firmware to your KMBox B+ check the Firmware Section above, or visit [kmbox.top](http://www.kmbox.top/BPro_firmware.html) for the latest firmware

You will also need to install [uPyCraft.exe]()


