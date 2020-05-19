import datetime


class Logger:

    def __init__(self, print_log, encoding='utf-8'):
        self.log_file = open(print_log, 'a', encoding=encoding)

    def __enter__(self):
        return self

    def write_log(self, action):
        self.log_file.write(f'{datetime.datetime.now()}: {action}\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.write_log(f'error: {exc_val}')
        self.write_log('Клнец работы')
        self.log_file.close()


if __name__ == '__main__':
    with Logger('function.py') as log:
        log.write_log('Начало рабты')
        log.write_log('Время работы')