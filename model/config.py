import logging
FORMAT = "[%(asctime)-15s][%(levelname)s][%(file)s] %(message)s"
LOG = logging.getLogger()

class MakeFileOptionalFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'file'):
            record.file = ''
        return True

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(FORMAT))
handler.addFilter(MakeFileOptionalFilter())
LOG.setLevel(logging.INFO)
LOG.addHandler(handler)

handler = logging.FileHandler('pipeline-statistics.log')
handler.setFormatter(logging.Formatter(FORMAT))
handler.addFilter(MakeFileOptionalFilter())
LOG.setLevel(logging.DEBUG)
LOG.addHandler(handler)
