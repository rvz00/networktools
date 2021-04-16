#!/usr/bin/env python3

import scapy.all as scapy
import argparse


def get_args():
    """
    Takes argument (ie. ip) from the user using -t or --target option.
    """
    parse = argparse.ArgumentParser()
    parse.add_argument("-t", "--target", dest="target_ip", help="Enter IP to scan")
    option = parse.parse_args()

    if not option.target_ip:
        parse.error("[-] Please specify IP, use --help for for more info")

    return option


def scan(ip):
    """
    Scans ip range using ARP request broadcast.
    srp generates two lists (answered, unanswered).
    answered_list contains two elements(packet sent, answer)
    """
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for elements in answered_list:
        client_dict = {"ip": elements[1].psrc, "mac": elements[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def print_result(scan_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for elements in scan_list:
        print(elements['ip'] + "\t\t" + elements['mac'])


options = get_args()
result = scan(options.target_ip)
print_result(result)
