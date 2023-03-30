import os

data_info = open('user/info.data')
data = data_info.read()

if data == '0':
	print("Opening Register Page...")
	os.startfile("setup.py")

if data == '1':
	print("Opening Login Page...")
	os.startfile("login.py")