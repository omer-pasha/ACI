def create_single_interface_policy_group():
    print("\n--- ACI Single Interface Policy Group Generator ---\n")

    group_name = input("Enter Policy Group Name (e.g., NY-DC-Access-Leaf1): ").strip()
    speed_policy = input("Enter Speed Policy Name (e.g., Speed-10G): ").strip()
    mcp_policy = input("Enter MCP Policy Name (e.g., MCP-Enabled): ").strip()
    aaep_name = input("Enter AAEP Name (e.g., NY-DC-AAEP-Access): ").strip()

    xml_output = f'''<imdata totalCount="1">
<infraAccPortGrp annotation="" descr="" dn="uni/infra/funcprof/accportgrp-{group_name}" name="{group_name}" nameAlias="" ownerKey="" ownerTag="" userdom=":all:">
    <infraRsLldpIfPol annotation="" tnLldpIfPolName="" userdom=":all:"/>
    <infraRsFcIfPol annotation="" tnFcIfPolName="" userdom=":all:"/>
    <infraRsLinkFlapPol annotation="" tnFabricLinkFlapPolName="" userdom=":all:"/>
    <infraRsL2PortAuthPol annotation="" tnL2PortAuthPolName="" userdom=":all:"/>
    <infraRsL2PortSecurityPol annotation="" tnL2PortSecurityPolName="" userdom=":all:"/>
    <infraRsHIfPol annotation="" tnFabricHIfPolName="{speed_policy}" userdom=":all:"/>
    <infraRsQosPfcIfPol annotation="" tnQosPfcIfPolName="" userdom=":all:"/>
    <infraRsCoppIfPol annotation="" tnCoppIfPolName="" userdom=":all:"/>
    <infraRsL2IfPol annotation="" tnL2IfPolName="" userdom=":all:"/>
    <infraRsCdpIfPol annotation="" tnCdpIfPolName="" userdom=":all:"/>
    <infraRsStpIfPol annotation="" tnStpIfPolName="" userdom=":all:"/>
    <infraRsSynceEthIfPolBndlGrp annotation="" tnSynceEthIfPolName="" userdom=":all:"/>
    <infraRsQosLlfcIfPol annotation="" tnQosLlfcIfPolName="" userdom=":all:"/>
    <infraRsQosIngressDppIfPol annotation="" tnQosDppPolName="" userdom=":all:"/>
    <infraRsMacsecIfPol annotation="" tnMacsecIfPolName="" userdom=":all:"/>
    <infraRsStormctrlIfPol annotation="" tnStormctrlIfPolName="" userdom=":all:"/>
    <infraRsQosEgressDppIfPol annotation="" tnQosDppPolName="" userdom=":all:"/>
    <infraRsMonIfInfraPol annotation="" tnMonInfraPolName="" userdom=":all:"/>
    <infraRsMcpIfPol annotation="" tnMcpIfPolName="{mcp_policy}" userdom=":all:"/>
    <infraRsAttEntP annotation="" tDn="uni/infra/attentp-{aaep_name}" userdom=":all:"/>
    <infraRsQosSdIfPol annotation="" tnQosSdIfPolName="" userdom=":all:"/>
</infraAccPortGrp>
</imdata>'''

    print("\n--- Generated XML ---\n")
    print(xml_output)


if __name__ == "__main__":
    create_single_interface_policy_group()
