# KMBOX B+ / Pro

## Content
- [Firmware](https://github.com/Rakeshmonkee/KMBOX/blob/main/KMBOX%20B+/readme.md#firmware)
- [Setting Up](https://github.com/Rakeshmonkee/KMBOX/blob/main/KMBOX%20B+/readme.md#setting-up)
- [Flashing](https://github.com/Rakeshmonkee/KMBOX/blob/main/KMBOX%20B+/readme.md#flashing)
- [Spoofing](https://github.com/Rakeshmonkee/KMBOX/blob/main/KMBOX%20B+/readme.md#spoofing)


## Firmware


| Date       |  Name                                     |
|------------|-------------------------------------------|
| Latest     |  [20240724.bin](https://gitee.com/ccironmgr/kmbox_resources/blob/master/firmware/bplus/latest/kmboxBpro%E5%9B%BA%E4%BB%B620240724.bin) |

last updated: 08/01/2024

### Obtaining firmware through the terminal

If you don't want to make an account with gitee to download the kmbox firmware, there is an alternative using your terminal and git.

if you have git installed, you can copy this link address: ```git clone https://gitee.com/ccironmgr/kmbox_resources.git``` ,and paste it into the terminal.

![image](https://github.com/user-attachments/assets/884c07f1-60cb-4f41-a351-36f066f24573)

Hit enter, and git clone information will be printer to the terminal.

![image](https://github.com/user-attachments/assets/c5542587-da85-4849-bf57-77c7aeac3245)

After it says `Resolving deltas: 100% (68/68), done.`, the clone has been successful.

The location of the installation will be the directory the terminal is open in. If you git clone the url on ```C:\Users\User\Desktop```, the folder will be on your desktop.

In my instance, the folder will be saved to the user directory `C:\Users\User` since that is where i did the git clone from.

The folder name should be called ```kmbox_resourcecs```. Navigate to `kmbox_resources/firmware/bplus/latest`. You should see the latest firmware binary file called `kmboxBpro ... .bin` where `...` is the date.

![image](https://github.com/user-attachments/assets/478dbd8a-f8bc-483c-b38a-311f252227e6)




## Setting up

### 1. Connecting USB cables to KMBox
Connect your USB Cables to the KMBox via the respective ports as seen in the image below.

![Kmbox B+](https://github.com/user-attachments/assets/7a961aab-f81c-4cc5-bf05-de598fcc06f8)

The Main PC USB goes into the PC port (bottom left).

The Second PC USB goes into the COM port (top left).

The mouse and keyboard go into any port on the right side of the KMBox.

### 2. Driver installing

On the second PC after plugging the USB into the COM port on the KMBox, you should see a USB Serial Device under Other Devices within Device Manager as seen in the image below.

![image](https://github.com/user-attachments/assets/070d40b0-754c-49dc-b459-a2a825f976c3)

If you see this, Download [CH341SER.EXE](https://www.wch.cn/downloads/file/65.html?time=2023-03-17%2016:47:34&code=DZOI4uB6P0dEfCxL0bp5AGLyOaggJMAb025ICJEt?time=2024-07-15%2012:09:09&code=bHjmlFZUgldeCHSHm0N9q3Ogcifv7sUpcTIS1BTV), or visit [WCH-IC](https://www.wch-ic.com/downloads/CH341SER_EXE.html) for CH341SER.EXE

After running CH341SER.exe you should have an option to install CH341SER.INF, click on the install button.

If the install was successful, you should get a popup saying "Driver install success".

You can then check to see if the driver was installed in Device Manager, and if installed correctly, you should see a USB-SERIAL CH340 (COM4) Device under Ports(COM & LPT) as seen in the image below.

![image](https://github.com/user-attachments/assets/c02bdde7-0345-4659-9bd6-e544a3ff5771)

After the driver has been installed, your KMBox has been set up. Follow the Flashing part below.

## Flashing

To flash firmware to your KMBox B+ check the Firmware Section above, or visit [kmbox.top](http://www.kmbox.top/BPro_firmware.html) for the latest firmware.

You will also need to install [uPyCraft.exe](https://github.com/Rakeshmonkee/KMBOX/blob/main/KMBOX%20B%2B/uPyCraft.exe) or visit [uPyCraft Github](https://github.com/DFRobot/uPyCraft_src) for the source code if you want to run the program manually via your Python interpreter.

After you have installed uPyCraft.exe and the latest version of the KMBox firmware, run uPyCraft.exe

Within uPyCraft click on the tools button in the header section and click Burn Firmware.

Make sure to follow the settings below.

Board: esp32
Burn_addr: 0x1000
erase_flash: yes
com: com of the KMBox
Firmware: bin file of the latest KMBox firmware

To check the com of your KMBox, go to Device Manager and back under Ports (COM & LPT) look for the USB-SERIAL CH340.

After the CH340, there should be a COM x, with x representing the number. See the image below for example. So in my case, since my COM is COM4 I will choose COM4.

![image](https://github.com/user-attachments/assets/dece3122-5d24-4092-b85c-677025fe20f2)

Image showing everything selected correctly

![image](https://github.com/user-attachments/assets/33913a11-a710-4ad8-bbaf-3134d1ec8619)

Image showing the flashing

![image](https://github.com/user-attachments/assets/97bced60-3b19-43d3-a72a-d05adf0fbe74)

Once the flash has been successful, the screen on the KMBox should restart and should display the latest firmware version on the bottom of the screen.

To test that the KMBox is working successfully, run the [KMBox_B_Test.py](https://github.com/Rakeshmonkee/KMBOX/blob/main/KMBOX%20B%2B/KMBox_B_Test.py). Input the COM port number and you should see your mouse move in a positive and negative direction on the x and y axis.

Depending if you have installed the serial library before or not you will need to:

1. Open command prompt as Admin
2. Install the serial library via this prompt > `pip3 install serial` and `pip3 install pyserial`.

After running the pip install command, this should install the serial module.

I recommend running the test using PyCharm Community edition so you can run the Python script in a virtual environment. You will need to select the Python interpreter if it is your first time installing it. 

To install the serial and pyserial library, click on Python Packages, and search for serial, under PyPi repository, it should show serial and Pyserial, click on them and install.

![image](https://github.com/user-attachments/assets/d0be4256-6309-4122-88af-52ce4637bf75)


## Spoofing

On uPyCraft click on Tools > hover over serials > click on the COM of your kmbox.

This should then make the device have a drop down in the left side of the GUI. Open boot.py

![image](https://github.com/user-attachments/assets/9c44dce4-3a90-435e-ab43-d68d96c4b3f2)


Within `Boot.py` remove the # symbol from lines 54, 56, and 58.

![image](https://github.com/user-attachments/assets/877861ac-26a7-4e4e-a2d4-46630688ceeb)


To find your Mouse VID and PID, go to Device Manager and look under Human Interface Device or Mouse and other pointers for your mouse. Right click > properties > details > Hardware IDs. Match your Mouse VID and PID with the VID and PID within `boot.py`.

![image](https://github.com/user-attachments/assets/4c692527-66d7-4ed7-b897-0f727b783c1d)

After changing the VID and PID within `boot.py` , go to tools, and click Download. After downloading, unplug your KMBox completely, and plug it back in to view the changes.

To see if your KMBox has been spoofed correctly, you can go to Device Manager and find a USB Composite Device listed under Universal Serial Bus Controllers.

Right click > properties > details > Hardware IDs.

You should then see the same VID and PID of your mouse.

![image](https://github.com/user-attachments/assets/7693ff96-7865-4e97-9600-973cdee88205)

