from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.13.255.21', 'shicai.liu@okg.com', 'Wushuming1314?')
iosvl2.open()

ios_output = iosvl2.get_facts()
print (ios_output)
