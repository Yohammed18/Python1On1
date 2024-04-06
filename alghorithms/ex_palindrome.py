# Given a string, return true if the string is a palindrome or false if it's not. Palindroms are strings that form the word if it is reversed. 

# import the function that you will use to return the word backwords
import ex_reverse as rs


# create the palindrome function
def palindrome(word):
    # store the word in reverse
    reverse_word = rs.r_string_slice(word)
    
    # if else statement to chek if its a palindrome
    if word == reverse_word:
        return True
    else:
        return False
    

if __name__ == '__main__':
    # abba = True
    # abdefgs = false
    print(palindrome('abba'))
    print(palindrome('abdfece'))
    # palindrome word that will return true
    print()
    print(palindrome('radar'))
    print(palindrome('level'))
    print(palindrome('deified'))



