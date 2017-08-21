import sys
from model import event

for event in event.load_all(sys.argv[1]):
    if event['type'] != 'pipeline-success':
        continue
    last_success = event['datetime']

print last_success
