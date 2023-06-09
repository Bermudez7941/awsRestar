import os
import subprocess
os.system("ls")
print("--------------------------------------------------------------------------------------")
subprocess.run(["ls","-l"])

print("--------------------------------------------------------------------------------------")
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
print("--------------------------------------------------------------------------------------")

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])