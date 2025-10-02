#!/usr/bin/env python3
"""
L3 Domain XML Generator
Prompts for L3 Domain name and VLAN Pool name
"""

def create_l3_domain():
    # Prompt for L3 Domain name
    l3_domain_name = input("Enter L3 Domain name: ").strip()
    if not l3_domain_name:
        print("❌ L3 Domain name is required.")
        return

    # Prompt for VLAN Pool name
    vlan_pool_name = input("Enter VLAN Pool name: ").strip()
    if not vlan_pool_name:
        print("❌ VLAN Pool name is required.")
        return

    # Build XML
    xml_output = f"""<imdata totalCount="1">
  <l3extDomP dn="uni/l3dom-{l3_domain_name}" name="{l3_domain_name}">
    <infraRsVlanNs tDn="uni/infra/vlanns-[{vlan_pool_name}]-static"/>
  </l3extDomP>
</imdata>"""

    # Show result
    print("\n✅ Generated L3 Domain XML:\n")
    print(xml_output)

    # Save to file
    filename = f"L3Domain_{l3_domain_name}.xml"
    with open(filename, "w") as f:
        f.write(xml_output)
    print(f"\n💾 Saved as {filename}")


if __name__ == "__main__":
    create_l3_domain()
