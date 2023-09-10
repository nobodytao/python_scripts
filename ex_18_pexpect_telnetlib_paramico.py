import pexpect, yaml
import re
from pprint import pprint


def show_command(ip, username, password, enable, commands, prompt="#"):
    with pexpect.spawn(f"ssh {username}@{ip}", timeout=10, encoding="utf-8") as ssh:
        ssh.expect("[Pp]assword")
        ssh.sendline(password)
        enable_status = ssh.expect([">", "#"])
        if enable_status == 0:
            ssh.sendline("enable")
            ssh.expect("[Pp]assword")
            ssh.sendline(enable)
            ssh.expect(prompt)

        ssh.sendline("terminal length 0")
        ssh.expect(prompt)

        result = {}
        for command in commands:
            ssh.sendline(command)
            match = ssh.expect([prompt, pexpect.TIMEOUT, pexpect.EOF])
            if match == 1:
                print(
                    f"Символ {prompt} не найден. Исключение!"
                )
            if match == 2:
                print("Соединение разорвано. Исключение!")
                return result
            else:
                output = ssh.before
                result[command] = output.replace("\r\n", "\n")
        return result

if __name__ == "__main__":
    command = ["sh ip int br"]
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(str(dev['host']))
        result = show_command(dev['host'], dev['username'], dev['password'], dev['secret'], command)
        pprint(result, width=120)
