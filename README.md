#  RFID RaspberryPI Communication system
This project implements a lightweight  RaspberryPi 3 b +  server and Keyboard Emulation(HID) RFID  reader connected to a client Communication system designed for Raspberry Pi devices. It enables secure port connection and communication between the server and a client(multiple) its designed in Python Flask in LAN network and Endev library for reading the specific keyboard interface RFID reader. its designed for study purposes and has capabilities to be upgradable. 
## 1. Main Components
### U will need:
- two or more RaspberryPi's 3 b + if you need. or any other model 'listed below' could work two,
- 2x  Micro USB Adapter for power for the RaspberryPI
- A PC or an laptop with 2 or more USB gen 3.0 or gen 2.0 ports for the main power to RPi (If you dont have an alt. PC Laptop, use Phone USB A adapterand plug it into power) But at least laptop reccomended for SSH
- one or more Neuftech, or any other Keyboard in interface USB Emutation(HID) RFID Reader Cable comes included. Link: ()
- An USB A/bluetooth keyboard and a bluetooth/USB A mouse.
- An Installation Media(USB flash drive/s or an micro SD card/s, maybe you will need the micro SD card reader and adapter to connect Micro SD card into it. Link: ()
- An External Monitor (if you Have an PC),
- An HDMI Cable or two,
- Recommended SSH protocol or tool Putty etc.. (i will use Putty).

## Initalization
### 1. iso Instalation:
Get the ISO file <a href="https://www.raspberrypi.com/software/">Here</a> and plug the instalation media into your PC or laptop etc. When the Imager will download open it and select an RPi Model, RPI OS and your usb drive. Then  click ```Next```, ```edit settings```(edit settings on your preferences)", than ```yes```, and ```yes``` and then it will start the download for your ISO file. <a href="https://youtu.be/DRJAILbqjy0?si=Bjus8FsSx8V6RNjL">Full step guide how to install RPi OS</a><h5 style="font-weight: bold; font-color: #14a3e0;">!! Important ignore the Windows unable to format the drive error !!</h5>If you have windows as I did the format drive message will show up. Ignore it, beacause RaspberryPi OS is A Linux system and widows cant recognize it. if you have Linux the error message might not show up.
When the error message shows/or not(depending on your OS),  unplug the drive. 

### 2. Hardware preparation:
Plug both power w Micro USB and display with HDMI out your monitor and  the mouse and keyboard in the RPi. Install your operating system, and connect RPi to your LAN network 
(I reccomend that you remember the password because then you cant acces the RPi from SSH.)

### 3. IP Configuration:
Open terminal on the taskbar, and type ```ifconfig``` then look at the  IPv4 addres that resambles your IP exm. ```192.168.0.xxx.``` (i reccomend that you save and decide whitch ip will be the RPi ```server``` and which one(or more) will be the  ```client```

### 4. SSH Configuration:
On All RaspberryPi's Configure SSH by opening the terminal and typing ```sudo raspi-config``` and then navigating to ```interface Options``` and enabling SSH protocol by selecting ```yes```.
When you have all those steps enabled you can install Putty a free SSH client for windows <a href="https://www.putty.org/">Here</a>. 
When you installed Putty open it by pressing ``` 🪟 + S```  on windows or ```^ + S``` on linux and typing putty.
Then Putty Will open and you can type the Required IPv4 address of the writed down IPv4 address of RaspberryPi in your LAN network. exm. ```192.168.0.yyy```.
Then you will need to sign in with your existing username and password as you created on the RPi with the same IPv4 as that one that you connected via putty with.
When both username and  password will be correct, ssh/putty will grant acces to your RPi's terminal. It will say something like this: ```raspberry2@raspberrypi:~ $```

### 5. python libraries  and creating an virtual envroviement:
When you have putty connected to all RPi IP addresses of RaspberryPi's, and decided whitch RPi will be the server and whitch one(or more) the client, you need to create a virtual envroviement for your exm. ```server.py``` and 
 ```client1,2...``` file because RasberryPi OS comes with preinstaled python. 

To check if you have Python just run ```python3 --version``` or ```python3 -V```.
On the All RaspberryPi's run ```sudo apt-get update```.
When the update is finished run ```sudo apt install python3-venv``` to install packages and then run ```python3 -m venv ~/venv``` to create your virtual envrovienment.
Then you will need to activate your Virtual envrovienment by running this command ```source venv/bin/activate```. (do it on all RPi's via putty)

When your Virtual envrovienment is activated it will show this ```(venv) raspberry2@raspberrypi:~ $```. Now you can install Flask requests and Endev library.

Run theese commands: ```sudo apt-get update```, ```pip3 install flask requests``` and ```sudo apt install python3-evdev```.
that will install all of libraries that you need for this project.

### 6. Creating python files and an templates folder:
When you created the virtual envroviement the directory venv appeared in your desktop exm. ```/home/username/```
when you have VENV still activated, and server Rpi decided run the command ```nano server.py``` on the server RPi via Putty and press enter.
You will create a new file named server.py in nano editor, and then 

