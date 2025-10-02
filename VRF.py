import xml.etree.ElementTree as ET

def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            indent(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i

def create_vrf_element(tenant_name, vrf_name, pc_enf_pref, pc_enf_dir):
    ctx = ET.Element("fvCtx", {
        "annotation": "",
        "bdEnforcedEnable": "no",
        "descr": "",
        "dn": f"uni/tn-{tenant_name}/ctx-{vrf_name}",
        "ipDataPlaneLearning": "enabled",
        "knwMcastAct": "permit",
        "name": vrf_name,
        "nameAlias": "",
        "ownerKey": "",
        "ownerTag": "",
        "pcEnfDir": pc_enf_dir,
        "pcEnfPref": pc_enf_pref,
        "userdom": ":all:",
        "vrfIndex": "0"
    })

    ET.SubElement(ctx, "fvRsBgpCtxPol", {
        "annotation": "",
        "tnBgpCtxPolName": "",
        "userdom": ":all:"
    })

    ET.SubElement(ctx, "fvRsCtxToExtRouteTagPol", {
        "annotation": "",
        "tnL3extRouteTagPolName": "",
        "userdom": ":all:"
    })

    ET.SubElement(ctx, "fvRsCtxToEpRet", {
        "annotation": "",
        "tnFvEpRetPolName": "",
        "userdom": ":all:"
    })

    ET.SubElement(ctx, "fvRsOspfCtxPol", {
        "annotation": "",
        "tnOspfCtxPolName": "",
        "userdom": ":all:"
    })

    ET.SubElement(ctx, "vzAny", {
        "annotation": "",
        "descr": "",
        "matchT": "AtleastOne",
        "name": "",
        "nameAlias": "",
        "prefGrMemb": "disabled",
        "userdom": ":all:"
    })

    ET.SubElement(ctx, "fvRsVrfValidationPol", {
        "annotation": "",
        "tnL3extVrfValidationPolName": "",
        "userdom": ":all:"
    })

    return ctx

def main():
    tenant_name = input("Enter Tenant Name: ").strip()
    if not tenant_name:
        print("❌ Tenant name cannot be empty.")
        return

    vrf_name = input("Enter VRF Name: ").strip()
    if not vrf_name:
        print("❌ VRF name cannot be empty.")
        return

    # Policy Control Enforcement Preference
    while True:
        pc_enf_pref = input("Enter Policy Control Enforcement Preference (enforced/unenforced): ").strip().lower()
        if pc_enf_pref in ["enforced", "unenforced"]:
            break
        else:
            print("❌ Invalid input. Please enter 'enforced' or 'unenforced'.")

    # Policy Control Enforcement Direction
    while True:
        pc_enf_dir = input("Enter Policy Control Enforcement Direction (ingress/egress): ").strip().lower()
        if pc_enf_dir in ["ingress", "egress"]:
            break
        else:
            print("❌ Invalid input. Please enter 'ingress' or 'egress'.")

    # Create root
    root = ET.Element("imdata", {"totalCount": "1"})

    # Create VRF
    vrf_element = create_vrf_element(tenant_name, vrf_name, pc_enf_pref, pc_enf_dir)
    root.append(vrf_element)

    indent(root)
    xml_str = ET.tostring(root, encoding="unicode")

    output_file = f"vrf_{vrf_name}.xml"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(xml_str)
        print(f"\n✅ VRF XML saved to '{output_file}'")
    except Exception as e:
        print(f"\n❌ Failed to write file: {e}")

if __name__ == "__main__":
    main()
