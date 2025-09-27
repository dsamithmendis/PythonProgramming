import json

# JSON string containing two objects in a list
myVar = '[{"name": "Bob", "languages": ["English", "French"]}, {"name": "Alice", "languages": ["Spanish"]}]'

# Parse the JSON string
data = json.loads(myVar)

# Count JSON objects
count = len(data) if isinstance(data, list) else 1

print(count)
