import subprocess
command = input("text\n")
if command[:5] == "open ":
    command1 = command[6:]
    process = subprocess.Popen(['explorer', command1], stdout=subprocess.PIPE, universal_newlines=True)
else:
    print("no")