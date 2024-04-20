from flask import Flask
import logging
from logger import set_file_handler, FORMATTER

app = Flask(__name__)
# logging默认WARNING级别
if app.debug:
    app.logger.setLevel(logging.DEBUG)
else:
    app.logger.setLevel(logging.INFO)

set_file_handler(app.logger, 'main.log', FORMATTER)


from apis.proxy import *