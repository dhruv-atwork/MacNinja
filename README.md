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

## Warning
Do not delete og_mac.txt, it stores your original MAC

## DISCLAIMER

- Use responsibly.
- Changing MAC addresses may disrupt network connections.
- Tested on Kali Linux only
