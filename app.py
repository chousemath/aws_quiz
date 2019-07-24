import json

with open('questions.json') as f:
    questions = json.load(f)

for key, val in questions.items():
    print(key)
    print(val)
