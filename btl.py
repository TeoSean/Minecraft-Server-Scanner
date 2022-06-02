import datetime

class Logger:
    def __init__(self, decorator, decorator_number):
        # self.filename=filename
        self.decorator=decorator
        self.decorator_number=decorator_number
    def entry(self, entry_data):
        ent=''
        time=datetime.datetime.now()
        time_formatted=time.strftime('%d %B %Y, %H:%M:%S')
        # file = open(self.filename, 'a+')
        ent += self.decorator*self.decorator_number+'\n'
        print(self.decorator*self.decorator_number)
        ent += f'Time: {time_formatted}\n'
        print(f'Time: {time_formatted}')
        for key in entry_data:
            ent += f'{key}: {entry_data[key]}\n'
            print(f'{key}: {entry_data[key]}')
        # file.close()
        return ent

    def close(self):
        # file = open(self.filename, 'a+')
        ent = ''
        time=datetime.datetime.now()
        time_formatted=time.strftime('%d %B %Y, %H:%M:%S')
        ent += self.decorator*self.decorator_number+'\n'
        ent += f'File closed at {time_formatted}'
        