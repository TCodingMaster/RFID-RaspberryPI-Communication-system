#  RFID RaspberryPI Communication system
"This project implements a lightweight server for the Raspberry Pi 3 B+ and a keyboard emulation (HID) RFID reader, enabling communication with clients. Built using Python Flask and the Endev library, it facilitates secure port communication between the server and one or more clients. The system integrates an SQLite database for user management and includes a web interface for data visualization. Designed for study purposes, it is easily upgradable for expanded functionality and designed in Slovenian Language."
##  Main Components
### You will need:
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
### 1. ISO Instalation:
Get the ISO file <a href="https://www.raspberrypi.com/software/">Here</a> and plug the instalation media into your PC or laptop etc. When the Imager will download open it and select an RPi Model, RPI OS and your usb drive. Then  click ```Next```, ```edit settings```(edit settings on your preferences)", than ```yes```, and ```yes``` and then it will start the download for your ISO file. <a href="https://youtu.be/DRJAILbqjy0?si=Bjus8FsSx8V6RNjL">Full step guide how to install RPi OS</a><h5 style="font-weight: bold; font-color: #14a3e0;">!! Important ignore the Windows unable to format the drive error !!</h5>If you have windows as I did the format drive message will show up. Ignore it, beacause RaspberryPi OS is A Linux system and widows cant recognize it. if you have Linux the error message might not show up.
When the error message shows/or not(depending on your OS),  unplug the drive. 

### 2. Hardware preparation:
Plug both power w Micro USB and display with HDMI out your monitor and  the mouse and keyboard in the RPi. Install your operating system, and connect RPi to your LAN network 
(I reccomend that you remember the password because then you cant acces the RPi from SSH.)

