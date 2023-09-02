import subprocess, os, ipaddress

#standard input/output stream
result = subprocess.run(['ls', '-ls'], stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))

#Turn off standard input/output stream, only result
result = subprocess.run(['ls', '-ls'], stdout=subprocess.DEVNULL)
print(result.stdout)
print(result.returncode)

#Stderr
result = subprocess.run(['ping', '-c', '3', '-n', 'a'], stderr=subprocess.PIPE, encoding='utf-8')
print(result.stderr)

print(os.path.abspath("python_scripts"))

