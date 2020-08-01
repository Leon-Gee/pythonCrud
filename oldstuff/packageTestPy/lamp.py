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