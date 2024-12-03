char = input('enter anyone letter ')
char = char.strip().lower()
if len(char) > 1 or len(char) < 1 or not(char.isalpha()):
    print('Error')
else:
    if char in ['a','e','i','o','u']:
        print('The vowel letter')
    elif char == 'y':
        print('Vovel and consonant letter')
    else:
        print('The consonant letter')
