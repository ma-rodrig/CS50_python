# implement a program that prompts the user for a str in English
# and then outputs the “emojized” version of that str, converting
# any codes (or aliases) therein to their corresponding emoji.

#load the emojize function(converts emoji aliases) from the emoji package
from emoji import emojize

text= input('Input: ')
#language='alias' interpret slack-style emoji aliases
#aliases: text shortcuts, written between colons (:)
print('Output:', emojize(text, language='alias'))

