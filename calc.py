print("""
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

[1] +
[2] -
[3] x
[4] /
""")
while True:
    select = input("> ")
    
    if select == '1':
        a = input("Enter First Digit: ")
        print("+")
        b = input('Enter The Second Digit: ')
        c = int(a)+int(b)
        print(c)

    if select == '2':
        a = input("Enter First Digit: ")
        print("-")
        b = input('Enter The Second Digit: ')
        c = int(a)-int(b)
        print(c)
        
    if select == '3':
        a = input("Enter First Digit: ")
        print("x")
        b = input('Enter The Second Digit: ')
        c = int(a)*int(b)
        print(c)

    if select == '4':
        a = input("Enter First Digit: ")
        print("/")
        b = input('Enter The Second Digit: ')
        c = int(a)/int(b)
        print(c)