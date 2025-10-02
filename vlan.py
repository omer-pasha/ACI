#!/usr/bin/env python3
"""
VLAN Pool XML Generator
Prompts for VLAN pool name and VLAN range (from/to)
"""

def create_vlan_pool():
    # Prompt for VLAN pool name
    pool_name = input("Enter VLAN Pool name: ").strip()
    if not pool_name:
        print("❌ VLAN pool name is required.")
        return

    # Prompt for VLAN range
    vlan_from = input("Enter VLAN start number: ").strip()
    vlan_to = input("Enter VLAN end number: ").strip()

    if not vlan_from.isdigit() or not vlan_to.isdigit():
        print("❌ VLAN numbers must be numeric.")
        return

    # Build XML
    xml_output = f"""<imdata totalCount="1">
  <fvnsVlanInstP allocMode="static" dn="uni/infra/vlanns-[{pool_name}]-static" name="{pool_name}">
    <fvnsEncapBlk from="vlan-{vlan_from}" to="vlan-{vlan_to}" allocMode="static" role="external"/>
  </fvnsVlanInstP>
</imdata>"""

    # Show result
    print("\n✅ Generated VLAN Pool XML:\n")
    print(xml_output)

    # Save to file
    filename = f"VLANPool_{pool_name}.xml"
    with open(filename, "w") as f:
        f.write(xml_output)
    print(f"\n💾 Saved as {filename}")


if __name__ == "__main__":
    create_vlan_pool()
