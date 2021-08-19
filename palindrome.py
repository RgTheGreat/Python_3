import sys
print("THIS IS A APP TO CHECK IF A WORD IS PALINDROME")

def check_palindrome(x):
    length_word = len(x)
    for i in range(length_word):
        if x[i] != x[length_word -i -1]:
            return False
        i = i + 1
    return True

while 1:
    x = input("type the word: ")
    if x == "exit":
        sys.exit()

    if check_palindrome(x) == True:
        print("it is a palindrome")
    else:
        print("It is not a palindrome")
