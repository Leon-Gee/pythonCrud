class DesktopLamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self,is_turned_on):
        self.__is_turned_on = False

    def turn_on(self):
        self.__is_turned_on = True
        self.display_image()

    def turn_off(self):
        self.__is_turned_on = False
        self.display_image()
    
    def display_image(self):
        if self.__is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
    
    def is_on(self):
        if self.__is_turned_on:
            return True
        else:
            return False


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

