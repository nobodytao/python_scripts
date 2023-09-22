from pprint import pprint
import yaml, paramiko
from netmiko import (ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException)


def send_show_command(device, commands):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output
        return result
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    device = {
        "device_type": "cisco_ios_telnet",
        "host": "192.168.178.1",
        "username": "Luba",
        "password": "LubaLubaLuba",
        "secret": "Luba",
    }
    result = send_show_command(device, ["sh clock", "sh ip int br"])
    pprint(result, width=120)