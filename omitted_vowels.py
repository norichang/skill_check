s = input()
new_string = ''

for letter in s:
    if letter not in 'aeiou':
        new_string += letter

print (new_string)
