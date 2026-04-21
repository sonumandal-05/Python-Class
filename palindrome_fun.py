def is_palindrome(word):
    rev_word=word[::-1]
    if word==rev_word:
        return True
    else:  
        return False
print(is_palindrome("madam"))