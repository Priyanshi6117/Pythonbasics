word=input("Enter a word:")
for char in word:
    if word.count(char)==1:
        print("The first non-repeated character is", char)
        break