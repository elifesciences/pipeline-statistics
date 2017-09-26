from model import event
from datetime import datetime
import sys

start_date = end_date = None
if len(sys.argv) > 2:
    start_date = event.parse_date(sys.argv[2])

if len(sys.argv) > 3:
    end_date = event.parse_date(sys.argv[3])

runs = {}
for event in event.load_all(sys.argv[1]):
    run = runs.get(event['number'], {})
    run[event['type']] = event['datetime']
    runs[event['number']] = run

if start_date:
     runs = {k:v for k,v in runs.items() if v.get('pipeline-start') > start_date}

if end_date:
     runs = {k:v for k,v in runs.items() if v.get('pipeline-start') < end_date}

successes = 0
total = 0
success_times = []
for r in runs:
    total = total + 1
    if 'pipeline-success' in runs[r]:
        successes = successes + 1
        success_times.append((runs[r]['pipeline-success'] - runs[r]['pipeline-start']).total_seconds())

failure_rate = (1 - (float(successes) / total)) * 100
if success_times:
    average_success_time = float(sum(success_times)) / successes
else:
    average_success_time = -1
print "%.1f,%d,%d" % (failure_rate, average_success_time, total)
