# WiFi Deauthentication Attack Script

A Python script that uses the Scapy library to perform a WiFi deauthentication attack. This tool demonstrates a common type of Denial-of-Service (DoS) attack by sending crafted deauthentication frames to a specific client on a wireless network, causing it to disconnect from the access point.

## Features

* Crafts and sends 802.11 deauthentication frames using Scapy.
* Targets a specific client MAC address on the network.
* Takes the target MAC, gateway MAC, and a monitor-mode interface as command-line arguments.

## Technologies Used

* Python
* Scapy

## ❗Prerequisite: Enable Monitor Mode

For this script to work, your wireless network interface **must** be in **monitor mode**.

1.  **Identify your wireless interface name** (e.g., `wlan0`, `en0`).
    ```bash
    iwconfig
    ```
2.  **Enable monitor mode** (replace `<interface>` with your actual interface name):
    ```bash
    sudo ifconfig <interface> down
    sudo iwconfig <interface> mode monitor
    sudo ifconfig <interface> up
    ```

## Setup and Usage

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Ashin-06/wifi-deauth-attack.git
    cd wifi-deauth-attack
    ```

2.  **Install Dependencies:**
    ```bash
    pip install scapy
    ```

3.  **Run the Attack Script:**
    This script requires root privileges to send raw packets.
    ```bash
    sudo python deauth_attack.py --target <target_mac> --gateway <gateway_mac> --interface <monitor_interface>
    ```

## ⚖️ Ethical and Legal Disclaimer

This tool is for **educational purposes only**, specifically for use in controlled environments on networks you own or have explicit permission to test. Launching a deauthentication attack against a network without consent is **illegal** and can be prosecuted. The author is not responsible for any misuse of this software.
