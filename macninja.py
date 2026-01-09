import subprocess
import sys
import re
import random
import os
import tkinter as tk
from tkinter import messagebox

# BACKUP FOR FIRST TIME RUN
BACKUP_FILE = "og_mac.txt"

# Checking if the script's running in Linux for my trust issues on user
if sys.platform != "linux":
    messagebox.showerror("Error", "This is a Linux only script!")
    sys.exit()

# Checking if the user really read the readme file and is using root for running this script.
if subprocess.run(["id", "-u"], capture_output=True, text=True).stdout.strip() != "0":
    messagebox.showerror("Error", "This program requires Sudo/Root access in order to function.")
    sys.exit()


# function to fetch original mac address of the interface
def get_current_address(interface):
    result = subprocess.run(
        ["ip", "link", "show", interface],
        capture_output=True, text=True)

    search_mac_addr = re.search(r"link/ether\s+([0-9a-fA-F:]{17})", result.stdout)
    if search_mac_addr:
        return search_mac_addr.group(1)
    return None


# function which generates a random mac address to be spoofed
def generate_random_mac():
    mac_hexes = []

    for i in range(6):
        random_number = random.randint(0x00, 0xff)
        hex_part = f"{random_number:02x}"
        mac_hexes.append(hex_part)

    mac_address = ":".join(mac_hexes)
    return mac_address

 # function which backs up the user's original mac address
def backup_mac(original_mac):
    if not os.path.exists(BACKUP_FILE):
        with open(BACKUP_FILE, "w") as f:
            f.write(original_mac)
            messagebox.showinfo("Backup Created",
                                "Since it was your first run, your original mac address is backed up in og_mac.txt")
# function which changes the mac address to the new generated address
def change_mac(interface, new_address):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ip", "link", "set", interface, "address", new_address])
    subprocess.run(["ifconfig", interface, "up"])


# GUI Button Commands

def get_mac_button():
    global original_mac
    interface = interface_entry.get().strip()

    original_mac = get_current_address(interface)
    if not original_mac:
        messagebox.showerror("Error", "Mac Address not found.")
        return

    backup_mac(original_mac)
    status_label.config(text=f"Current MAC Address: {original_mac}")

def spoof_mac_button():
    interface = interface_entry.get().strip()
    rand_mac = generate_random_mac()
    change_mac(interface, rand_mac)
    status_label.config(text=f"Current MAC Address: {rand_mac}")
    if not os.path.exists(BACKUP_FILE):
        original_mac = get_current_address(interface)
        if original_mac:
            backup_mac(original_mac)

def restore_mac_button():
    interface = interface_entry.get().strip()

    if not os.path.exists(BACKUP_FILE):
        messagebox.showerror("Error", "og_mac.txt not found.")
        return
    with open(BACKUP_FILE, "r") as f:
        data = f.read().strip()

    change_mac(interface, data)
    status_label.config(text=f"Restored MAC Address: {data}")


#GUI Codes

window = tk.Tk()
window.title("MacNinja")
window.geometry("420x260")
window.resizable(width=False, height=False)

tk.Label(window, text="Enter the interface you wish to mask/spoof(eth0, wlan0 etc.)\n",
font = "Arial").pack(pady=10)

interface_entry = tk.Entry(window)
interface_entry.pack()

tk.Button(window,text="Get Current MAC Address",command=get_mac_button).pack(pady=5),

tk.Button(window, text="Mask a Random MAC Address", command=spoof_mac_button).pack(pady=5)
tk.Button(window, text="Restore Original Mac Address", command=restore_mac_button).pack(pady=5)

status_label = tk.Label(
    window,
    text="⚠️ DO NOT DELETE og_mac.txt else you won't be able to restore",
    wraplength=400
)
status_label.pack(pady=10)

window.mainloop()
