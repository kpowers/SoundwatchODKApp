#May 5, 2016 Kelsey Powers
#Pyg Latin function made on Codecademy

pyg = 'ay'
#ask for user tp input a word
original = raw_input('Enter a word:')

#check to make sure that it is a word
if len(original) > 0 and original.isalpha():
    #change case to lower
    word=original.lower()
    #grab the first letter to move to end of word
    first=word[0]
    #concatenate new word adding first letter and 'ay' to end
    new_word = word[1:] + first + pyg
else:
    #user input is not a word
    print 'empty'
