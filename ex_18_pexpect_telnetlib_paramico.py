import pexpect

ssh = pexpect.spawn('ssh Luba@192.168.178.1')

ssh.expect('[Pp]assword')
ssh.sendline('cisco')
ssh.expect('[>#]')
ssh.sendline('enable')
ssh.expect('[Pp]assword')
ssh.sendline('cisco')
ssh.expect('[>#]')