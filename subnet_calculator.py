# subnet_calculator.py

import ipaddress

def calculate_subnet(ip_with_subnet):
    try:
        network = ipaddress.ip_network(ip_with_subnet, strict=False)
        
        print("\n📘 Subnet Calculation Results:\n")
        print(f"🧠 IP Address:          {network.network_address}")
        print(f"📡 Broadcast Address:   {network.broadcast_address}")
        print(f"🌐 Network Mask:        {network.netmask}")
        print(f"🔢 Wildcard Mask:       {network.hostmask}")
        print(f"👨‍💻 Host Bits:           {network.max_prefixlen - network.prefixlen}")
        print(f"👥 Total Hosts:         {network.num_addresses}")
        print(f"🟢 Usable Hosts:        {network.num_addresses - 2 if network.num_addresses > 2 else 0}")
        hosts = list(network.hosts())
        if len(hosts) >= 2:
            print(f"✅ First Host:          {hosts[0]}")
            print(f"⛔ Last Host:           {hosts[-1]}")
        print(f"📏 Subnet Prefix:       /{network.prefixlen}")
        print(f"🔢 Binary Netmask:      {' '.join([format(int(octet), '08b') for octet in str(network.netmask).split('.')])}")
    
    except ValueError:
        print("❌ Invalid IP address or subnet. Please try again (e.g., 192.168.1.0/24).")

# Main program loop
if __name__ == "__main__":
    print("🔧 IP Subnet Calculator 🔧")
    ip_input = input("Enter IP address with subnet (e.g., 192.168.1.0/24): ")
    calculate_subnet(ip_input)
