def main():
    number = int(input('Type the number for the analysis: '))
     print('Is the number a prime number? ')
    if prime(number) == True:
        print('yes')
    else:
        print('no')

  

def prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3,number):
            if number % i == 0:
                return False
            
    return True
               


if __name__ == '__main__':
  main()