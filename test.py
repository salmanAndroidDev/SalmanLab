import re

message = """my main purpose is automating stuff i wanna use
 something like automail, autoprocess most of my stuff and autocompile to comile easily
 beyond that i'm crazy about as also my mail is salmanAndroidDev@yahoo.com also sbmlai25@gmail.com
 by the way no no no  i would like there male is female and also afdefeafefdedfemadle and amale to autotweet and autopost my last mail is salmanAndB@outlook.com before
 i had salmanplusb@gmail.com and also salmanplusb@yahoo.com. u can check +-*/+-*/+-*/+-*/+-*/n
 my phone number is 915753-3678 by the way salman would you like to have dinner?"""

regx_object = re.compile(r'(\d\d\d\d\d-)?(\d\d\d-)?\d\d\d-\d\d\d\d')
another_rej = re.compile(r'(\d){3,}-(\d){4}')
mo = another_rej.search(message)

print(mo)