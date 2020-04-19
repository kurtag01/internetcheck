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
location1 = "/etc/config/dhcp"
location2 = "/etc/config/wireless"
newline = "\toption disabled '1'\n\toption dns '209.222.18.218 209.222.18.222'"

time.sleep(2)

with open(location1, "r") as file:
    content = file.readlines()
    
content[5] = "\toption rebind_protection '0'\n"

with open(location1, "w") as file"
    file.writelines(content)
    
with open (location2, "a") as file2:
    file2.writelines(newline)

while status == False:
    time.sleep(5)
    status = connection()
    
with open(location1, "r") as file:
    lines = file.readlines()
    
lines[5] = "\toption rebind_protection '1'\n"

with open (location1, "w") as file:
    file.writelines(lines)


