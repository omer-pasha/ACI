#!/usr/bin/env python3
"""
AAEP (Attachable Access Entity Profile) XML Generator
Flexible: can bind to Physical or L3 Domain
"""

def create_aaep():
    # Prompt for AAEP name
    aaep_name = input("Enter AAEP name: ").strip()
    if not aaep_name:
        print("❌ AAEP name is required.")
        return

    # Prompt for Domain type
    domain_type = input("Enter Domain type (phys/l3ext): ").strip().lower()
    if domain_type not in ["phys", "l3ext"]:
        print("❌ Invalid domain type. Use 'phys' or 'l3ext'.")
        return

    # Prompt for Domain name
    domain_name = input("Enter Domain name: ").strip()
    if not domain_name:
        print("❌ Domain name is required.")
        return

    # Build XML
    xml_output = f"""<imdata totalCount="1">
  <infraAttEntityP dn="uni/infra/attentp-{aaep_name}" name="{aaep_name}">
    <infraRsDomP tDn="uni/{domain_type}dom-{domain_name}"/>
  </infraAttEntityP>
</imdata>"""

    # Show result
    print("\n✅ Generated AAEP XML:\n")
    print(xml_output)

    # Save to file
    filename = f"AAEP_{aaep_name}.xml"
    with open(filename, "w") as f:
        f.write(xml_output)
    print(f"\n💾 Saved as {filename}")


if __name__ == "__main__":
    create_aaep()
