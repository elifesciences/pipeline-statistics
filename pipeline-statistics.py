from model import event
import sys

runs = {}
for event in event.load_all(sys.argv[1]):
    run = runs.get(event['number'], {})
    run[event['type']] = event['datetime']
    runs[event['number']] = run

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
