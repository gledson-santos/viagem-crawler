import logging
import graypy

logger = logging.getLogger('voo_crawler')
logger.setLevel(logging.DEBUG)

handler = graypy.GELFHTTPHandler(host='127.0.0.1', port=12201)
logger.addHandler(handler)
