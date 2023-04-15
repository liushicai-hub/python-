config_interface = """<config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>2</name>
            <description xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">netconf_configed</description>
            <shutdown xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="remove"/>
            <ip>
              <address>
                <primary>
                  <address xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">10.1.1.1</address>
                  <mask xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">255.255.255.252</mask>
                </primary>
              </address>
            </ip>
          </GigabitEthernet>
          <Loopback>
            <name>0</name>
            <description xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">netconf_configed</description>
            <shutdown xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="remove"/>
            <ip>
              <address>
                <primary>
                  <address xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">10.1.255.11</address>
                  <mask xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">255.255.255.255</mask>
                </primary>
              </address>
            </ip>
          </Loopback>
        </interface>
      </native>
    </config>
"""
config_ospf = """<config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>2</name>
            <ip>
              <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                <ospf>
                  <network>
                    <point-to-point xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge"/>
                  </network>
                </ospf>
              </router-ospf>
            </ip>
          </GigabitEthernet>
        </interface>
        <router>
          <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
            <ospf>
              <process-id>
                <id>1</id>
                <network>
                  <ip>10.1.255.11</ip>
                  <wildcard>0.0.0.0</wildcard>
                  <area xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">0</area>
                </network>
                <network>
                  <ip>10.1.1.0</ip>
                  <wildcard>0.0.0.3</wildcard>
                  <area xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">0</area>
                </network>
                <router-id xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">10.1.255.11</router-id>
                <default-information>
                  <originate xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge"/>
                </default-information>
              </process-id>
            </ospf>
          </router-ospf>
        </router>
      </native>
    </config>
"""
config_dhcp = """    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
          <dhcp>
            <excluded-address xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-dhcp">
              <low-high-address-list>
                <low-address>10.1.100.1</low-address>
                <high-address>10.1.100.100</high-address>
              </low-high-address-list>
            </excluded-address>
            <pool xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-dhcp">
              <id>VL100_POOL</id>
              <default-router>
                <default-router-list xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">10.1.100.1</default-router-list>
              </default-router>
              <dns-server>
                <dns-server-list xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">10.1.100.1</dns-server-list>
              </dns-server>
              <domain-name xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">qytei.com</domain-name>
              <network>
                <primary-network>
                  <number>10.1.100.0</number>
                  <mask xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">255.255.255.0</mask>
                </primary-network>
              </network>
            </pool>
          </dhcp>
        </ip>
      </native>
    </config>
"""
config_wan = """    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>3</name>
            <description xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">Connect_to_INET</description>
            <shutdown xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="remove"/>
            <ip>
              <address>
                <dhcp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge"/>
              </address>
            </ip>
          </GigabitEthernet>
        </interface>
      </native>
    </config>
"""
config_acl = """    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
          <access-list>
            <standard xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
              <name xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">NAT</name>
              <access-list-seq-rule>
                <sequence xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">5</sequence>
                <permit>
                  <std-ace>
                    <ipv4-prefix xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">10.1.100.0</ipv4-prefix>
                    <mask xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">0.0.0.255</mask>
                  </std-ace>
                </permit>
              </access-list-seq-rule>
            </standard>
          </access-list>
        </ip>
      </native>
    </config>
"""
config_in_out = """    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>2</name>
            <ip>
              <nat xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-nat">
                <inside xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge"/>
              </nat>
            </ip>
          </GigabitEthernet>
          <GigabitEthernet>
            <name>3</name>
            <ip>
              <nat xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-nat">
                <outside xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge"/>
              </nat>
            </ip>
          </GigabitEthernet>
        </interface>
      </native>
    </config>
"""
config_nat = """    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
          <nat xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-nat">
            <inside>
              <source>
                <list>
                  <id>NAT</id>
                  <interface>
                    <name>G3</name>
                    <overload xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge"/>
                  </interface>
                </list>
              </source>
            </inside>
          </nat>
        </ip>
      </native>
    </config>
"""

CfgList = [config_interface, config_ospf, config_dhcp, config_wan, config_acl, config_in_out, config_nat]

DNS = """<config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
          <dns>
            <server xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge"/>
          </dns>
        </ip>
      </native>
    </config>
"""
