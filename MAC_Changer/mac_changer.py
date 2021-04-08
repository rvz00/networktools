#!/usr/bin/env python3

import subprocess
import optparse
import re


def get_argument():
    """
    Takes argument from user input.
    """
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parse.error("[-] Please specify interface, use --help for more info")
    elif not options.new_mac:
        parse.error("[-] please specify new MAC address, use --help more info")

    return options


def change_mac(interface, new_mac):
    """
    Sets the new MAC address in the interface.
    """
    print("[+] Changing MAC address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def current_mac():
    """
    Gets the current MAC address
    """
    ifconfig_output = subprocess.check_output(["ifconfig", options.interface])
    mac_search_result = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_output))
    if mac_search_result:
        print("[+] Current MAC address is " + mac_search_result.group(0))
    else:
        print("[-] Could not find MAC address")


options = get_argument()
change_mac(options.interface, options.new_mac)
current_mac()