### 3. IP Configuration:
Open terminal on the taskbar, and type: 
```bash 
ifconfig
```
 then look at the  IPv4 addres that resambles your IP exm. ```192.168.0.xxx.``` (i reccomend that you write it down and decide whitch ip will be the RPi ```server``` and which one(or more) will be the  ```client```

### 4. SSH Configuration:
On All RaspberryPi's Configure SSH by opening the terminal and typing 
```bash
sudo raspi-config
``` 
and then navigating to ```interface Options``` and enabling SSH protocol by selecting ```yes```.
When you have all those steps enabled you can install Putty a free SSH client for windows <a href="https://www.putty.org/">Here</a>. 
When you installed Putty open it by pressing ``` 🪟 + S```  on windows or ```^ + S``` on linux and typing putty.
Then Putty Will open and you can type the Required IPv4 address of the writed down IPv4 address of RaspberryPi in your LAN network. exm. ```192.168.0.yyy```.
Then you will need to sign in with your existing username and password as you created on the RPi with the same IPv4 as that one that you connected via putty with.
When both username and  password will be correct, ssh/putty will grant acces to your RPi's terminal. It will say something like this: ```raspberry2@raspberrypi:~ $```

### 5. python libraries  and creating an virtual envroviement:
When you have putty connected to all RPi IP addresses of RaspberryPi's, and decided whitch RPi will be the server and whitch one(or more) the client, you need to create a virtual envroviement for your exm. ```server.py``` and 
 ```client1,2...``` file because RasberryPi OS comes with preinstaled python. 

To check if you have Python just run: 
```bash
python3 --version
```
 or alternative:
 ```bash
 python3 -V˛
```

On the All RaspberryPi's run: 
```bash
sudo apt-get update
```

When the update is finished run: 
```bash
sudo apt install python3-venv
```
to install VENV and then run: 
```bash
python3 -m venv ~/venv
```
to create your virtual envrovienment.
Then you will need to activate your Virtual envrovienment by running this command: 
```bash
source venv/bin/activate
```
(do it on all RPi devices allso clients and connect to them via putty)
### 6. Installing requested python liraries
When your Virtual envrovienment is activated it will show like this ```(venv) raspberry2@raspberrypi:~ $```. Now you can install Flask, requests, SQLITE and Endev library.

Run theese commands: 
```bash
sudo apt-get update
```
 ```bash
pip3 install flask requests #This library is for the server
```
 ```bash
 sudo apt install python3-evdev #This library is for reading output from RFID reader
```
```bash
sudo apt-get install sqlite3 #this library is for required data base.
```
That will install all of libraries that you need for this project.

### 7. Creating python files and an templates folder:
When you created the virtual envroviement the directory venv appeared in your desktop exm. ```/home/username/```.
 If you have VENV still activated, and server Rpi selected run this command 
```bash
nano server.py
```
If not Activate it by running:
```bash
source venv/bin/activate
```
on the server RPi via Putty and press enter.
You will create a new file named server.py in nano editor. Then paste ```RFID_server.py``` code from my repository.
When creating the file server.py and pasting the code in the file ```server.py```, its time to assemble the  ```app_route()``` for linking the path for the ```index.html``` page.


## 8. Code setup ```server.py```
### Pasting the code to ```server.py``` might be easy but please change the code that the ```server.py``` will funciton correctly:
- Please change the example IP of server  ```192.168.0.100``` to the existing IPv4 address of the selected ```server``` RaspberryPi
- When the server RPi IP is choosed rightyou can integrate ```@app.route('/')``` in ```server.py``` path for ```index.html``` webpage.
 ### The code will look something like this:
```python
# Other code 
@app.route('/')
def home():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Active sessions
    c.execute("SELECT rfid, start_time FROM active_sessions")
    active = c.fetchall()
    active_info = []
    for rfid, start_time in active:
        c.execute("SELECT name FROM users WHERE rfid=?", (rfid,))
        user = c.fetchone()
        name = user[0] if user else "Neznan"
        active_info.append({'rfid': rfid, 'name': name, 'start_time': start_time})

    # Finished sessions
    c.execute("SELECT rfid, name, start_time, end_time, duration FROM sessions ORDER BY id DESC LIMIT 20")
    sessions = c.fetchall()

    conn.close()
    return render_template('index.html', active=active_info, sessions=sessions)
    # Hosting Port Code: if __name__ == '__main__': etc...
  ```
 Write/save the file by pressing ```^ + O``` on linux or ```ctrl + O``` on windows, and then quit nano editor by pressing ```^ + X``` on linux or ```ctrl + X``` on windows.

### 9. Creating an ```add_user.py``` connected to an SQLITE database file:
In the opened terminal and VENV activated run this command to open nano once again:
```bash
nano add_user.py
```
in blank Nano editor paste the included code ```add_user.py```from the repository.
Code will look something like this: 
```python
# add_user.py
import sqlite3

rfid = input("Enter the RFID code: ")
name = input("Enter the user name: ")

conn = sqlite3.connect('rfid_system.db')
c = conn.cursor()
c.execute("INSERT OR REPLACE INTO users (rfid, name) VALUES (?, ?)", (rfid, name))
conn.commit()
conn.close()

print(f"User {name} added.")
```
Write/save the file by pressing ```^ + O``` on linux or ```ctrl + O``` on windows, and then quit nano editor by pressing ```^ + X``` on linux or ```ctrl + X``` on windows.

 ### 10. Creating an ```index.html``` file connected to ```server.py``` file to display results:
- Please be sure you have VENV still activated and then run theese commands to create an index.html file:
 ```bash
  mkdir -p templates
```
and then create an ```index.html``` file by running this command:
```bash
nano templates/index.html
```
That will open an newly created index.html file in nano editor.
### 11.  Pasting ```index.html``` code to your ```index.html``` file: 
Simply paste the code from ```index.html``` from the repository to your ```index.html``` file in nano editor.
### 12. When pasting the code Write/save the file by pressing ```^ + O``` on linux or ```ctrl + O``` on windows and quit nano editor and run:
```bash
python3 server.py
```
to ensure the server is running propperly.
check on what port are you and visit 
```http://<your_pi_server_ip>:5000``` or ```http://localhost:5000```

### 13. Obtaining Endev /dev/input/number_path for Client INPUT for RFID reader:
When you downloaded Endev library  it said step 6. and connected via Putty on all RPi devices its time to discover the usb port that the Reader is connected to.
In connected terminal type: 
```bash
python3 -m evdev.evtest
```
It will show something like this: 
```bash
---------------------------------------------------------------------------------------------------------------------------------
0   /dev/input/event0    vc4-hdmi                            vc4-hdmi/input0    
1   /dev/input/event1    vc4-hdmi HDMI Jack                  ALSA               
2   /dev/input/event4    Sycreader RFID Technology Co., Ltd SYC ID&IC USB Reader usb-3f980000.usb-1.1.2/input0       08FF20140315
```
When the output shows, find the port that the USB RFID reader is conected to and remember the ```/dev/input/event_number``` because you will need the ```/dev/input/event_number``` in your ```client.py``` code.
when you remembered the ```/dev/input...```  
## 14. ```Client.py``` Code setup:
When the ```dev/input/..``` is remembered, you can start with ```client```(or multiple) setup
Now you need to select the other RPi to be a client. If you have more RPi devices you will create multiple ```client1.py```, ```client2.py``` etc... files  as you will sign in via Putty.
Make sure to have VENV enabled and now create this files on each RPi separate, e.g. rp1 should be ```client1.py``` rpi2 should be ```client2 etc.``` by running this command:
```bash
nano clent1.py #that many client.py file as how much RPi devices(clients) do you have.
```
#### in each nano ```client.py``` paste the code: ```Client.py``` from the repository and change theese parts: 
```python
#import code and start flask app

SERVER_URL = 'http://192.168.0.100:5000/rfid_event'  # Change to the IP of the server.
DEVICE_ID = 'A'  # Change to B,C,D,... for the next other clients.
RFID_INPUT_PATH = '/dev/input/event0'  #change the right /dev/input/event.. path for USB RFID reader.

#other code..
```
## 15. When changing theese parts of code you are allmost finished with the project and the last thing you will need to do is to start the both clients.
start them one by one by typing this command:
```bash
python3 client1.py
```
```bash
python3 client2.py #or 3,4,5 etc. according how many clients to you have
```
# Thanks for visiting the page 🤍

## the links for buying the items ↓↓↓
 #### - <a href="https://www.amazon.de/-/en/Neuftech-RFID-Reader-Contactless-EM4100/dp/B018OYOR3E/ref=sr_1_1?crid=3POXC2T5M0OVH&dib=eyJ2IjoiMSJ9.LGYouj3pKNgQSCnFOV7i94jdSSA4B2FrmNY-ORbNNWTNMlCVDHkky0CJVAveKUxk2V7MhM9Pq64IwL47OXtOKpjhnt1oq6d2XTpi7laUBGIqNHHQwKwacTnqvsgbUnR1_h9gCYhmO796QXIdwNj7Mi5bjAERb6WsQqlvavWlcNDzNFk3U6MSkrhhX0qmIZHbMfHnCId9HrSc_Nn3srOgrCho6n4sQxmn89EzsUZseuc.rbYKU8wbwMrl6bJesCflwhEYggzoGnt9BboIwXHKRiM&dib_tag=se&keywords=neuftech+RFID+Reader&qid=1744798884&sprefix=neuftech+rfid+reade%2Caps%2C560&sr=8-1">Neuftech USB RFID Reader</a>
#### - <a href="https://www.amazon.de/-/en/Raspberry-Model-Board-1GB-Plus/dp/B0BNJPL4MW/ref=sr_1_3?crid=23QRYLE69OPJ6&dib=eyJ2IjoiMSJ9.kT6YfutOjwKMh4swpKAvfVf60PRETROhPDFxvhPqpPCRkLH5rDYNMgoyFqxFn8H3inzrCJmlpK9VJiXoFM4Z7Z4jjLWoP_acQVxooDo_WEoiV-ViToK2QGfUXHMEJCxhQS5iiIswNtNuiDBP8Hmh3gW_u7zgK9LuE8LyX2uh8bn8OhlNtzHEIP9LCfoyvuS5MJReNesXxsYKZZm9R_c74vjh2VxsrVXX4VihR92TbE4.sIr9s0Z1Zhx6x6UUOhkuUSBp9dZCken_rI5JY6lDTUY&dib_tag=se&keywords=raspberry+pi+3b+%2B&qid=1744799017&sprefix=raspberry+pi+3b+%2B%2Caps%2C146&sr=8-3">RaspberryPi 3 b +</a>
#### - <a href="https://www.amazon.de/-/en/SC1112-Raspberry-Pi-5-8gb/dp/B0CK2FCG1K/ref=sr_1_3?crid=1W7IHU8CZE83E&dib=eyJ2IjoiMSJ9.ptP7J3FZcmbYoZvFxUp_Vsja9oTthOJvFk_ZWVEluAx_PsrLrlD8qyVgiL2fDZ7n_MGA5gtdJOHPSi-G1afxUjM2MMgwg1VJvMnW-mqGNo7rZtZWk_OrygiUFUXE4LlbqNriQek9DIFA3yn-URi-tT1MGPdrJC4TyisMd6O4-pMhTWQXdV4I5NYKYb7x5QTHwP7eJFTeE8N2okW9oBRBepjpYNgs6jwAEHCPX0QEPgw.pA1Xii_GAR5PdVjDE_BvZ9LFDmNyUO8aTamoXvoE4CA&dib_tag=se&keywords=raspberry%2Bpi&qid=1744799083&sprefix=raspberry%2Bpi%2Caps%2C137&sr=8-3&th=1">Raspberry Pi 5 8gb</a>
#### - <a href="https://www.amazon.de/-/en/Raspberry-Pi-Model-GB/dp/B07TGBLK33/ref=sr_1_5?crid=1S53RGOATDPVM&dib=eyJ2IjoiMSJ9.Ecc4WqoL9GzQPna5ZAtas3tOERLYHnomX6lsUs_zQ2vzAQzUunYZ67leL7srYPPL4V87_uM7-RULC4OAmezyS-7X38WWzk_BlGdDgutOqDeB3xExPRZ54A2CG-sZIiKgYEahdb57yn5zw92lRTa3MNdbKsYpCwiwKF3aCvC_J7Jakb2HkOSADQgUIm9m_qGCp4PG1jpn5YSEf3JYtiSW8wXQ9IvOMMw033Eso5T8ZrU.ZraHwDPpH_G4YVA65LBV0ggcWnjv227hhMPLlZvgs3U&dib_tag=se&keywords=raspberry+pi+4&qid=1744799237&sprefix=raspberry+pi+4%2Caps%2C121&sr=8-5">RaspberryPi 4 2gb</a>



##### Designed by @TCodingMaster © 2025 SLO




