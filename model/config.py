import logging
FORMAT = "[%(asctime)-15s][%(levelname)s][%(name)s] %(message)s"

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(FORMAT))
LOG = logging.getLogger()
LOG.setLevel(logging.INFO)
LOG.addHandler(handler)
