from datetime import datetime, timedelta
import sys
from model import event
from model.config import LOG

filename = sys.argv[1]
lower_limit = datetime.now() - timedelta(minutes=int(sys.argv[2]))
LOG.info("Lower limit: %s", lower_limit, extra={'file':filename})
last_success = event.last(filename, 'pipeline-success')
LOG.info("Last success: %s", last_success, extra={'file':filename})
if last_success < lower_limit:
    LOG.error("Failed check", extra={'file':filename})
    sys.exit(2)
else:
    LOG.info("Ok check", extra={'file':filename})
