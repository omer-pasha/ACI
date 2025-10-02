import xml.etree.ElementTree as ET

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
        print("❌ Tenant name cannot be empty.")
        return

    root = ET.Element("imdata", {"totalCount": "1"})

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

    indent(root)
    xml_str = ET.tostring(root, encoding="unicode")

    output_file = f"tenant_{tenant_name}.xml"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(xml_str)
        print(f"\n✅ Tenant XML saved to '{output_file}'")
    except Exception as e:
        print(f"\n❌ Error writing to file: {e}")

if __name__ == "__main__":
    main()
