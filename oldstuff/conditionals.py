def main():
    age = int(input('Hi, my name is leon, tell me, how old are you? '))
    say_hello(age)


def say_hello(age):
    if age >= 18:
        print('Wow, you are an adult')
    else:
            print('Wow, you are a kid lol')

if __name__ == '__main__':
  main()