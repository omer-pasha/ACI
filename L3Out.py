import xml.dom.minidom

def create_l3out_script():
    # Basic L3Out / tenant inputs
    dc_name = input("Enter DC name: ").strip()
    vrf_name = input("Enter VRF name: ").strip()
    l3out_domain = input("Enter L3Out domain: ").strip()
    external_epg = input("Enter External EPG name: ").strip()

    # Contract input (only provider or consumer)
    contract = input("Enter contract name: ").strip()
    contract_scope = input("Apply contract as [provider/consumer]: ").strip().lower()
    if contract_scope not in ["provider", "consumer"]:
        print("⚠️ Invalid choice, defaulting to provider.")
        contract_scope = "provider"

    # Node profile / router IDs
    node1_id = input("Enter Leaf ID for Node Profile 1: ").strip()
    node1_rtr_id = input("Enter Router ID for Node Profile 1: ").strip()
    node2_id = input("Enter Leaf ID for Node Profile 2: ").strip()
    node2_rtr_id = input("Enter Router ID for Node Profile 2: ").strip()

    intf_profile_name = input("Enter Interface Profile base name: ").strip()

    # OSPF interface policy details
    ospf_if_pol_name = input("Enter OSPF interface policy name [default OSPF-WAN-Interface]: ").strip() or "OSPF-WAN-Interface"
    ospf_auth_type = input("Enter OSPF auth type [none/md5] [default md5]: ").strip() or "md5"
    ospf_auth_keyid = input("Enter OSPF authKeyId [default 1]: ").strip() or "1"

    # Interface collection
    interfaces = []
    while True:
        vlan = input("Enter VLAN number for interface (or 'done' to finish): ").strip()
        if vlan.lower() == 'done':
            break
        ip_address = input("Enter primary IP address with mask: ").strip()
        secondary_ip = input("Enter secondary IP address with mask (or leave blank): ").strip()
        leaf_id = input("Enter Leaf ID for this interface: ").strip()
        intf_name = input("Enter Interface/PC name (e.g., eth1/1 or WAN-PC1): ").strip()
        mtu = input("Enter MTU [default 9150]: ").strip() or "9150"

        path = f"topology/pod-1/paths-{leaf_id}/pathep-[{intf_name}]"

        interfaces.append({
            "vlan": vlan,
            "ip": ip_address,
            "secondary_ip": secondary_ip,
            "path": path,
            "mtu": mtu
        })

    # External EPG subnets
    ext_subnets = []
    print("Enter External EPG subnets (CIDR). Type 'done' when finished.")
    while True:
        subnet = input("Subnet (CIDR), or 'done' to finish: ").strip()
        if subnet.lower() == 'done':
            break
        if subnet:
            scope = input("Enter subnet scope (import/export-rtctrl/shared) [default export-rtctrl]: ").strip() or "export-rtctrl"
            ext_subnets.append(f'        <l3extSubnet ip="{subnet}" scope="{scope}" userdom=":all:"/>')

    if not ext_subnets:
        print("Note: No external EPG subnets were defined; the generated L3Out will contain no <l3extSubnet> entries.")

    ospf_area_id = input("Enter OSPF Area ID: ").strip()
    ospf_area_type = input("Enter OSPF Area Type [default nssa]: ").strip() or "nssa"

    # Build interface XML blocks
    interface_xml = ""
    for i, intf in enumerate(interfaces, 1):
        interface_xml += f'''
    <l3extLIfP name="{intf_profile_name}{i}" prio="unspecified" tag="yellow-green" userdom=":all:">
        <l3extRsPathL3OutAtt addr="{intf['ip']}" encap="vlan-{intf['vlan']}" ifInstT="ext-svi" mtu="{intf['mtu']}" tDn="{intf['path']}" userdom=":all:"/>'''
        if intf['secondary_ip']:
            interface_xml += f'''
        <l3extRsPathL3OutAtt addr="{intf['secondary_ip']}" encap="vlan-{intf['vlan']}" ifInstT="ext-svi" mtu="{intf['mtu']}" tDn="{intf['path']}" userdom=":all:"/>'''
        interface_xml += f'''
        <ospfIfP authKeyId="{ospf_auth_keyid}" authType="{ospf_auth_type}" userdom=":all:">
            <ospfRsIfPol tnOspfIfPolName="{ospf_if_pol_name}" userdom=":all:"/>
        </ospfIfP>
    </l3extLIfP>'''

    # Build subnets XML
    subnets_xml = "\n".join(ext_subnets)

    # Build contract XML (only provider OR consumer)
    if contract_scope == "consumer":
        contract_xml = f'        <fvRsCons tnVzBrCPName="{contract}"/>\n'
    else:  # provider
        contract_xml = f'        <fvRsProv tnVzBrCPName="{contract}"/>\_
