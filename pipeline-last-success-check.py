from datetime import datetime, timedelta
import sys
from model import event
from model.config import LOG

lower_limit = datetime.now() - timedelta(minutes=int(sys.argv[2]))
LOG.info("Lower limit: %s", lower_limit)
last_success = event.last(sys.argv[1], 'pipeline-success')
LOG.info("Last success: %s", last_success)
if last_success < lower_limit:
    LOG.error("Failed check")
    sys.exit(2)
else:
    LOG.info("Ok check")
