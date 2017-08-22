import sys
from model import event
from model.config import LOG

filename = sys.argv[1]
LOG.info(event.last(filename, 'pipeline-success'), extra={'file':filename})
