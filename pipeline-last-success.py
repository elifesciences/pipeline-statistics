from datetime import datetime
import json
import sys

with open(sys.argv[1]) as f:
    content = f.readlines()

runs = {}
for line in content:
    event = json.loads(line)
    if event['type'] != 'pipeline-success':
        continue
    last_success = datetime.strptime(event['datetime'], "%Y-%m-%dT%H:%M:%S.%fZ")

print last_success
