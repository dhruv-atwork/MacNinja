# MacNinja

MacNinja is a **Linux-only MAC address masking/spoofing tool** written in Python.  
It allows users to **view, randomize, and restore** their network interface MAC address — now with a **Graphical User Interface (GUI)** built using **Tkinter**.

---

## 🚀 Features

- ✅ View current MAC address of a network interface
- 🎭 Mask/Spoof MAC address with a randomly generated value
- 🔄 Restore the original MAC address
- 💾 Automatic backup of original MAC address on first run
- 🖥️ Simple & beginner-friendly GUI
- 🔐 Requires root privileges (safe system-level execution)

---

## 🛠️ Requirements

- **Operating System:** Linux
- **Python Version:** Python 3.12+
- **Privileges:** Root / sudo access 

---

## 🖼️ Preview

- GUI-based MAC address changer for Linux

<img width="618" height="261" alt="image" src="https://github.com/user-attachments/assets/105a5a7c-a7b6-49eb-81c9-f245f9629d8b" />

<img width="779" height="313" alt="image" src="https://github.com/user-attachments/assets/aaa8ae20-183b-484b-8f36-f7b3a68c5b8b" />

<img width="421" height="297" alt="image" src="https://github.com/user-attachments/assets/b97bc08e-9c19-4fad-a6bb-8dec7ae866e7" />

### After masking:
<img width="425" height="289" alt="image" src="https://github.com/user-attachments/assets/8b3305c9-931f-4b02-85bf-7be03996361b" />


---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/MacNinja.git
```
```bash
cd MacNinja
```
```bash
sudo python macninja.py
```
---

### Python Modules Used
All modules are part of the Python standard library:
- `subprocess`
- `sys`
- `re`
- `random`
- `os`
- `tkinter`

---

## Warning
Do not delete og_mac.txt, it stores your original MAC

## DISCLAIMER

- Use responsibly.
- Changing MAC addresses may disrupt network connections.
- Tested on Kali Linux only
