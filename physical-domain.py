#!/usr/bin/env python3
"""
Physical Domain with VLAN Pool Reference XML Generator
Prompts for Physical Domain name and VLAN Pool name
"""

def create_phys_domain_with_vlan():
    # Prompt for Physical Domain name
    domain_name = input("Enter Physical Domain name: ").strip()
    if not domain_name:
        print("❌ Physical Domain name is required.")
        return

    # Prompt for VLAN Pool name
    vlan_pool_name = input("Enter VLAN Pool name: ").strip()
    if not vlan_pool_name:
        print("❌ VLAN Pool name is required.")
        return

    # Build XML
    xml_output = f"""<imdata totalCount="1">
  <physDomP dn="uni/phys-{domain_name}" name="{domain_name}">
    <infraRsVlanNs tDn="uni/infra/vlanns-[{vlan_pool_name}]-static"/>
  </physDomP>
</imdata>"""

    # Show result
    print("\n✅ Generated Physical Domain XML with VLAN Pool Reference:\n")
    print(xml_output)

    # Save to file
    filename = f"PhysDomain_{domain_name}.xml"
    with open(filename, "w") as f:
        f.write(xml_output)
    print(f"\n💾 Saved as {filename}")


if __name__ == "__main__":
    create_phys_domain_with_vlan()
