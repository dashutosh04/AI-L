import json

jsonlike = '{"help":1234, "send":23456}'

print(json.loads(jsonlike))