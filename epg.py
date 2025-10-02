import xml.etree.ElementTree as ET

def create_epg_element(epg_name, bd_name, consumer_contract, provider_contract, domain_list):
    epg = ET.Element("fvAEPg", {
        "annotation": "",
        "descr": "",
        "exceptionTag": "",
        "floodOnEncap": "disabled",
        "fwdCtrl": "",
        "hasMcastSource": "no",
        "isAttrBasedEPg": "no",
        "matchT": "AtleastOne",
        "name": epg_name,
        "nameAlias": "",
        "pcEnfPref": "unenforced",
        "prefGrMemb": "exclude",
        "prio": "level3",
        "shutdown": "no",
        "userdom": ":all:"
    })

    ET.SubElement(epg, "fvRsBd", {
        "annotation": "",
        "tnFvBDName": bd_name,
        "userdom": ":all:"
    })

    ET.SubElement(epg, "fvRsCustQosPol", {
        "annotation": "",
        "tnQosCustomPolName": "",
        "userdom": ":all:"
    })

    # Consumer contract (if provided)
    if consumer_contract:
        ET.SubElement(epg, "fvRsCons", {
            "annotation": "",
            "intent": "install",
            "prio": "unspecified",
            "tnVzBrCPName": consumer_contract,
            "userdom": ":all:"
        })

    # Provider contract (if provided)
    if provider_contract:
        ET.SubElement(epg, "fvRsProv", {
            "annotation": "",
            "intent": "install",
            "matchT": "AtleastOne",
            "prio": "unspecified",
            "tnVzBrCPName": provider_contract,
            "userdom": ":all:"
        })

    # Domain attachments
    for domain in domain_list:
        ET.SubElement(epg, "fvRsDomAtt", {
            "annotation": "",
            "apiMode": "mgmt",
            "bindingType": "none",
            "classPref": "encap",
            "customEpgName": "",
            "delimiter": "",
            "encap": "unknown",
            "encapMode": "auto",
            "epgCos": "Cos0",
            "epgCosPref": "disabled",
            "instrImedcy": "lazy",
            "ipamDhcpOverride": "0.0.0.0",
            "ipamEnabled": "no",
            "ipamGateway": "0.0.0.0",
            "lagPolicyName": "",
            "netflowDir": "both",
            "netflowPref": "disabled",
            "numPorts": "0",
            "portAllocation": "none",
            "primaryEncap": "unknown",
            "primaryEncapInner": "unknown",
            "resImedcy": "immediate",
            "secondaryEncapInner": "unknown",
            "switchingMode": "native",
            "tDn": domain,
            "untagged": "no",
            "userdom": ":all:",
            "vnetOnly": "no"
        })

    return epg

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            indent(child, level+1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i

def main():
    # Prompts
    tenant_name = input("Enter Tenant Name: ").strip()
    if not tenant_name:
        print("Tenant name cannot be empty.")
        return

    app_profile_name = input("Enter Application Profile Name: ").strip()
    if not app_profile_name:
        print("Application Profile name cannot be empty.")
        return

    consumer_contract = input("Enter Consumer Contract Name (leave blank if none): ").strip()
    provider_contract = input("Enter Provider Contract Name (leave blank if none): ").strip()

    print("\nEnter Domain Distinguished Names (one per line), then press Enter twice to finish:")
    domain_list = []
    while True:
        domain = input()
        if domain.strip() == "":
            break
        domain_list.append(domain.strip())

    if not domain_list:
        print("At least one domain must be entered.")
        return

    print("\nEnter EPG names (one per line), then press Enter twice to finish:")
    epg_names = []
    while True:
        line = input()
        if line.strip() == "":
            break
        epg_names.append(line.strip())

    if not epg_names:
        print("No EPG names entered. Exiting.")
        return

    # Root XML
    root = ET.Element("imdata", {"totalCount": str(len(epg_names))})

    # fvAp (Application Profile)
    fvAp = ET.SubElement(root, "fvAp", {
        "annotation": "",
        "descr": "",
        "dn": f"uni/tn-{tenant_name}/ap-{app_profile_name}",
        "name": app_profile_name,
        "nameAlias": "",
        "ownerKey": "",
        "ownerTag": "",
        "prio": "unspecified",
        "userdom": ":all:"
    })

    # Create each EPG
    for epg_name in epg_names:
        # Using EPG name as BD name by default
        epg_element = create_epg_element(epg_name, epg_name, consumer_contract, provider_contract, domain_list)
        fvAp.append(epg_element)

    # Format and write output
    indent(root)
    xml_str = ET.tostring(root, encoding='unicode')

    output_file = f"{tenant_name}_{app_profile_name}_epgs.xml"
    try:
        with open(output_file, "w", encoding='utf-8') as f:
            f.write(xml_str)
        print(f"\n✅ XML output saved to '{output_file}'.")
    except Exception as e:
        print(f"\n❌ Failed to write to file: {e}")

if __name__ == "__main__":
    main()
