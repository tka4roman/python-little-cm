#!/usr/bin/python3

import subprocess
import optparse
import re

def get_args():
	parser = optparse.OptionParser()

	parser.add_option("-u", "--username", dest="username", help="With the help of this arg you define your username")
	parser.add_option("-c", "--command" , dest="command" , help="With the help of this arg you define your command")
	parser.add_option("-p", "--path"	, dest="filename", help="With the help of this arg you define a file with list of your hosts")

	(options, arguments) = parser.parse_args()
	
	return options

def execute_ssh(username, command, host):
	
	print("[+] Executing ssh commands on the host {}:".format(host))
	subprocess.Popen(["ssh", username + "@" + host, command ], 
					shell=False, 
					stdout=subprocess.PIPE)

def get_hosts(path):
	
	file  = open(path, "r")	
	hosts = file.read().split("\n")

	return hosts 

### Main execution

options = get_args()

filename = options.filename
hosts = get_hosts(filename)

username = options.username
command = options.command

for host in hosts:
	if host != "":
		try:
			execute_ssh(username, command, host)
		except:
			print("[-] Unable to connect...")
