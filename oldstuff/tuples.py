def first_not_repeating_char(char_sequence):
        
    for char in char_sequence:
        character = char_sequence.count(char)
        if character == 1:
            return char
        else:
            return '_'
    
if __name__ == "__main__":
    char_sequence = str(input("Type a secuence of characters: "))

    result = first_not_repeating_char(char_sequence)

    if result != "_":
        print("The first character that is not repeated is: {}".format(result) )
   
    else:
        print("All character are repeated, please, try again")