import subprocess
import sys
import re
import random
import os


print('''
███╗░░░███╗░█████╗░░█████╗░███╗░░██╗██╗███╗░░██╗░░░░░██╗░█████╗░
████╗░████║██╔══██╗██╔══██╗████╗░██║██║████╗░██║░░░░░██║██╔══██╗
██╔████╔██║███████║██║░░╚═╝██╔██╗██║██║██╔██╗██║░░░░░██║███████║
██║╚██╔╝██║██╔══██║██║░░██╗██║╚████║██║██║╚████║██╗░░██║██╔══██║
██║░╚═╝░██║██║░░██║╚█████╔╝██║░╚███║██║██║░╚███║╚█████╔╝██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝''')

# BACKUP FOR FIRST TIME RUN

BACKUP_FILE = "og_mac.txt"


# Checking if the script's running in Linux for my trust issues on user
if sys.platform != "linux":
    print("\nThis is a Linux only script!")
    sys.exit()

# Checking if the user really read the readme file and is using root for running this script.
if subprocess.run(["id", "-u"], capture_output=True, text=True).stdout.strip() != "0":
    print(
        "\nThis script requires root/sudo access. Run 'sudo su' in your commands shell and run this script for functionality.\n")
    sys.exit()

# Asking user which interface's mac address to spoof
interface = input(
    "\n Enter the interface you wish to mask/spoof(eth0, wlan0 etc.)"
    "\n If you're unsure, continue with eth0. If that doesn't work, check using ifconfig in your Linux shell.\n""Enter the interface: ")


# defining a function to fetch original mac address of the interface
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

    for _ in range(6):
        random_number = random.randint(0x00, 0xff)
        hex_part = f"{random_number:02x}"
        mac_hexes.append(hex_part)

    mac_address = ":".join(mac_hexes)
    return mac_address


def change_mac(interface, new_address):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ip", "link", "set", interface, "address", new_address])
    subprocess.run(["ifconfig", interface, "up"])


# Now what is their mac address?
original_mac = get_current_address(interface)
if not original_mac:
    print("Mac address not found!")
    sys.exit()
else:
    print(f"\n Current MAC address: {original_mac}")

# LET'S BACK UP THEIR ORIGINAL MAC ADDRESS IN CASE THEY'RE RUNNING THIS SCRIPT FOR THE 1ST TIME
if not os.path.exists(BACKUP_FILE):
    with open(BACKUP_FILE, "w") as f:
        f.write(original_mac)
    print("\nSince it was your first run, your original mac address is backed up in og_mac.txt")
else:
    print("\nYour original Mac address is backed up to og_mac.txt, you can use option 2 ")

with open(BACKUP_FILE, "r") as f:
    data = f.read().strip()

print("\n⚠️ DO NOT DELETE og_mac.txt else you won't be able to use option 2 ⚠️\n")
print("\nHow do you want to proceed?\n")
print("\n1 Mask to a Random Mac Address\n")
print("\n2 Restore the original Mac Address")

option = int(input("\nEnter your action: "))

if option == 1:
    rand_mac = generate_random_mac()
    print(f"\n Changed Mac address: {rand_mac}")
    change_mac(interface, rand_mac)

elif option == 2:
    print("\n Restoring the original Mac Address......")
    change_mac(interface, data)

else:
    print("\n Invalid Option. Choose between 1 and 2")
    sys.exit()

mac_address_now = get_current_address(interface)
print(f"\n Now your Mac Address is: {mac_address_now}")

