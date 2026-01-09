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

> GUI-based MAC address changer for Linux  
> (Screenshots coming soon)

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/MacNinja.git
cd MacNinja
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
