import subprocess
command = input("text\n")
if command[:5] == "open ":
    command1 = command[5:]
    process = subprocess.Popen(['explorer', command1], stdout=subprocess.PIPE, universal_newlines=True)
elif command[:6] == "close ":
    command1 = command[6:]
    print(command1)
    print('/IM ' + command1 + ' /F')
    process = subprocess.Popen(['taskkill', '/im ' + command1 + '.exe'], stdout=subprocess.PIPE, universal_newlines=True)
else:
    print('no')
    