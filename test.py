import re
import pyperclip as clip

result = re.compile(r'''(
 ((\d{3})|(\(\d{3}\)))? # first seperator
 (\s|-) # space or dash
 \d{3}  # 3 digit
 -       #seperator
 \d{4}       #last 4 digits
 (((ext(\.)?\s)|x)
 (\d{2,5}))?)      #extensions optional
''', re.VERBOSE)
email_re = re.compile(r'''
[a-zA-Z0-9_.+]+ #sub domain
@               # atsign
[a-zA-Z0-9_.+]+ # extensio
'''
, re.VERBOSE)
# name_re = r'\w*\s\w*'
# number_re = re.compile(r'(\d{3}-\d{3}-\d{4})')
# email_re = re.compile(r'\w*@\w*.\w*')
# info_re = re.compile(r'\w*\w*, \d{3}-\d{3}-\d{4}, \w*@\w*.\w*')
# results = info_re.findall(number_pattern, re.VERB
total = result.findall(clip.paste())
str = ''
total_numbers = []
for i in total:
    total_numbers.append(i[0])
str = '\n'.join(total_numbers)
clip.copy(str)