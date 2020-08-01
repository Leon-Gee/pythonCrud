def protected(func):

    def wrapper(password):
        
        if password == 'leon':
            return func()
        else:
            print('Password wrong as s8 of got')

    return wrapper


@protected
def protected_func():
    print('Your pass is correct my amigo')

if __name__ == "__main__":
    password = input(str('Type your password: '))
    protected_func(password)