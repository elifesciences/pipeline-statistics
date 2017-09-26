from datetime import datetime
from . import config
import json

def parse_date(string):
    return datetime.strptime(string, "%Y-%m-%dT%H:%M:%S.%fZ")

def load_all(filename, type=None):
    with open(filename) as f:
        content = f.readlines()
        for line in content:
            event = json.loads(line)
            if type:
                if event['type'] != type:
                    continue
            event['datetime'] = parse_date(event['datetime'])
            yield event

def last(filename, type=None):
    for event in load_all(filename, type):
        last_success = event['datetime']
    return last_success
