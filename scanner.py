#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# This line is for cleaning the screen
subprocess.call('clear', shell=True)

# Prompt the user to input the host
server    = raw_input("Enter a host: ")
serverIP  = socket.gethostbyname(server)

# Format presentation with information on which host is being scanned
print "-" * 70
print "Scanning remote host", serverIP
print "-" * 70

# Check what time the scan started
time1 = datetime.now()

# List of common ports. here it will scans all ports between 1 and 8443)

try:
    common_ports = {'21': 'FTP',
'22': 'SSH',
'23': 'TELNET',
'25': 'SMTP',
'53': 'DNS',
'69': 'TFTP',
'80': 'HTTP',
'109': 'POP2',
'110': 'POP3',
'123': 'NTP',
'137': 'NETBIOS-NS',
'138': 'NETBIOS-DGM',
'139': 'NETBIOS-SSN',
'143': 'IMAP',
'156': 'SQL-SERVER',
'389': 'LDAP',
'443': 'HTTPS',
'546': 'DHCP-CLIENT',
'547': 'DHCP-SERVER',
'995': 'POP3-SSL',
'993': 'IMAP-SSL',
'2086': 'WHM/CPANEL',
'2087': 'WHM/CPANEL',
'2082': 'CPANEL',
'2083': 'CPANEL',
'3306': 'MYSQL',
'8443': 'PLESK'
}
    for port in range(1,10000):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((serverIP, port))
        if result == 0:
		if str(port) in common_ports.keys():
    			print "Port {}: 	 Open".format(port), " ", common_ports.get(str(port))
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
time2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
resultTotal =  time2 - time1

# Printing the information to screen
print 'Scanning Completed in: ', resultTotal
