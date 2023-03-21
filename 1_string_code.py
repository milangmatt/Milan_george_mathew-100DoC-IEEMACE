def string_code(input_string):                  #function definition
    coded_string=""                             #init output string
    for chara in input_string:                  #traversal
        if chara>="a" and chara<="z":           #check for small letters
            coded_string+=str(ord(chara)-96)+" "
        elif chara>="A" and chara<="Z":         #check for capital letters
            coded_string+=str(ord(chara)-64)+" "
        else:                                   #for other characters
            continue
    return (coded_string)                       #function return
    
        
print(string_code("The sunset sets at twelve o' clock."))