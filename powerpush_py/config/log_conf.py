import logging
import colorlog

log_format = (
    '%(asctime)s - '
    '%(log_color)s%(levelname)-6s%(reset)s '
    '%(filename)s:%(lineno)-3s '
    '%(message)s'
)
log_colors_config = {
    'DEBUG':    'cyan',
    'INFO':     'green',
    'WARNING':  'yellow',
    'ERROR':    'red',
    'CRITICAL': 'red,bg_white',
}

def setup_logger():
    colorlog.basicConfig(
        format=log_format,
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG,
        log_colors=log_colors_config
    )