#!/usr/bin/python3
import urllib.request
import time
import fileinput

location = "/etc/config/dhcp"

#Loop through the dhcp file and turn off rebind protection:
with fileinput.FileInput(location, inplace=True, backup='.bak')as file:
    for line in file:
        print(line.replace("option rebind_protection '1'", "option rebind_protection '0'"), end='')

#function to check internet connectivity
def connection():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

status = connection()

while status == False:
    time.sleep(5)
    status = connection()    
    
if status == True:    
    with fileinput.FileInput(location, inplace=True, backup='.bak')as file:
        for line in file:
            print(line.replace("option rebind_protection '0'", "option rebind_protection '1'"), end='')
