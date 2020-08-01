countries ={
    'mexico':1,
    'austria':2,
    'japan':3,
    'corea':4

}

while True:
    country = str(input('Type the name of a country: ')).lower()
    try:


        print('the number mason is {} and the country is {}'.format(countries[country],country))

    except:

        print('We dont have the number for that country')
     

    finally:

        print('Contact leon and he will add it, or maybe see another video for python learning, who knows')