import requests

base_url = 'http://host1.open.uom.lk:8080'

response = requests.get(f"{base_url}/api/products/")
data = response.json()

#data => #{'message': 'success', 'data': [{'id': 680, 'productName': 'Araliya Basmathi Rice', 'description': 'White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.', 'category': 'Rice', 'brand': 'Araliya', 'expiredDate': '2023.05.04', 'manufacturedDate': '2022.02.20', 'batchNumber': 324567, 'unitPrice': 1020, 'quantity': 200, 'createdDate': '2022.02.24'}, {'id': 686, 'productName': 'Araliya Basmathi Rice', 'description': 'White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.', 'category': 'Rice', 'brand': 'CIC', 'expiredDate': '2023.05.04', 'manufacturedDate': '2022.02.20', 'batchNumber': 324567, 'unitPrice': 1020, 'quantity': 200, 'createdDate': '2022.02.24'}]}


products = data['data']
print(len(products))
