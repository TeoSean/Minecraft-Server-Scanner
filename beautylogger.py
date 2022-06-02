import datetime

class Logger:
    def __init__(self, filename, decorator, decorator_number):
        self.filename=filename
        self.decorator=decorator
        self.decorator_number=decorator_number
    def entry(self, entry_data):
        time=datetime.datetime.now()
        time_formatted=time.strftime('%d %B %Y, %H:%M:%S')
        file = open(self.filename, 'a+')
        file.write(self.decorator*self.decorator_number+'\n')
        print(self.decorator*self.decorator_number)
        file.write(f'Time: {time_formatted}\n')
        print(f'Time: {time_formatted}')
        for key in entry_data:
            file.write(f'{key}: {entry_data[key]}\n')
            print(f'{key}: {entry_data[key]}')
        file.close()

    def close(self):
        file = open(self.filename, 'a+')
        time=datetime.datetime.now()
        time_formatted=time.strftime('%d %B %Y, %H:%M:%S')
        file.write(self.decorator*self.decorator_number+'\n')
        file.write(f'File closed at {time_formatted}')
        