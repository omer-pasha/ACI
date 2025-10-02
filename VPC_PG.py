def create_vpc_policy_group():
    print("\n--- ACI vPC / Port-Channel Policy Group Generator ---\n")

    group_name = input("Enter Policy Group Name (e.g., NY-DC-CORSW-vPC): ").strip()
    lag_type = input("Enter LAG Type (node=vPC, link=Port-Channel): ").strip() or "node"
    lacp_policy = input("Enter LACP Policy Name (e.g., PC-LACP-Active): ").strip()
    speed_policy = input("Enter Speed Policy Name (e.g., Speed-10G): ").strip()
    mcp_policy = input("Enter MCP Policy Name (e.g., MCP-Enabled): ").strip()
    aaep_name = input("Enter AAEP Name (e.g., NY-DC-AAEP-CORSW): ").strip()

    xml_output = f'''<imdata totalCount="1">
<infraAccBndlGrp annotation="" descr="" dn="uni/infra/funcprof/accbundle-{group_name}" lagT="{lag_type}" name="{group_name}" nameAlias="" ownerKey="" ownerTag="" userdom=":all:">
    <infraRsLldpIfPol annotation="" tnLldpIfPolName="" userdom=":all:"/>
    <infraRsFcIfPol annotation="" tnFcIfPolName="" userdom=":all:"/>
    <infraRsLinkFlapPol annotation="" tnFabricLinkFlapPolName="" userdom=":all:"/>
    <infraRsLacpPol annotation="" tnLacpLagPolName="{lacp_policy}" userdom=":all:"/>
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
</infraAccBndlGrp>
</imdata>'''

    print("\n--- Generated XML ---\n")
    print(xml_output)


if __name__ == "__main__":
    create_vpc_policy_group()
