import xml.etree.ElementTree as ET

def create_bd_element(bd_name, vrf_name):
    fvBD = ET.Element("fvBD", {
        "OptimizeWanBandwidth": "no",
        "annotation": "",
        "arpFlood": "yes",
        "descr": "",
        "enableRogueExceptMac": "no",
        "epClear": "no",
        "epMoveDetectMode": "",
        "hostBasedRouting": "no",
        "intersiteBumTrafficAllow": "no",
        "intersiteL2Stretch": "no",
        "ipLearning": "yes",
        "ipv6McastAllow": "no",
        "limitIpLearnToSubnets": "yes",
        "llAddr": "::",
        "mac": "00:22:BD:F8:19:FF",
        "mcastARPDrop": "yes",
        "mcastAllow": "no",
        "multiDstPktAct": "bd-flood",
        "name": bd_name,
        "nameAlias": "",
        "ownerKey": "",
        "ownerTag": "",
        "serviceBdRoutingDisable": "no",
        "type": "regular",
        "unicastRoute": "yes",
        "unkMacUcastAct": "flood",
        "unkMcastAct": "flood",
        "userdom": ":all:",
        "v6unkMcastAct": "flood",
        "vmac": "not-applicable"
    })
    ET.SubElement(fvBD, "fvRsBDToNdP", {"annotation": "", "tnNdIfPolName": "", "userdom": ":all:"})
    ET.SubElement(fvBD, "fvRsBdToEpRet", {"annotation": "", "resolveAct": "resolve", "tnFvEpRetPolName": "", "userdom": ":all:"})
    ET.SubElement(fvBD, "fvRsCtx", {"annotation": "", "tnFvCtxName": vrf_name, "userdom": ":all:"})
    ET.SubElement(fvBD, "fvRsIgmpsn", {"annotation": "", "tnIgmpSnoopPolName": "", "userdom": ":all:"})
    ET.SubElement(fvBD, "fvRsMldsn", {"annotation": "", "tnMldSnoopPolName": "", "userdom": ":all:"})
    return fvBD

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
    tenant_name = input("Enter Tenant Name: ").strip()
    if not tenant_name:
        print("Tenant name cannot be empty.")
        return

    vrf_name = input("Enter VRF (Context) Name: ").strip()
    if not vrf_name:
        print("VRF name cannot be empty.")
        return

    print("\nPaste BD names (one per line), then press Enter twice to finish:")
    bd_names = []
    while True:
        line = input()
        if line.strip() == "":
            break
        bd_names.append(line.strip())

    if not bd_names:
        print("No BD names entered. Exiting.")
        return

    # Root element <imdata totalCount="">
    root = ET.Element("imdata", {"totalCount": ""})

    # Tenant element inside <imdata>
    tenant = ET.SubElement(root, "fvTenant", {
        "annotation": "",
        "descr": "",
        "dn": f"uni/tn-{tenant_name}",
        "name": tenant_name,
        "nameAlias": "",
        "ownerKey": "",
        "ownerTag": "",
        "userdom": ":all:"
    })

    for bd_name in bd_names:
        tenant.append(create_bd_element(bd_name, vrf_name))

    indent(root)

    # Convert the tree to a string
    xml_output = ET.tostring(root, encoding="unicode")

    # Print to console
    print("\nGenerated XML:\n")
    print(xml_output)

    # Export to file
    file_name = f"{tenant_name}_bds.xml"
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(xml_output)
        print(f"\n✅ XML successfully written to '{file_name}'")
    except Exception as e:
        print(f"\n❌ Failed to write to file: {e}")

if __name__ == "__main__":
    main()
