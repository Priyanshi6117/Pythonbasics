n=input("Enter:").split()
a=list(n)
b=a.copy()
a.reverse()
if (a==b):
    print("It is a palindrome of elements.")
else:
    print("It is not a palindrome of elements.")