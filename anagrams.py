# First string and second string
# Sort both and compare if they are equal
def isAnagram(s, t):

    word1 = s.lower()
    word2 = t.lower()

    word1 = sorted(word1)
    word2 = sorted(word2)

    print(word1, word2)

    if word1 == word2:
      return True
    else:
      return False

print(isAnagram("ANA", "NAA"))