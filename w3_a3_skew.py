import re
pattern = '[A-Za-z]'
def wrong_name(name):
    word = name.split(' ')
    print(word)
    first_name = ''.join(re.findall(pattern, word[0]))
    last_name = ''.join(re.findall(pattern, word[1])) or ''
    result = first_name + ' ' + last_name
    print(result)

wrong_name("!+Steven Rogers23")
wrong_name("%Harry !Potter")