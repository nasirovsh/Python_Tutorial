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


def timeit_example_1():
    @timeit
    def test():
        time.sleep(2)
        return 'test'

    test()


def timeit_example_2():
    log_time = {}

    @timeit
    def multiply_numbers(a, b):
        time.sleep(2)  # simulate a time-consuming operation
        return a * b

    multiply_numbers(3, 4, log_time=log_time, log_name='MULTIPLY_NUMBERS')

    print(log_time)


def timeit_example_3():
    class MyClass:
        @timeit
        def method(self, a, b):
            time.sleep(2)  # simulate a time-consuming operation
            return a + b

    obj = MyClass()
    obj.method(3, 4)


if __name__ == '__main__':
    timeit_example_1()
    timeit_example_2()
    timeit_example_3()
