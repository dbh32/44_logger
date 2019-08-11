from datetime import datetime
import re


def logger_path(path='C:\\Temp\\'):
    def logger(func):
        def target_func(*args, **kwargs):
            timestamp = str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S"))
            timestamp_format = re.sub(r"[.:]", "_", timestamp).replace(' ', '-')
            func_return = func(*args, **kwargs)
            with open(f'{path}' + f'{timestamp_format}' + '-' + f'{func.__name__}.txt',
                      'wt', encoding='utf-8-sig') as log_file:
                log_file.write(timestamp + '\n' + '\n' +
                               'Function: ' + func.__name__ + '\n' +
                               'Params: ' + '\n' +
                               '    Args: ' + str(args) + '\n' +
                               '    Kwargs: ' + str(kwargs) + '\n' + '\n' +
                               'Return: ' + '\n' + str(func_return))
            return func_return

        return target_func

    return logger
