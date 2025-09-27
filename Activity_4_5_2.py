import xml.etree.ElementTree as ET

# Original XML data
xml_data = '''<motorvehicles>
  <vehicle>
    <registration_no>CB11456</registration_no>
    <make>Toyota</make>
    <model>Innova</model>
  </vehicle>
  <vehicle>
    <registration_no>PR2245</registration_no>
    <make>Mazda</make>
    <model>Bongo</model>
  </vehicle>
  <vehicle>
    <registration_no>DE2115</registration_no>
    <make>TATA</make>
    <model>Sumo</model>
  </vehicle>
  <vehicle>
    <registration_no>CAR7785</registration_no>
    <make>Nissan</make>
    <model>Skyline</model>
  </vehicle>
</motorvehicles>'''

# Parse XML
root = ET.fromstring(xml_data)

# Update only the vehicle with registration_no DE2115
for vehicle in root.findall('vehicle'):
    reg = vehicle.find('registration_no')
    if reg is not None and reg.text == 'DE2115':
        vehicle.find('make').text = 'Nissan'
        vehicle.find('model').text = 'Skyline'

# Print registration numbers of Nissan vehicles with reg_no == DE2115
for vehicle in root.findall('vehicle'):
    reg = vehicle.find('registration_no')
    make = vehicle.find('make')
    if reg is not None and make is not None:
        if make.text == 'Nissan' and reg.text == 'DE2115':
            print(reg.text)
