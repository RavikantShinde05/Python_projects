import random
import string
from shlex import join



print ("Welcome to Random Password Generator")


Length_pwd=int(input("Enter the length of your Password:"))
lowerD =string.ascii_lowercase
upperD =string.ascii_uppercase
digitD =string.digits
symbolsD = string.punctuation

combine = lowerD+upperD+digitD+symbolsD

x = random.sample(combine, Length_pwd)
password=join(x)
print(password)

