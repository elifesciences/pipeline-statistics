from datetime import datetime
import json

def load_all(filename, type=None):
    with open(filename) as f:
        content = f.readlines()
        for line in content:
            event = json.loads(line)
            if type:
                if event['type'] != type:
                    continue
            event['datetime'] = datetime.strptime(event['datetime'], "%Y-%m-%dT%H:%M:%S.%fZ")
            yield event
