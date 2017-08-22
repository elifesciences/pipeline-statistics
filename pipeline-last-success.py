import sys
from model import event
from model.config import LOG

LOG.info(event.last(sys.argv[1], 'pipeline-success'))
