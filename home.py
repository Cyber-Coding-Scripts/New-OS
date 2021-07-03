import time
import os
import socket

login_pass = open('user/password.pass')
login_name = open('user/dataname.pass')
l_p = login_pass.read()
l_n = login_name.read()
print("""
░█████╗░██╗░░░██╗██████╗░███████╗██████╗░░░░░░░██╗░░██╗
██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗░░░░░░╚██╗██╔╝
██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝█████╗░╚███╔╝░
██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗╚════╝░██╔██╗░
╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║░░░░░░██╔╝╚██╗
░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚═╝░░╚═╝
""")
print("Welcome " + l_n)
print("The Date Is: " + time.strftime("%m/%d/%y"))
print("""
[1] To Open Google
[2] To Open Text Editor
[3] To Open File Exploer
[4] To Configure and Open BioS
[5] To Open Terminal
[6] To Open Calculator
[7] To Close OS Safley
""")

select = input("[?]: ")

if select == '1':
	os.startfile('home.py')
	os.startfile('brows.py')

if select == '2':
	os.startfile('home.py')
	os.startfile('edit.pyw')

if select == '3':
	os.startfile('home.py')
	os.startfile('file.pyw')

if select == '4':
	while True:
		b_login = input(str("Please Enter The Password To " + l_n + " To Open BioS: "))
		if b_login == l_p:
			print("Opening BioS")
			host_name = socket.gethostname()
			host_ip = socket.gethostbyname(host_name)
			print("[1] USER NAME: " + l_n)
			print("[2] PASSWORD: " + l_p)
			print("Hostname:", host_name)
			print("LOCAL IPS: " + host_ip)
			edit_b = input("Enter [?] to change setting: ")
			if edit_b == '1':
				edit_n = input("Enter New Username: ")
				with open('user/dataname.pass', 'w') as f:
					f.writelines(edit_n)
				print("Username Changed To " + edit_n)
				input("Press Enter To Restart: ")
				os.startfile('home.py')
				os.system('exit')

			if edit_b == '2':
				edit_p = input("Enter New Password: ")
				with open('user/password.pass', 'w') as f:
					f.writelines(edit_p)

				print("Password Changed To " + edit_p)
				input("Press Enter To Restart: ")
				os.startfile('home.py')
				os.system('exit')
			else:
				print("Wrong Password To " + l_n)

	else:
		print("Wrong Password To " + l_n)

if select == '5':
	os.startfile('home.py')
	os.startfile('terminal.py')

if select == '6':
	os.startfile('home.py')
	os.startfile('calc.py')

if select == '7':
	os.system('exit')
