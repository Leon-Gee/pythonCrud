def run():
    counter = 0
    with open('numbers.txt') as f:
       for line in f:
           counter += line.count('1')
           print('you can find one {} times'.format(counter))


if __name__ == "__main__":
    run()