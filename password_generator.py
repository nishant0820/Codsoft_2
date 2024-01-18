import random
import string

print("\n============= Welcome to Password Generator ===============")
def main():
    length=int(input("Enter the length of password: "))
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation

    combine=lowercase+uppercase+digits+symbols
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()
main()