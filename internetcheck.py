#!/bin/python3
import socket
import time
import fileinput


def connection():
    try:
        s = socket.create_connection(("1.1.1.1", 80), 2)
        s.close()
        return True
    except:
        pass
    return False    

status = connection()
location = "/etc/config/dhcp"

while status == False:
    time.sleep(5)
    status = connection()
    
with open(location, "r") as file:
    lines = file.readlines()
    
lines[5] = "\toption rebind_protection '1'\n"

with open (location, "w") as file:
    file.writelines(lines)


