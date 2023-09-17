import netmiko

# 定义交换机列表
switches = ["10.13.255.21","10.13.255.23"]

# 定义用户名和密码
username = "shicai.liu@okg.com"
password = "Wushuming1314?"


# 定义函数，用于连接并执行 show  命令
def connect_and_show(switch):
    try:
        device = netmiko.ConnectHandler(
            device_type="cisco_ios",
            ip=switch,
            username=username,
            password=password,
        )

        output = device.send_command("show ip int br")

        print(f"Switch {switch}:\n{output}")

    except netmiko.NetmikoTimeoutException as e:
        print(f"Failed to connect to switch {switch}: {e}")
    except netmiko.NetmikoAuthenticationException as e:
        print(f"Failed to authenticate to switch {switch}: {e}")


# 使用 if __name__ == "__main__": 模式执行函数
if __name__ == "__main__":
    for switch in switches:
        connect_and_show(switch)
