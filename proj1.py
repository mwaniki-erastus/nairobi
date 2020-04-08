#!/usr/bin/env python

def main(args):
    message= "Hello world"
    print(message)
    
    # changing the value of avariable at any point during execution
    message = "wachana na hii editor ni shit"
    
    #using methods to alter the variable in upper/lower/title cases
    print(message.title())
    print(message.upper())
    print(message.lower())
    
    #concatenating strings
    first_name = "erastus"
    last_name = "mwaniki"
    print(first_name.title() + " " + last_name.title())
    
    #using \t -tab and \n-newlines
    languages = "I will need to study:\n\tPython\n\tDjango\n\tR\n\tPentesting\n\tflask\n\tamongg others"
    print(languages)
    
    #using rstrip()/.lstrip() methods to remove extra space before/after a string
    fav_lang = "   The favorite language is python   "
    fav_lang = fav_lang.rstrip()
    fav_lang = fav_lang.lstrip()
    print(fav_lang)
    
    #exponential/floats and using str() mehod to display an integer in the same line with a string
    exponent = 2**3
    print("the value of 2**3 is "+ str(exponent))
    a = 101
    b = 2.67
    c = a * b
    print(c)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
