# Directions
# Given a string, return a new string with the reversed order of characters.
# Examples 'hello' = 'olleh'

# long solution
# Big O Anotation = O(n)
def r_string(word):
    # Used isinstance() instead of comparing types directly.
    if not isinstance(word, str):
        return False
    
    # create a variable that will store the reverse word
    reverse_word = ''
    
    # for loop backword and append each word
    for i in range(len(word)-1,-1, -1):
        reverse_word += word[i]
        
    return reverse_word

        


# slice solution
# O(1) annotation
def r_string_slice(word):
    # always check that the instance is of type string.
    if isinstance(word, str):
        # return the value reverse using slice.
        return word[::-1]
    
    return False


#  block in a Python script serves as a conditional statement that checks whether the script is being run directly or if it's being imported as a module.
if __name__ == '__main__':
    # Hello = olleH
    print(r_string('Hello')) 
    # backword = drowkcab
    print(r_string('backword'))
    
    print('\nSecond example')
    # elpmaxe
    print(r_string_slice('example'))
    # dlroW olleH
    print(r_string_slice('Hello World'))
    # False
    print(r_string_slice(12))