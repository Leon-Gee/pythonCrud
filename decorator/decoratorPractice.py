PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('Please, type your password: ')

        if password == PASSWORD:
            return func()
        else:
             print('Your password its incorrect')
    return wrapper


@password_required
def needs_password():
    print('Password its correct')


def upper(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)

        return result.upper()

    return wrapper

@upper
def sayMyName(name):
    return 'Hi, {} '.format(name)




if __name__ == '__main__':
    print(sayMyName('heinsenberg'))
    