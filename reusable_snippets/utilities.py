import time
import logging

logger = logging.getLogger('todo: Change Logger Name')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)s] (%(filename)s:%(lineno)s) %(asctime)s :: %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            logger.info('%s.%s %2.2f ms' % \
                        (args[0],method.__name__, (te - ts) * 1000))
        return result

    return timed