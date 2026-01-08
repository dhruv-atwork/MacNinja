# MacNinja

A simple **MAC Address Spoofer** for Linux, written in Python 3.12.  
Allows users to safely change their network interface MAC address, with **first-run backup** and **easy restore**.

---

## Features

- Works on Linux only 🐧  
- Random MAC address generation  
- Option to restore original MAC address  
- First-run backup stored in `og_mac.txt`  
- Beginner-friendly and fully customizable  

---

## Requirements

- Python 3.12+  
- Linux machine  
- Root/sudo access  

---

## Usage

```bash
sudo python3 spoofer.py
```

---

Enter the network interface (eth0, wlan0, etc.)

Choose:

1. Spoof to a random MAC

2. Restore original MAC

<img width="888" height="185" alt="image" src="https://github.com/user-attachments/assets/08645622-5abb-465a-a4ff-71c85e76867f" />

<img width="927" height="307" alt="image" src="https://github.com/user-attachments/assets/3a20ce77-5369-4d19-9589-23481a194608" />

<img width="914" height="360" alt="image" src="https://github.com/user-attachments/assets/09e60cfb-df09-4f47-8eb2-e0b10e145ab6" />

<img width="935" height="289" alt="image" src="https://github.com/user-attachments/assets/d39b79ad-81d7-499a-8c06-ccfddf83a5c8" />


## Warning
Do not delete og_mac.txt, it stores your original MAC

## DISCLAIMER

- Use responsibly.
- Changing MAC addresses may disrupt network connections.
- Tested on Kali Linux only
