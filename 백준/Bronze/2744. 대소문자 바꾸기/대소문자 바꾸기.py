word = input()

new_word = ''

for c in word:
    if c.isupper():
        new_word+=c.lower()
    else:
        new_word += c.upper()       

print(new_word)
