#Check if a string is a palindrome

word = "Nurses Run"

cleaned = word.lower().replace(" ", "")
reversed_word = cleaned[::-1]

if cleaned == reversed_word:
    print("Palindrome")
else:
    print("Not Palindrome")