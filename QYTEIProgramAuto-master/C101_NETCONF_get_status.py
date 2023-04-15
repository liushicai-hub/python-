from collections import OrderedDict

get_acl = """<filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
          <access-list/>
        </ip>
      </native>
    </filter>
    """

# ietf的标准模型检索接口信息
get_if = """<filter>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        </interface>
      </interfaces>
    </filter>
"""

get_OspfNbr = """
    <filter>
      <ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
        <ospfv2-instance>
          <ospfv2-area>
            <ospfv2-interface>
              <ospfv2-neighbor/>
            </ospfv2-interface>
          </ospfv2-area>
        </ospfv2-instance>
      </ospf-oper-data>
    </filter>
"""

x = """<filter>
      <ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
        <ospfv2-instance/>
      </ospf-oper-data>
    </filter>
"""

xx = OrderedDict([('interfaces', OrderedDict([('@xmlns', 'urn:ietf:params:xml:ns:yang:ietf-interfaces'), ('interface', [
    OrderedDict([('name', 'GigabitEthernet1'), ('type', OrderedDict(
        [('@xmlns:ianaift', 'urn:ietf:params:xml:ns:yang:iana-if-type'), ('#text', 'ianaift:ethernetCsmacd')])),
                 ('enabled', 'true'), ('ipv4', OrderedDict([('@xmlns', 'urn:ietf:params:xml:ns:yang:ietf-ip'), (
        'address', OrderedDict([('ip', '203.0.113.11'), ('netmask', '255.255.255.0')]))])),
                 ('ipv6', OrderedDict([('@xmlns', 'urn:ietf:params:xml:ns:yang:ietf-ip')]))]), OrderedDict(
        [('name', 'GigabitEthernet2'), ('description', 'xiaofang'), ('type', OrderedDict(
            [('@xmlns:ianaift', 'urn:ietf:params:xml:ns:yang:iana-if-type'), ('#text', 'ianaift:ethernetCsmacd')])),
         ('enabled', 'true'), ('ipv4', OrderedDict([('@xmlns', 'urn:ietf:params:xml:ns:yang:ietf-ip'), (
        'address', OrderedDict([('ip', '10.1.1.1'), ('netmask', '255.255.255.252')]))])),
         ('ipv6', OrderedDict([('@xmlns', 'urn:ietf:params:xml:ns:yang:ietf-ip')]))]), OrderedDict(
        [('name', 'GigabitEthernet3'), ('type', OrderedDict(
            [('@xmlns:ianaift', 'urn:ietf:params:xml:ns:yang:iana-if-type'), ('#text', 'ianaift:ethernetCsmacd')])),
         ('enabled', 'true'), ('ipv4', OrderedDict([('@xmlns', 'urn:ietf:params:xml:ns:yang:ietf-ip')])),
         ('ipv6', OrderedDict([('@xmlns', 'urn:ietf:params:xml:ns:yang:ietf-ip')]))]), OrderedDict(
        [('name', 'Loopback0'), ('description', 'xiaoniu'), ('type', OrderedDict(
            [('@xmlns:ianaift', 'urn:ietf:params:xml:ns:yang:iana-if-type'), ('#text', 'ianaift:softwareLoopback')])),
         ('enabled', 'true'), ('ipv4', OrderedDict([('@xmlns', 'urn:ietf:params:xml:ns:yang:ietf-ip'), (
        'address', OrderedDict([('ip', '10.1.255.11'), ('netmask', '255.255.255.255')]))])),
         ('ipv6', OrderedDict([('@xmlns', 'urn:ietf:params:xml:ns:yang:ietf-ip')]))])])]))])
