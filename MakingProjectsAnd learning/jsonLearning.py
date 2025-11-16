import json

data = {
    "name": "Shivam",
    "age": 15,
    "skills": ["Python", "AI", "Math"]
}

# Save (write) data to a file
with open("data.json", "w") as f:
    json.dump(data, f)
with open("data.json","r") as f:
    data = json.load(f)
    print(data)