def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

str1 = "Hello"
if is_palindrome(str1):
    print("Palindrome")
else:
    print("Not a palindrome")


# output
# Not a palindrome