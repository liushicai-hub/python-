import netmiko

def ssh_to_switch(ip_address, username, password):
    """
    SSH to a Cisco switch.
    """

    device = netmiko.ConnectHandler(
        device_type="cisco_ios",
        ip=ip_address,
        username=username,
        password=password,
    )

    command = "show version"
    output = device.send_command(command)
    start_ver = (output.find('Version'))
    print(output[start_ver:(start_ver + 21)])

  # print(output)
  # print(output.find('Software'))
# send_config_set can send multiple commands in configuration mode
    # commands = ['router ospf 1',
    #             'network 10.0.0.0 0.255.255.255 area 0',
    #             'network 192.168.100.0 0.0.0.255 area 1']
    #
    # output = ssh.send_config_set(commands)
    # print(output)

if __name__ == "__main__":
    ip = "10.13.255.21"
    username = "shicai.liu@okg.com"
    password = "Wushuming1314?"

    ssh_to_switch(ip, username, password)