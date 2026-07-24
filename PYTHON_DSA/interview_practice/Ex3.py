## Palindrome or not

def palindrome(s):

    if s == s[::-1]:
        return True
    else:
        return False

s = "kanak"
print(palindrome(s))