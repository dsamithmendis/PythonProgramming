import xml.etree.ElementTree as ET

# Create root element
tag1 = ET.Element("tag1")

# Add subelements with correct text
ET.SubElement(tag1, "tag2").text = "Animal"
ET.SubElement(tag1, "tag3").text = "Domestic"

# Nested structure for tag4
tag4 = ET.SubElement(tag1, "tag4")
ET.SubElement(tag4, "tag4.1").text = "Cat"
ET.SubElement(tag4, "tag4.2").text = "Persian"

# Corrected values
ET.SubElement(tag1, "tag5").text = "Iran"
ET.SubElement(tag1, "tag6").text = "Male"
ET.SubElement(tag1, "tag7").text = "2021.05.04"

# Output the XML
ET.dump(tag1)
