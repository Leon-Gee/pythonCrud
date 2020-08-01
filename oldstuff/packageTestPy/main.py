from lamp import DesktopLamp



def run():
    lamp = DesktopLamp(is_turned_on=False)
     
    while True:
        command = str(input('''Hi, welcome, tell me, what you want to do with your lamp my valedor?        
        A)Turn on
        B)Turn off
        Anything else) Exit
        ''')).upper()
        
        if command == 'A':
            if lamp.is_on() == True:
                print(chr(27)+'[2j')
                print('\033c')
                print('\x1bc')
                print('The lamp is already turned on')
            else:
             lamp.turn_on()
        elif command == 'B':
            if lamp.is_on() == False:
                print(chr(27)+'[2j')
                print('\033c')
                print('\x1bc')
                print('The lamp is already turned off')
            else:
                lamp.turn_off()
        else:
            break

if __name__ == "__main__":
    run()

