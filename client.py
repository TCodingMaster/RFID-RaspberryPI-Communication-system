 # client.py
import requests
from evdev import InputDevice, categorize, ecodes

SERVER_URL = 'http://192.168.0.101:5000/rfid_event'  # Change to the correct ip of the 'server.py'
DEVICE_ID = 'A'  # change to B,C,D etc. for all other clients
RFID_INPUT_PATH = '/dev/input/event4'  # Correct path for reading output from USB RFID reader
def get_device():
    try:
        return InputDevice(RFID_INPUT_PATH)
    except FileNotFoundError:
        print("Napaka: RFID čitalnik ni najden.")
        exit()

def read_rfid(dev):
    tag = ''
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            data = categorize(event)
            if data.keystate == 1:  # Key Down
                key = data.keycode
                if key == 'KEY_ENTER':
                    return tag
                if 'KEY_' in key:
                    key = key.replace('KEY_', '')
                    if key.isdigit():
                        tag += key
                    elif key in 'ABCDEFGHIJKLMN':
                        tag += key.lower()

def send_to_server(tag):
    res = requests.post(SERVER_URL, json={'rfid': tag, 'device_id': DEVICE_ID})
    print(res.json()['message'])

if __name__ == '__main__':
    dev = get_device()
    print(f"Client {DEVICE_ID} pripravljen. Čakamo RFID...")
    while True:
        tag = read_rfid(dev)
        send_to_server(tag)