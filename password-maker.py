#python project
#password-maker
#mehraan kiya

import string

from random import *

print("""

Password maker version 1.0

Coded By *m3hr44n*       https://github.com/m3hr44n


Create a strong password for yourself in no time


""")

char = string.ascii_letters + string.punctuation + string.digits

#password is composition ==> cahr

password = "".join(choice(char) for x in range(randint(18,30)))

#for that password strong sparrow 

print("this is your password : " , password)
