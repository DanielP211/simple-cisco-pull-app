import paramiko
import time
import getpass
import string
import re

d1 = raw_input("Choose if you want to use a proxy to access your devices or no (A - Use proxy, B - Access devices directly) ")

#print("Choose if you want to use a proxy to access your devices.")

#response = None

#while response not int {"A","B"}
#    response = raw_input("Please enter yes or no: ")

if (d1 == 'A' or d1 == 'a'):

    proxyIP = raw_input("Input proxy: ")
    proxyusername = raw_input("Input proxy username: ")
    proxypassword = getpass("Input proxy password: ")

    deviceusername = raw_input("Input username: ")
    devicepassword = getpass("Input password: ")

    f1 = open("devices.txt","r")
    f2 = open("commands.txt","r")
    f3 = open("log.txt", "w+")

    devices_REMOTE = f1.readlines()
    commands_REMOTE = f2.readlines()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(proxyIP, username=proxyusername, password=proxypassword)
    connection = ssh.invoke_shell()

    for device in devices_REMOTE:
        device = str(device.rstrip())
        connection.send("\n ssh -l " +str(deviceusername) +" " +str(device) +"\n")
        time.sleep(5)
        connection.send(str(devicepassword) +"\n")
        time.sleep(5)
        for command in commands_REMOTE:
            commad = str(command.rstrip())
            connection.send("\n" +str(command) +"\n")
            connection.send("\n" +"exit" +"\n")
            time.sleep(5)
        output_str = ""
        output = connection.recv(65535)
        output_str = str(output)
        hostname =""
        version =""
        SN =""
        hostname = re.search(r'[a-zA-Z0-9-]+-BA',output_str)
        version = re.search(r'15.+[0-9].[0-9]+',output_str)
        SN = re.search(r'FCZ+[a-zA-Z0-9]+',output_str)
#    if hostname == "":
#	continue
        dash = '-' * 120
        print (dash)
        print ("|  HOSTNAME:  {}  |  VERSION:  {}  |   SN:   {}   |  DEVICE IP:  {}  |".format(hostname.group(0), version.group(0), SN.group(0), device))
        print (dash)
        time.sleep(2)
        ssh.close()
        time.sleep(4)
        f1.close()
        f2.close()
        f3.close()

elif (d1 == "B" or d1 == "b"):

    deviceusername = raw_input("Input username: ")
    devicepassword = getpass("Input password: ")

    f1 = open("devices.txt","r")
    f2 = open("commands.txt","r")
    f3 = open("log.txt", "w+")

    devices_REMOTE = f1.readlines()
    commands_REMOTE = f2.readlines()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(proxyIP, username=proxyusername, password=proxypassword)
    connection = ssh.invoke_shell()

for device in devices_REMOTE:
        device = str(device.rstrip())
        connection.send("\n ssh -l " +str(deviceusername) +" " +str(device) +"\n")
        time.sleep(5)
        connection.send(str(devicepassword) +"\n")
        time.sleep(5)
        for command in commands_REMOTE:
            commad = str(command.rstrip())
            connection.send("\n" +str(command) +"\n")
            connection.send("\n" +"exit" +"\n")
            time.sleep(5)
        output_str = ""
        output = connection.recv(65535)
        output_str = str(output)
        hostname =""
        version =""
        SN =""
        hostname = re.search(r'[a-zA-Z0-9-]+-BA',output_str)
        version = re.search(r'15.+[0-9].[0-9]+',output_str)
        SN = re.search(r'FCZ+[a-zA-Z0-9]+',output_str)
#    if hostname == "":
#	continue
        dash = '-' * 120
        print (dash)
        print ("|  HOSTNAME:  {}  |  VERSION:  {}  |   SN:   {}   |  DEVICE IP:  {}  |".format(hostname.group(0), version.group(0), SN.group(0), device))
        print (dash)
        time.sleep(2)
        ssh.close()
        time.sleep(4)
        f1.close()
        f2.close()
        f3.close()

else:
	print("Wrong choice")