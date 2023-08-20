#Two pointers solution
def palindrome(s):
    l, r = 0, len(s) -1

    s = s.lower()

    while l < r:
        while not s[l].isalnum():
            l += 1
        while not s[r].isalnum():
            r -=1
        if s[l] != s[r]:
            return False
        l, r = l+1, r-1
    return True

print(palindrome("A man, a plan, a canal: Panama"))