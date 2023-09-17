"""

import logging
import sys

# TODO: Research Harris ANW2 3G ALE interface
 
# Logging Setup 
logger = logging.getLogger('decoder_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

# Decode Harris ANW2 3G ALE
def decode_anw2_3g_ale(data):
	logger.info('Decoding Harris ANW2 3G ALE')
	# TODO: Code decoding logic